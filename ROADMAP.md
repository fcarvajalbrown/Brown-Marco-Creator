# Brown Marco Creator roadmap

Phases are ordered dependency first.

- Phase detail and exit checks: [docs/PRD.md](docs/PRD.md#phases)
- Finished items: [docs/ROADMAP-HISTORY.md](docs/ROADMAP-HISTORY.md)

## Open items

- ADRs 0001 to 0005 drafted from Felipe's answers — Proposed, awaiting Felipe's acceptance — [docs/adr](docs/adr/README.md)
- Licence for the public repo — Blocked on Felipe
- Graphics API ADR — Blocked on Felipe — phase D
- Physics library ADR — Blocked on Felipe — phase I
- Build system ADR — Blocked on Felipe — phase B
- Derived data and import settings storage ADR — Blocked on Felipe — [ADR 0003](docs/adr/0003-source-assets-no-container.md)
- UE 4.27 module import graph — In Progress in `ue55-rea` (Phase 1 batch) — phase A

## Phases

| Phase | Status | Shaped by |
|---|---|---|
| A. Study UE 4.27 with REA | In Progress (in `ue55-rea`) | ADR [0001](docs/adr/0001-own-engine-ue427-study-only.md), [0002](docs/adr/0002-scope-and-platforms.md) |
| B. Workspace and editor shell | Blocked on build system ADR | ADR [0004](docs/adr/0004-cpp-and-dear-imgui.md) |
| C. Core and source-asset registry | Not Started | ADR [0003](docs/adr/0003-source-assets-no-container.md) |
| D. Renderer | Blocked on graphics API ADR | ADR [0002](docs/adr/0002-scope-and-platforms.md) |
| E. Editor panels | Not Started | ADR [0003](docs/adr/0003-source-assets-no-container.md), [0005](docs/adr/0005-single-editor-mode.md) |
| F. Gameplay framework, input, Play In Editor | Not Started | |
| G. Visual scripting | Not Started | ADR [0001](docs/adr/0001-own-engine-ue427-study-only.md) |
| H. Material editor | Not Started | |
| I. Physics, animation, AI | Blocked on physics library ADR | |
| J. Audio, UI, cinematics, particles | Not Started | |
| K. Lighting and world scale | Not Started | |
| L. Modeling tools | Not Started | ADR [0005](docs/adr/0005-single-editor-mode.md) |
| M. Packaging and cooking | Not Started; consoles need Felipe's developer programme access | ADR [0002](docs/adr/0002-scope-and-platforms.md) |
