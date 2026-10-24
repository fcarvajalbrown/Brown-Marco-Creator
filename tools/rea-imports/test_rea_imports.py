import tempfile
from pathlib import Path

from rea_imports import select_dlls


def test_select_dlls():
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        for name in ["UE4Editor-Core.dll", "UE4Editor-Engine.dll", "UnrealEditor-Core.dll", "UE4Editor.exe"]:
            (folder / name).touch()
        assert [d.name for d in select_dlls(folder, "UE4Editor-", [])] == ["UE4Editor-Core.dll", "UE4Editor-Engine.dll"]
        assert [d.name for d in select_dlls(folder, "UnrealEditor-", [])] == ["UnrealEditor-Core.dll"]
        assert [d.name for d in select_dlls(folder, "UE4Editor-", ["Engine"])] == ["UE4Editor-Engine.dll"]


if __name__ == "__main__":
    test_select_dlls()
    print("ok")
