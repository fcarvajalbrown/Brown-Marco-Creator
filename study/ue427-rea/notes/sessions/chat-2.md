# Unattended desktop run, study phases 4 and 5

Done:
- Phase 4: `tools/study-order/study_order.py` builds the dependency-first order from the 398 core import searches; `notes/study-order.md` has 398 modules in 18 layers. Check: `test_study_order.py`.
- Findings: every Unreal DLL a core module imports is a core module; Core is imported directly by 394 of 397 modules; two import cycles, one of 69 modules caused by the editor build of Engine importing AudioMixer, GameplayTags, Kismet, Landscape, UMG and UnrealEd.
- Phase 5 prepared: `rea_imports.py` takes `--order` (study-order.md) and `--pattern`; `tools/study-order/module_surface.py` turns the name searches into a per-module table. Both checked offline.
- Main ROADMAP lists the study order (Done) and the core module study (Blocked).

- On the master session's instruction, `rea_imports.py` now runs REA from the pnpm install with node (`--rea` to override). The name survey ran 121 of 398 modules, 0 failed, and stopped at 14:00; `notes/module-surface.md` and findings record it.

Flags opened:
- Phase 5 step 1 survey to resume from module 122; step 3 not started.

Flags closed:
- Old ue55-rea worktree flag: the ue55-rea repo was merged here and is being deleted.
