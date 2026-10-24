import argparse
import json
from collections import Counter
from pathlib import Path

SUFFIX = ".search.json"
TOP = 8


def read_order(path):
    return [cells[3].strip() for cells in (line.split("|") for line in path.read_text(encoding="utf-8").splitlines()) if len(cells) > 4 and cells[1].strip().isdigit()]


def own_names(data):
    names = {item["value"] for item in data["normalized_result"]}
    return sorted(n for n in names if not n.split("::", 1)[0].upper().endswith(".DLL"))


def surface(names):
    classes = Counter(n.split("::", 1)[0] for n in names)
    return len(names), len(classes), classes.most_common(TOP)


def render(order, folder):
    lines = [
        "# UE 4.27 core module surface",
        "",
        "Built by `tools/study-order/module_surface.py` from REA procedure-name searches for `::` (`snapshots/names-ue4.27`), in study order. Imported names are left out, so each row is the module's own named procedures; a name without `::` (a free function outside any class or namespace) is not counted. Top scopes are the class or namespace before the first `::`, with their procedure count.",
        "",
        "| # | Module | Named procedures | Scopes | Top scopes |",
        "|---|---|---|---|---|",
    ]
    missing = []
    for index, module in enumerate(order, 1):
        path = folder / f"{module}{SUFFIX}"
        if not path.exists():
            missing.append(module)
            continue
        count, scopes, top = surface(own_names(json.loads(path.read_text(encoding="utf-8"))))
        lines.append(f"| {index} | {module} | {count} | {scopes} | {', '.join(f'{s} {n}' for s, n in top)} |")
    lines += ["", f"Not yet searched: {len(missing)} modules."]
    return "\n".join(lines) + "\n", len(order) - len(missing)


def main():
    parser = argparse.ArgumentParser(description="Summarize each module's own named procedures from REA name searches, in study order.")
    parser.add_argument("--order", required=True, type=Path, help="study-order.md")
    parser.add_argument("--names", required=True, type=Path, help="Folder of <Module>.search.json name searches")
    parser.add_argument("--out", required=True, type=Path, help="Markdown file to write")
    args = parser.parse_args()
    text, done = render(read_order(args.order), args.names)
    args.out.write_text(text, encoding="utf-8")
    print(f"{done} modules summarized -> {args.out}")


if __name__ == "__main__":
    main()
