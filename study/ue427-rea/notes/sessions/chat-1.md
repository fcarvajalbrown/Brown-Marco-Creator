# Overnight desktop run, UE 4.27 Phase 1

Done:
- Phase 1 core batch on UE 4.27.2 `Engine\Binaries\Win64`: 398 ok, 0 failed (`snapshots/imports-ue4.27`), paused once for the Cuna DiariZen run and resumed.
- `rea_imports.py`: `--prefix` check added, `--recursive` option for plugin modules, both covered by `test_rea_imports.py`.
- Found 654 plugin module DLLs outside the batch folder; Phase 1 step 5 added for them.
- Brown Marco Creator created (`fcarvajalbrown/Brown-Marco-Creator`, public): PRD, ROADMAP, ADRs 0001 to 0011 (Proposed), README, Apache-2.0 licence, 24 UE 4.27 feature notes. Profile README entry replaced SKPFORGE.

Flags opened:
- Plugin module batch not started (Phase 1 step 5).
- Brown Marco Creator phase B blocked on Vulkan SDK setup; ADRs await Felipe's acceptance.
- Old worktree `worktree-ue55-phase1-blocked` is merged into master and still on disk.

Flags closed:
- Phase 1 blocked on missing prerequisites (Ghidra, JDK, UE install now present).
