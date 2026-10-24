# Handoff: Brown Marco Creator on the laptop

The former `ue55-rea` repo now lives here under `study/ue427-rea/`, with its full history.

## Set up once
1. `git pull` on `main`.
2. `gh auth status` must show you logged in, then `python tools/fetch_artifacts/fetch.py`. It merges the git-ignored study data into `study/ue427-rea/snapshots/`: imports for all 398 core modules and the name survey for the first 121.
3. Tools, same versions as the desktop: UE 4.27.2 at `C:\Program Files\Epic Games\UE_4.27`, Ghidra 12.1.4 at `C:\tools\ghidra_12.1.4_PUBLIC`, Temurin JDK 21.0.12.1+1 at `C:\tools\jdk-21.0.12.1+1`, REA 6.7.0 installed with `corepack pnpm` into `C:\tools\rea-agents-pnpm` (npx is blocked on purpose). Keep `GHIDRA_HEADLESS_MAXMEM=4G`, never higher.

## Where it stands
- Planning: PRD, ROADMAP and Proposed ADRs 0006 to 0010 plus SDL3 (C++ with Dear ImGui, Vulkan, Jolt, CMake, cache plus sidecar files, Apache-2.0). No engine code yet.
- Study (`study/ue427-rea/ROADMAP.md`): phase 1 imports done for the 398 core modules, 0 failed; plugin modules deferred by Felipe (essentials only). Phase 4 study order done (18 layers, `study/ue427-rea/notes/study-order.md`). Phase 5 step 1 name survey at 121 of 398, 0 failed.

## Next steps, in order
1. Resume the name survey: rerun the phase 5 step 1 line in `study/ue427-rea/ROADMAP.md` (it continues at module 122), then step 2 to refresh `study/ue427-rea/notes/module-surface.md`.
2. Phase 5 step 3: functions, xrefs and traces per module, in study order.
3. Main ROADMAP phase B (editor shell on SDL3 and Dear ImGui) once the ADRs are accepted.

## Open for Felipe
Accept or change the Proposed ADRs. Whether the modeling-tools plugin (`UE4Editor-MeshModelingTools.dll`, the source of auto UV) counts as an essential despite the plugin deferral.

## Read first
`CLAUDE.md`, `ROADMAP.md`, `study/ue427-rea/ROADMAP.md`, `study/ue427-rea/notes/session-notes.md`.
