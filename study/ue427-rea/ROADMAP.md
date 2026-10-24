# Unreal Engine study with REA: roadmap

Goal: learn how Unreal Engine works from its installed DLLs, every fact through REA, then find legacy bloat. The study feeds Brown Marco Creator (`fcarvajalbrown/Brown-Marco-Creator`, phase A), Felipe's own engine with the 4.27 workflow. Findings: `notes/findings.md`. Finished items: `docs/ROADMAP-HISTORY.md`.

Engine version: the project switched from UE 5.5 to **UE 4.27.2**, installed at `C:\Program Files\Epic Games\UE_4.27` (module DLLs in `Engine\Binaries\Win64`, named `UE4Editor-*.dll`). The repo keeps its name `ue55-rea`. UE 5.5 results recorded before the switch stay in `notes/findings.md` for reference.

Commands run from `C:\Projects\Brown-Marco-Creator\study\ue427-rea` at the `!` prompt (Git Bash), one line per action. Outputs go to `snapshots/` (git-ignored).

## Open items

| # | Item | Status |
|---|---|---|
| 1 | Get each module DLL's imports through `rea search` | Done: 398 core modules, 0 failed (plugin modules deferred by Felipe: essentials only) |
| 2 | Get imports through `rea inspect-with-objdump` | Not Started |
| 3 | Get imports through MCP, one DLL at a time | Not Started |
| 4 | Build the dependency-first study order from the imports | Done: 398 modules in 18 layers, [notes/study-order.md](notes/study-order.md) |
| 5 | Study modules in that order with REA | In Progress |

Phases 1 to 3 are tried in order; a later phase runs only if the earlier one fails.

## Phase 1: `rea search` (In Progress)

The TraceLog test passed on UE 5.5 (see history). Imported data labels are missed; only imported functions count. Ghidra heap is `GHIDRA_HEADLESS_MAXMEM=4G`, never higher.

1. Run REA on every module DLL (resumable; rerun the same line after an interruption):
   `! GHIDRA_HEADLESS_MAXMEM=4G python -I tools/rea-imports/rea_imports.py --binaries 'C:/Program Files/Epic Games/UE_4.27/Engine/Binaries/Win64' --prefix UE4Editor- --out snapshots/imports-ue4.27`
2. Claude reads the `finished:` line and any `<Module>.error.txt` in `snapshots/imports-ue4.27`, and records the result in `notes/findings.md`.
3. Retry only the failed modules:
   `! GHIDRA_HEADLESS_MAXMEM=4G python -I tools/rea-imports/rea_imports.py --binaries 'C:/Program Files/Epic Games/UE_4.27/Engine/Binaries/Win64' --prefix UE4Editor- --out snapshots/imports-ue4.27 --only <Module> <Module>`
4. If the batch cannot complete: record why and go to Phase 2.
5. Deferred by Felipe (essentials only): the 654 plugin modules, same heap, if a later study needs them:
   `! GHIDRA_HEADLESS_MAXMEM=4G python -I tools/rea-imports/rea_imports.py --binaries 'C:/Program Files/Epic Games/UE_4.27/Engine/Plugins' --recursive --prefix UE4Editor- --out snapshots/imports-ue4.27-plugins`

## Phase 2: `rea inspect-with-objdump` (Not Started)

Felipe approved installing WinLibs binutils (step 1) only if the Phase 1 batch fails outright, and only if C: has 20 GB or more free right before the install; otherwise Phase 2 is recorded blocked. REA wraps GNU objdump but does not install it. The documented operations are `file_headers`, `section_headers`, `symbols`, `relocations`, `dwarf`, `disassemble`; none is documented as the PE import table, so this is a test.

1. Install GNU binutils (open source, WinLibs):
   `! winget install --id BrechtSanders.WinLibs.POSIX.UCRT -e`
2. Restart the terminal so `objdump` is on `PATH`, then check it:
   `! objdump --version`
3. Try the file headers on TraceLog:
   `! npx -y rea-agents@6.7.0 inspect-with-objdump 'C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-TraceLog.dll' file_headers --json > snapshots/TraceLog.objdump-headers.json`
4. Try the symbols on TraceLog:
   `! npx -y rea-agents@6.7.0 inspect-with-objdump 'C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor-TraceLog.dll' symbols --json > snapshots/TraceLog.objdump-symbols.json`
5. Claude reads both files; pass if either names the imported DLLs. Then a batch as in Phase 1 step 3; otherwise record and go to Phase 3.

## Phase 3: MCP, one DLL at a time (Not Started)

The route verified on Core. Claude runs these REA calls in the conversation; your action is to say "next" or name a DLL.

1. `open_binary` with the DLL path and `provider_id: ghidra`.
2. `list_names`; when the reply exceeds 10 MB, `export_evidence_bundle` to `snapshots/<Module>.evidence.json`.
3. Claude tallies the external names per library and records them in `notes/findings.md`.
4. `close_binary`.

## Phase 4: study order (Done)

Layer the modules bottom-up from the REA import data; within a layer, most-depended-on first. Modules that import each other form one group on one layer. Rebuild (seconds; rerun the same line to redo):
`! python -I tools/study-order/study_order.py --imports snapshots/imports-ue4.27 --out notes/study-order.md`
Check: `! cd tools/study-order && python test_study_order.py`

## Phase 5: study (In Progress)

Per module, in order: `search_procedures`, `analyze_function`, `procedure_pseudo_code`, `get_call_graph`, `xrefs` on named exports; findings to `notes/findings.md`.
