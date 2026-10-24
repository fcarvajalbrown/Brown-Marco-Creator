# Unattended desktop run, study phases 4 and 5

Done:
- Phase 4: `tools/study-order/study_order.py` builds the dependency-first order from the 398 core import searches; `notes/study-order.md` has 398 modules in 18 layers. Check: `test_study_order.py`.
- Findings: every Unreal DLL a core module imports is a core module; Core is imported directly by 394 of 397 modules; two import cycles, one of 69 modules caused by the editor build of Engine importing AudioMixer, GameplayTags, Kismet, Landscape, UMG and UnrealEd.
- Phase 5 prepared: `rea_imports.py` takes `--order` (study-order.md) and `--pattern`; `tools/study-order/module_surface.py` turns the name searches into a per-module table. Both checked offline.
- Main ROADMAP lists the study order (Done) and the core module study (Blocked).

Flags opened:
- Phase 5 blocked on Felipe: every `npx -y rea-agents@6.7.0` call was denied by this session's permissions, so no REA query ran and the REA side of the name survey is untested.

Flags closed:
- Old ue55-rea worktree flag: the ue55-rea repo was merged here and is being deleted.
