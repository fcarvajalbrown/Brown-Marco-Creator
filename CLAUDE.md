# Brown Marco Creator

Felipe's own game engine and editor with UE 4.27's workflow, written from scratch in C++ with Dear ImGui. UE 4.27 is study material only; no Epic code comes in. The REA study of the 4.27 DLLs lives in `C:\Projects\ue55-rea` (`fcarvajalbrown/ue55-rea`).

## Session start

Read `ROADMAP.md` first. Then, as the task needs: `docs/PRD.md` (vision, scope, phases), `docs/adr/` (decisions), `docs/research/` (findings).

## Rules

- Public repo. Every claim about Epic or Unreal Engine in the README or docs is a verified fact with a link, kept in `docs/research/`.
- Every behaviour taken from UE 4.27 is tagged as found by REA, observed in the 4.27 editor, read in Epic's docs, or read from the 4.27 install's files.
- ADRs stay Proposed until Felipe accepts them.
- Imported assets are never converted into a proprietary container ([ADR 0003](docs/adr/0003-source-assets-no-container.md)).
- Controller first: every editor and game flow is checked on an Xbox controller.
