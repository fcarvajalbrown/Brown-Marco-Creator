import argparse
import csv
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PREFIX = "UnrealEditor-"
SOURCE_AREAS = ("Runtime", "Editor", "Developer", "Programs")
IMPORT_HEADER = re.compile(r"^\s*(Import|DelayImport)\s*\{")
NAME_LINE = re.compile(r"^\s*Name:\s*(\S+\.dll)\s*$", re.IGNORECASE)


def module_name(dll_name):
    stem = Path(dll_name).stem
    return stem[len(PREFIX):] if stem.startswith(PREFIX) else None


def read_imports(dll_path):
    output = subprocess.run(
        ["llvm-readobj", "--coff-imports", str(dll_path)],
        capture_output=True, text=True, check=True,
    ).stdout
    direct, delayed = set(), set()
    kind = None
    for line in output.splitlines():
        header = IMPORT_HEADER.match(line)
        if header:
            kind = header.group(1)
            continue
        name = NAME_LINE.match(line)
        if name and kind:
            dependency = module_name(name.group(1))
            if dependency:
                (delayed if kind == "DelayImport" else direct).add(dependency)
            kind = None
    return direct, delayed


def source_areas(engine_source):
    areas = {}
    for area in SOURCE_AREAS:
        for build_file in (engine_source / area).rglob("*.Build.cs"):
            areas.setdefault(build_file.name[: -len(".Build.cs")], area)
    return areas


def strongly_connected(graph):
    index, low, stack, on_stack, components = {}, {}, [], set(), []
    counter = [0]

    def visit(start):
        work = [(start, iter(sorted(graph[start])))]
        index[start] = low[start] = counter[0]
        counter[0] += 1
        stack.append(start)
        on_stack.add(start)
        while work:
            node, children = work[-1]
            advanced = False
            for child in children:
                if child not in index:
                    index[child] = low[child] = counter[0]
                    counter[0] += 1
                    stack.append(child)
                    on_stack.add(child)
                    work.append((child, iter(sorted(graph[child]))))
                    advanced = True
                    break
                if child in on_stack:
                    low[node] = min(low[node], index[child])
            if advanced:
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[node])
            if low[node] == index[node]:
                component = []
                while True:
                    member = stack.pop()
                    on_stack.discard(member)
                    component.append(member)
                    if member == node:
                        break
                components.append(sorted(component))

    for node in sorted(graph):
        if node not in index:
            visit(node)
    return components


def layers(graph):
    components = strongly_connected(graph)
    component_of = {m: i for i, c in enumerate(components) for m in c}
    layer = {}
    for i, component in enumerate(components):
        below = [
            layer[component_of[d]]
            for m in component
            for d in graph[m]
            if component_of[d] != i
        ]
        layer[i] = 1 + max(below, default=-1)
    return {m: layer[component_of[m]] for m in graph}, components


def main():
    parser = argparse.ArgumentParser(
        description="Build the UnrealEditor module dependency graph from DLL import tables and assign dependency layers."
    )
    parser.add_argument("--engine", required=True, type=Path, help="Engine folder, e.g. D:/EpicGames/UE_5.5/Engine")
    parser.add_argument("--out", required=True, type=Path, help="Output CSV path")
    parser.add_argument("--delay-loads", action="store_true", help="Count delay-load imports as dependencies")
    args = parser.parse_args()

    binaries = args.engine / "Binaries" / "Win64"
    dlls = sorted(binaries.glob(PREFIX + "*.dll"))
    with ThreadPoolExecutor() as pool:
        imports = dict(zip(dlls, pool.map(read_imports, dlls)))

    modules = {module_name(d.name): d for d in dlls}
    graph, delayed_of = {}, {}
    for dll, (direct, delayed) in imports.items():
        name = module_name(dll.name)
        edges = direct | delayed if args.delay_loads else direct
        graph[name] = {d for d in edges if d in modules and d != name}
        delayed_of[name] = delayed & modules.keys()

    layer_of, components = layers(graph)
    cycle_of = {m: "+".join(c) for c in components if len(c) > 1 for m in c}
    dependents = {m: 0 for m in graph}
    for deps in graph.values():
        for d in deps:
            dependents[d] += 1
    areas = source_areas(args.engine / "Source")

    rows = sorted(graph, key=lambda m: (layer_of[m], -dependents[m], m))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["layer", "module", "area", "bytes", "dependencies", "dependents", "delay_loads", "cycle", "imports"])
        for m in rows:
            writer.writerow([
                layer_of[m], m, areas.get(m, "unknown"), modules[m].stat().st_size,
                len(graph[m]), dependents[m], len(delayed_of[m]), cycle_of.get(m, ""),
                " ".join(sorted(graph[m])),
            ])

    print(f"modules={len(graph)} layers={max(layer_of.values()) + 1} cycles={sum(len(c) > 1 for c in components)} out={args.out}")


if __name__ == "__main__":
    sys.exit(main())
