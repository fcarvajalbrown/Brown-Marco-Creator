# Brown Marco Creator roadmap

Phases are ordered dependency first.

- Phase detail and exit checks: [docs/PRD.md](docs/PRD.md#phases)
- Finished items: [docs/ROADMAP-HISTORY.md](docs/ROADMAP-HISTORY.md)

## Open items

- ADRs 0001 to 0011 drafted from Felipe's answers — Proposed, awaiting Felipe's acceptance — [docs/adr](docs/adr/README.md)
- Vulkan SDK (or fetched Vulkan-Headers plus a loader such as volk) for the phase B build — Blocked on Felipe: not installed on the desktop, setup not approved; CMake 4 and Visual Studio are present — phase B
- UE 4.27 feature notes from Epic's docs — Done for every kept feature (24 notes); 4.27 Modeling Tools behaviour still needs REA or the editor — [docs/research/ue427](docs/research/ue427/README.md) — phase A
- UE 4.27 cut list — candidates drafted, Blocked on Felipe's review — [cut-list-candidates.md](docs/research/ue427/cut-list-candidates.md) — phase A
- UE 4.27 module import graph — Done for the 398 core modules, 0 failed; plugin modules deferred (essentials only) — [study/ue427-rea](study/ue427-rea/ROADMAP.md) — phase A
- UE 4.27 dependency-first study order — Done: 398 core modules, 18 layers — [study-order.md](study/ue427-rea/notes/study-order.md) — phase A
- UE 4.27 core module study with REA, in that order — Blocked on Felipe: REA runs are denied in unattended sessions; the first step is one `!` line in the study roadmap — [study phase 5](study/ue427-rea/ROADMAP.md#phase-5-study-blocked-on-felipe) — phase A

## Phases

| Phase | Status | Shaped by |
|---|---|---|
| A. Study UE 4.27 with REA | In Progress (in `study/ue427-rea`) | ADR [0001](docs/adr/0001-own-engine-ue427-study-only.md), [0002](docs/adr/0002-scope-and-platforms.md) |
| B. Workspace and editor shell | Blocked on Vulkan SDK setup | ADR [0004](docs/adr/0004-cpp-and-dear-imgui.md), [0009](docs/adr/0009-cmake.md), [0011](docs/adr/0011-sdl3.md) |
| C. Core and source-asset registry | Not Started | ADR [0003](docs/adr/0003-source-assets-no-container.md), [0010](docs/adr/0010-asset-cache-and-sidecars.md) |
| D. Renderer | Not Started | ADR [0002](docs/adr/0002-scope-and-platforms.md), [0007](docs/adr/0007-vulkan-first.md) |
| E. Editor panels | Not Started | ADR [0003](docs/adr/0003-source-assets-no-container.md), [0005](docs/adr/0005-single-editor-mode.md) |
| F. Gameplay framework, input, Play In Editor | Not Started | |
| G. Visual scripting | Not Started | ADR [0001](docs/adr/0001-own-engine-ue427-study-only.md) |
| H. Material editor | Not Started | |
| I. Physics, animation, AI | Not Started | ADR [0008](docs/adr/0008-jolt-physics.md) |
| J. Audio, UI, cinematics, particles | Not Started | |
| K. Lighting and world scale | Not Started | |
| L. Modeling tools | Not Started | ADR [0005](docs/adr/0005-single-editor-mode.md) |
| M. Packaging and cooking | Not Started; consoles need Felipe's developer programme access | ADR [0002](docs/adr/0002-scope-and-platforms.md) |
