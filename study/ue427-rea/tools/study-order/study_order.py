import argparse
import json
import sys
from pathlib import Path

SUFFIX = ".search.json"


def read_imports(folder, prefix):
    modules = {}
    for path in sorted(folder.glob("*" + SUFFIX)):
        data = json.loads(path.read_text(encoding="utf-8"))
        libraries = {item["value"].split("::", 1)[0].upper() for item in data["normalized_result"]}
        modules[path.name[: -len(SUFFIX)]] = libraries
    by_library = {(prefix + m + ".DLL").upper(): m for m in modules}
    graph = {m: sorted({by_library[lib] for lib in libs if lib in by_library} - {m}) for m, libs in modules.items()}
    unresolved = {m: sorted(lib for lib in libs if lib.startswith(prefix.upper()) and lib not in by_library) for m, libs in modules.items()}
    return graph, {m: libs for m, libs in unresolved.items() if libs}


def strongly_connected(graph):
    index, low, stack, on_stack, components = {}, {}, [], set(), []

    def visit(root):
        work = [(root, iter(graph[root]))]
        index[root] = low[root] = len(index)
        stack.append(root)
        on_stack.add(root)
        while work:
            node, children = work[-1]
            child = next(children, None)
            if child is None:
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
            elif child not in index:
                index[child] = low[child] = len(index)
                stack.append(child)
                on_stack.add(child)
                work.append((child, iter(graph[child])))
            elif child in on_stack:
                low[node] = min(low[node], index[child])

    for node in sorted(graph):
        if node not in index:
            visit(node)
    return components


def study_order(graph):
    components = strongly_connected(graph)
    component_of = {m: i for i, c in enumerate(components) for m in c}
    layer = {}
    for i, component in enumerate(components):
        below = [layer[component_of[d]] for m in component for d in graph[m] if component_of[d] != i]
        layer[i] = 1 + max(below) if below else 0
    dependents = {m: 0 for m in graph}
    for deps in graph.values():
        for d in deps:
            dependents[d] += 1
    order = sorted(graph, key=lambda m: (layer[component_of[m]], -dependents[m], m))
    cycles = [c for c in components if len(c) > 1]
    return [(m, layer[component_of[m]], dependents[m], graph[m]) for m in order], cycles


def render(rows, cycles, unresolved):
    lines = [
        "# UE 4.27 core module study order",
        "",
        "Built by `tools/study-order/study_order.py` from the REA import data in `snapshots/imports-ue4.27` (398 core modules). Layer 0 imports no other Unreal module; each module sits one layer above its highest dependency. Within a layer, the module with the most direct dependents comes first, then by name. Imported data labels are not in the REA data, so a module imported only for data is missing as a dependency.",
        "",
        f"Cycles (modules studied as one group): {'; '.join(', '.join(c) for c in cycles) if cycles else 'none'}.",
        "",
        "Unreal imports with no matching core module: "
        + ("; ".join(f"{m}: {', '.join(libs)}" for m, libs in sorted(unresolved.items())) if unresolved else "none")
        + ".",
        "",
        "| # | Layer | Module | Direct dependents | Imports from |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| {i} | {layer} | {m} | {count} | {', '.join(deps)} |" for i, (m, layer, count, deps) in enumerate(rows, 1)]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Build the dependency-first module study order from REA import searches.")
    parser.add_argument("--imports", required=True, type=Path, help="Folder of <Module>.search.json files")
    parser.add_argument("--out", required=True, type=Path, help="Markdown file to write")
    parser.add_argument("--prefix", default="UE4Editor-", help="Module DLL name prefix")
    args = parser.parse_args()
    graph, unresolved = read_imports(args.imports, args.prefix)
    if not graph:
        sys.exit(f"no {SUFFIX} files in {args.imports}")
    rows, cycles = study_order(graph)
    args.out.write_text(render(rows, cycles, unresolved), encoding="utf-8")
    print(f"{len(rows)} modules, {1 + max(r[1] for r in rows)} layers, {len(cycles)} cycles, {len(unresolved)} with unresolved imports -> {args.out}")


if __name__ == "__main__":
    main()
