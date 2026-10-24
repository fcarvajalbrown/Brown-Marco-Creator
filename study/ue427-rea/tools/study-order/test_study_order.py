from study_order import study_order


def test_study_order():
    graph = {
        "Core": [],
        "TraceLog": [],
        "CoreUObject": ["Core"],
        "Engine": ["Core", "CoreUObject", "Slate"],
        "Slate": ["Core", "SlateCore"],
        "SlateCore": ["Core", "Slate"],
        "Editor": ["Engine", "TraceLog"],
    }
    rows, cycles = study_order(graph)
    assert [(m, layer) for m, layer, _, _ in rows] == [
        ("Core", 0), ("TraceLog", 0), ("Slate", 1), ("CoreUObject", 1), ("SlateCore", 1), ("Engine", 2), ("Editor", 3),
    ]
    assert cycles == [["Slate", "SlateCore"]]
    assert dict((m, n) for m, _, n, _ in rows)["Core"] == 4


if __name__ == "__main__":
    test_study_order()
    print("ok")
