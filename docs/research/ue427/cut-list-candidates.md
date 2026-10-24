# Cut-list candidates

Parts of UE 4.27 the feature notes flagged as possible cuts. Nothing here is cut until Felipe decides, after the study is complete (study first, then cut).

| Candidate | Why it is flagged | Note |
|---|---|---|
| Brush Editing (BSP) mode | Not on the kept list in ADR 0002 | [editor-modes.md](editor-modes.md) |
| Fracture mode | Not on the kept list in ADR 0002 | [editor-modes.md](editor-modes.md) |
| Separate mode tabs | Replaced by one mode, ADR 0005 | [editor-modes.md](editor-modes.md) |
| Separate Hierarchical LOD Outliner | Could fold into the World Outliner | [hlod.md](hlod.md) |
| World Composition grid | Plain level streaming may cover the need | [level-streaming.md](level-streaming.md) |
| Cascade | Niagara's model is kept; two particle systems overlap | [niagara.md](niagara.md) |
| Clothing and vehicles | Not on the kept list | [physics.md](physics.md) |
| Movie Render Queue | Offline rendering, not game shipping | [sequencer.md](sequencer.md) |
| Sound Cues and Sound Classes | Studio rule uses parameterised sources, Submixes and modulation buses instead | [audio.md](audio.md) |
| Layered materials and Material Layers | Instances, functions and parameter collections may cover the need | [materials.md](materials.md) |
| Unreal Swarm distributed lighting builds | A single-machine GPU baker fits the target | [lightmass.md](lightmass.md) |
| Mobile and iOS paths | Already out by ADR 0002 | |

