# UE 5.5 study with REA: roadmap

Goal: learn how UE 5.5 works from the installed DLLs under `D:\EpicGames\UE_5.5\Engine\Binaries\Win64`, every fact through REA, then find legacy bloat. Findings: `notes/findings.md`. Finished items: `docs/ROADMAP-HISTORY.md`.

Commands run from `C:\Projects\ue55-rea` at the `!` prompt (Git Bash), one line per action. Outputs go to `snapshots/` (git-ignored).

## Open items

| # | Item | Status |
|---|---|---|
| 1 | Get each module DLL's imports through `rea search` | In Progress |
| 2 | Get imports through `rea inspect-with-objdump` | Not Started |
| 3 | Get imports through MCP, one DLL at a time | Not Started |
| 4 | Build the dependency-first study order from the imports | Not Started |
| 5 | Study modules in that order with REA | Not Started |

Phases 1 to 3 are tried in order; a later phase runs only if the earlier one fails.

## Phase 1: `rea search` (In Progress)

The TraceLog test passed (see history). Imported data labels are missed; only imported functions count.

1. Run REA on every module DLL (resumable; rerun the same line after an interruption):
   `! python -I tools/rea-imports/rea_imports.py --binaries 'D:/EpicGames/UE_5.5/Engine/Binaries/Win64' --out snapshots/imports`
2. Claude reads the `finished:` line and any `<Module>.error.txt` in `snapshots/imports`, and records the result in `notes/findings.md`.
3. Retry only the failed modules:
   `! python -I tools/rea-imports/rea_imports.py --binaries 'D:/EpicGames/UE_5.5/Engine/Binaries/Win64' --out snapshots/imports --only <Module> <Module>`
4. If the batch cannot complete: record why and go to Phase 2.

## Phase 2: `rea inspect-with-objdump` (Not Started)

REA wraps GNU objdump but does not install it. The documented operations are `file_headers`, `section_headers`, `symbols`, `relocations`, `dwarf`, `disassemble`; none is documented as the PE import table, so this is a test.

1. Install GNU binutils (open source, WinLibs):
   `! winget install --id BrechtSanders.WinLibs.POSIX.UCRT -e`
2. Restart the terminal so `objdump` is on `PATH`, then check it:
   `! objdump --version`
3. Try the file headers on TraceLog:
   `! npx -y rea-agents@6.7.0 inspect-with-objdump 'D:\EpicGames\UE_5.5\Engine\Binaries\Win64\UnrealEditor-TraceLog.dll' file_headers --json > snapshots/TraceLog.objdump-headers.json`
4. Try the symbols on TraceLog:
   `! npx -y rea-agents@6.7.0 inspect-with-objdump 'D:\EpicGames\UE_5.5\Engine\Binaries\Win64\UnrealEditor-TraceLog.dll' symbols --json > snapshots/TraceLog.objdump-symbols.json`
5. Claude reads both files; pass if either names the imported DLLs. Then a batch as in Phase 1 step 3; otherwise record and go to Phase 3.

## Phase 3: MCP, one DLL at a time (Not Started)

The route verified on Core. Claude runs these REA calls in the conversation; your action is to say "next" or name a DLL.

1. `open_binary` with the DLL path and `provider_id: ghidra`.
2. `list_names`; when the reply exceeds 10 MB, `export_evidence_bundle` to `snapshots/<Module>.evidence.json`.
3. Claude tallies the external names per library and records them in `notes/findings.md`.
4. `close_binary`.

## Phase 4: study order (Not Started)

Layer the modules bottom-up from the REA import data; within a layer, most-depended-on first. The order is written here only after the data exists.

## Phase 5: study (Not Started)

Per module, in order: `search_procedures`, `analyze_function`, `procedure_pseudo_code`, `get_call_graph`, `xrefs` on named exports; findings to `notes/findings.md`.
