import tempfile
from pathlib import Path

from rea_imports import read_order, select_dlls


def test_select_dlls():
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        for name in ["UE4Editor-Core.dll", "UE4Editor-Engine.dll", "UnrealEditor-Core.dll", "UE4Editor.exe"]:
            (folder / name).touch()
        assert [d.name for d in select_dlls(folder, "UE4Editor-", [])] == ["UE4Editor-Core.dll", "UE4Editor-Engine.dll"]
        assert [d.name for d in select_dlls(folder, "UnrealEditor-", [])] == ["UnrealEditor-Core.dll"]
        assert [d.name for d in select_dlls(folder, "UE4Editor-", ["Engine"])] == ["UE4Editor-Engine.dll"]
        nested = folder / "Plugins" / "Foo" / "Binaries" / "Win64"
        nested.mkdir(parents=True)
        (nested / "UE4Editor-Foo.dll").touch()
        assert [d.name for d in select_dlls(folder, "UE4Editor-", [])] == ["UE4Editor-Core.dll", "UE4Editor-Engine.dll"]
        assert [d.name for d in select_dlls(folder, "UE4Editor-", [], recursive=True)] == ["UE4Editor-Core.dll", "UE4Editor-Engine.dll", "UE4Editor-Foo.dll"]
        assert [d.name for d in select_dlls(folder, "UE4Editor-", ["Engine", "Core"])] == ["UE4Editor-Engine.dll", "UE4Editor-Core.dll"]
        order = folder / "study-order.md"
        order.write_text(
            "# Order\n\n| # | Layer | Module | Direct dependents | Imports from |\n|---|---|---|---|---|\n"
            "| 1 | 1 | Core | 1 |  |\n| 2 | 2 | Engine | 0 | Core |\n",
            encoding="utf-8",
        )
        assert read_order(order) == ["Core", "Engine"]


if __name__ == "__main__":
    test_select_dlls()
    print("ok")
