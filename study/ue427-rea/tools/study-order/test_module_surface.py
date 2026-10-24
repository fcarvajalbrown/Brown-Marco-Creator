import json
import tempfile
from pathlib import Path

from module_surface import render


def test_render():
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        names = ["UE4EDITOR-CORE.DLL::FString::FString", "FFoo::Bar", "FFoo::Baz", "FFoo::Baz", "NBar::FIn::Qux", "KERNEL32.DLL::Sleep"]
        (folder / "Foo.search.json").write_text(json.dumps({"normalized_result": [{"value": n} for n in names]}), encoding="utf-8")
        text, done = render(["Core", "Foo"], folder)
        assert done == 1
        assert "| 2 | Foo | 3 | 2 | FFoo 2, NBar::FIn 1 |" in text
        assert "Not yet searched: 1 modules." in text


if __name__ == "__main__":
    test_render()
    print("ok")
