# UE 5.5 study with REA: findings

## Goal

Learn how Unreal Engine 5.5 works from the installed engine at `D:\EpicGames\UE_5.5`, then use that knowledge to optimize it by removing legacy bloat. A clean-room open-source rebuild was discussed and parked; only its timeline was estimated.

## REA scoping

- REA is registered at Claude Code local scope for `C:\Projects\ue55-rea` only. The entry lives in `~/.claude.json` under this folder's path; no other project loads it.
- Local scope installs no REA skill; `rea doctor` and `rea update` do not see this entry; it stays on `rea-agents@6.7.0`.
- Remove with `claude mcp remove --scope local rea` from this folder.
- Clean-room separation is not provided by any scope choice; REA's docs say it needs a separate OS account or container (`docs/installation.md` in the REA repo, "Limit REA to one project or agent profile").

## Engine size on disk

Measured with `find` and `wc` over `D:\EpicGames\UE_5.5\Engine`.

| Area | Modules | Headers | .cpp/.c | Shader files | Lines |
|---|---|---|---|---|---|
| Source/Runtime | 257 | 9,770 | 80 | 0 | 2,022,422 |
| Source/Editor | 133 | 3,855 | 0 | 0 | 425,385 |
| Source/Developer | 156 | 1,678 | 5 | 0 | 231,307 |
| Source/Programs | 2 | 116 | 0 | 0 | 21,996 |
| Source/ThirdParty | 121 | 27,149 | 0 | 0 | 7,109,012 |
| Plugins | 1,216 | 38,950 | 563 | 412 | 5,535,469 |
| Shaders | 1 | 35 | 0 | 1,016 | 325,383 |

- Epic-authored total, excluding ThirdParty: 1,765 modules, about 8.6M lines.
- The launcher install ships headers only. Implementation lives in 1,107 DLLs under `Engine\Binaries\Win64`, with 540 PDBs beside them.
- Full implementation source requires Epic's GitHub repository (Epic account linked to GitHub).

## REA readiness on this machine

- Native analysis needs Ghidra 12.1.x (verified with 12.1.4) and a 64-bit full JDK 21 or newer. Found: no Ghidra, no IDA, Java 1.8 only. Hopper does not run on Windows.
- Windows Ghidra support is "P0": read-only, no annotation or renaming.
- REA imports a private copy of each binary and does not accept a caller-selected PDB (`docs/ghidra-provider.md`). The sibling PDBs may therefore go unused; the PDB load state reported for the first DLL will confirm.
- REA reads binaries only. Removing bloat requires rebuilding from Epic's full source.
- Default Ghidra heap is 2G; raise `GHIDRA_HEADLESS_MAXMEM` for large DLLs.

## Installed providers

- Ghidra 12.1.4 at `C:\tools\ghidra_12.1.4_PUBLIC`, zip SHA-256 matched the GitHub release digest; `win_x86_64` decompiler present. Ghidra 12.2 was skipped because REA accepts 12.1.x only.
- Temurin JDK 21.0.12.1+1 at `C:\tools\jdk-21.0.12.1+1`, zip SHA-256 matched the Adoptium API; `java -version` reports 21.0.12.1 LTS.
- Download zips deleted after extraction.
- `rea-agents@6.7.0 doctor --provider ghidra --json`, run from this folder: `"healthy": true`; all ten Ghidra checks pass, including native decompiler and Windows native authority (local NTFS only). Global client registrations report `missing`, which is expected: REA is meant to be registered at local scope only.
- Run REA commands from this folder, never from the REA source checkout: there, `npx rea-agents@6.7.0` resolves to the checkout's own package and fails with "'rea' is not recognized".
- From the `!` prompt (Git Bash), `cmd /c` is rewritten to a drive path; use Bash env-prefix syntax or `cmd.exe //d //c`.

- Registered: `claude mcp add --scope local rea` with `GHIDRA_INSTALL_DIR` and `JAVA_HOME` env, stored in `~/.claude.json` under project `C:\Projects\ue55-rea`; `claude mcp list` from this folder reports `rea` connected.

## Readiness checks

1. `npx -y rea-agents@6.7.0 doctor --provider ghidra --json` with `GHIDRA_INSTALL_DIR` and `JAVA_HOME` set: expect `"healthy": true`.
2. `claude mcp list` from this folder: `rea` connected.
3. In a session here, call `binary_session` with `{}` and read `tool_availability`, then open one DLL.

## First session with REA

- `binary_session {}` before any target: 77 tools available, 72 `target_required`, 27 `provider_unavailable` (adb, apktool), 21 `provider_missing` (JEB, jadx, sigrok, binwalk and others), 10 `unsupported_host`. Ghidra provider `available`; no missing client requirements.
- None of `UnrealEditor-Core`, `-CoreUObject`, `-Engine`, `-RenderCore`, `-Renderer` has a PDB beside it. The 540 PDBs in `Binaries\Win64` belong to standalone programs (CrashReportClient, BuildPatchTool and others). Editor module PDBs come from the launcher option "Editor symbols for debugging", not installed.
- `UnrealEditor-Core.dll` (20,021,528 bytes, SHA-256 `6ac94596...24bc`) records PDB `UnrealEditor-Core.pdb`, GUID `{55A4614C-6E78-418A-B18A-2717DF82C0E3}`, bare file name only, and exports 7,120 decorated C++ names (`llvm-readobj --coff-exports`). Public API names are therefore available without a PDB.
- Even with the editor symbols installed, REA would not load them: it imports a private copy and neither copies a sibling PDB nor accepts one (`docs/ghidra-provider.md` lines 62-64).
- Opening Core with `provider_id: ghidra` succeeded, but the first query (`binary_overview`) failed with `provider_timeout`: import plus auto-analysis did not finish within the default 330,000 ms `REA_GHIDRA_STARTUP_TIMEOUT_MS`. Not out of memory. PDB load state was not reported because the handshake never completed. REA removed its temp runtime; no Java process remained.
- Remedies named by REA: raise `REA_GHIDRA_STARTUP_TIMEOUT_MS` in the registration env, or skip analyzers with `REA_GHIDRA_DISABLED_ANALYZERS`; the MCP client tool-call timeout is separate. Claude Code moved the call to a background task after 120 s and it kept running, so the client timeout was not the limit.
- Re-registered at local scope with `REA_GHIDRA_STARTUP_TIMEOUT_MS=1800000` (30 min), full analysis kept, heap still 2G. Command, from Git Bash in this folder: `MSYS_NO_PATHCONV=1 claude mcp add --scope local rea -e 'GHIDRA_INSTALL_DIR=C:\tools\ghidra_12.1.4_PUBLIC' -e 'JAVA_HOME=C:\tools\jdk-21.0.12.1+1' -e REA_GHIDRA_STARTUP_TIMEOUT_MS=1800000 -- cmd.exe /d /c npx -y rea-agents@6.7.0 mcp`. `claude mcp add-json` with the same config was rejected with "Invalid configuration: : Invalid input". `claude mcp list` reports `rea` connected. A running Claude Code session keeps the old env until restarted.

## Core analysis result

- After the restart with the 30-minute limit, Ghidra 12.1.4 finished default auto-analysis of `UnrealEditor-Core.dll` in about 10 minutes (Java started 13:10:44, result before 13:21) on the 2G heap. No out-of-memory.
- PDB handshake: Ghidra references `UnrealEditor-Core.pdb`, GUID `55a4614c-6e78-418a-b18a-2717df82c0e3`, age 1, version RSDS, load state **unknown**. In practice no PDB was available (none installed, REA does not copy one), so names come from exports and Ghidra's own recovery only.
- Inventory: image base `0x180000000`; 44,286 procedures; 29,940 defined strings; 10 segments, `.text` 14.2 MB, `.rdata` 4.5 MB, `.data` 10.3 MB, `.pdata` 0.55 MB, plus a 44 KB `.uedbg` section (Unreal-specific debug data section, contents not yet inspected).
- With 7,120 named exports against 44,286 procedures, at most about 16% of Core's recovered functions carry an original name.

## Rebuild timeline (parked)

Derived estimate, order of magnitude only.

- Godot: in-house from 2001, open-sourced February 2014; about 2.1M lines (Open Hub, secondary snippet); about 3,980 contributors including anonymous (GitHub API).
- O3DE: CryEngine code licensed to Amazon in 2015, released as O3DE July 2021; 127.6 MB of C++ and about 350 contributors (GitHub API). It grew by inheriting code, so it gives no from-scratch rate.
- UE 5.5 headers alone are about 4.1 times Godot's whole codebase; at Godot's pace (about 25 years for 2.1M lines) that is about 100 years.
- AI factor: METR 2025 RCT, experienced developers on large mature repos, 19% slower (about 120 years). Peng et al. 2023, small greenfield task, 55.8% faster (about 45 years). METR's 2026 follow-up reported its design no longer gives a reliable signal.
- Range: about 45 to 120 years at Godot-community pace. Lines are not features, Godot's growth was not linear, and both studies predate current models.

Sources: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ , https://arxiv.org/abs/2302.06590 , https://blog.robbowley.net/2026/04/04/metrs-developer-productivity-research-2026-update/ , https://www.wikipedia.org/wiki/O3DE , https://www.openhub.net/p/godotengine
- Closed with `close_binary` and a snapshot at `snapshots/UnrealEditor-Core.rea-snapshot` (git-ignored). It is 32,627 bytes with 2 evidence records: it keeps the cached query results, not Ghidra's database, so new queries on Core will likely re-run the roughly 10-minute analysis.

## Imports through REA

- A module graph built with `llvm-readobj` was reverted (`97b5f73`): the study order must come from REA.
- REA has no PE import view: `inspect_binary_layout` covers ELF on Linux only. Imports come from `list_names`, where Ghidra external symbols carry the library, e.g. `TBBMALLOC.DLL::scalable_free` at `EXTERNAL:0x5`, `source: imported`.
- For Core, `list_names` completed (about 10 min of analysis) but its response (10,549,103 bytes) exceeded REA's 10 MB MCP budget. Retained evidence exported with `export_evidence_bundle` to `snapshots/UnrealEditor-Core.evidence.json` (127,151,029 bytes, git-ignored): 432,320 names, 630 external.
- Core imports from 35 libraries. Unreal modules: UnrealEditor-TraceLog (33 symbols), UnrealEditor-BuildSettings (10). Third-party: TBBMALLOC (5), WinPixEventRuntime (2). The rest are Windows and MSVC runtime DLLs (KERNEL32 227, MSVCP140 65, USER32 49, DBGHELP 17 and others).
- Whether Ghidra lists delay-load imports among these externals is not yet established.
- REA CLI `analyze <dll> --provider ghidra --json` (run with `GHIDRA_INSTALL_DIR`, `JAVA_HOME`, `REA_GHIDRA_STARTUP_TIMEOUT_MS` prefixed) returns the same overview as MCP `binary_overview`: segments and counts, no imports. On UnrealEditor-TraceLog.dll (SHA-256 `9db62425...5082`): 336 procedures, 182 strings, `.text` 82 KB; PDB `UnrealEditor-TraceLog.pdb` referenced, load state unknown. Output kept at `snapshots/TraceLog.analyze.json`.
- `rea --help` (6.7.0) has no CLI form of MCP `list_names`. Native name access on the CLI: `search` ("every analyzed string or procedure name"), `function`, `xrefs`, `trace`. `inspect-with-objdump` wraps GNU objdump and keeps its raw output as Evidence; GNU objdump is not installed on this machine.
- REA CLI `search <dll> "DLL::" --provider ghidra --json` on TraceLog ran `search_strings` (literal, case-insensitive), not a procedure-name search, and returned no matches. Output kept at `snapshots/TraceLog.search.json`. The flag that selects procedure names is not yet known.
- REA CLI `search <dll> "DLL::" --kind procedures --provider ghidra --json` returns imported functions with their library: TraceLog gives 87 (`EXTERNAL:0x1` = `WS2_32.DLL::accept`), from KERNEL32 29, CRT runtime 22, WS2_32 13, VCRUNTIME140 12, CRT heap 7, VCRUNTIME140_1 2, CRT string 1, CRT stdio 1. No Unreal module imports. Imported data labels (type `label` in `list_names`, e.g. Core's `TBBMALLOC.DLL::scalable_allocation_command`) are not procedures and are missed; a DLL imported only for data would not show as a dependency.
- First full import batch run (started from the session prompt) stopped at 36/498 after AudioCaptureWasapi: the session host killed it while the system was critically low on memory. 38 `search.json` files exist in `snapshots/imports` (including the two smoke-test DLLs), no error files, no Ghidra process left. Rerunning the same line resumes from the next DLL.

## Import batch, second run on a 1 GB Ghidra heap

- Started with `GHIDRA_HEADLESS_MAXMEM=1G` at the `!` prompt with 1.8 GB RAM free.
- Claude Code stopped it on low system memory after `[84/498] ChaosVehiclesCore ok 53s`. 85 of the 498 modules have a `search.json` (the first 84 in alphabetical order plus TraceLog from the earlier test), and there are no `error.txt` files.
- DLLs 37 to 84 took 32 to 72 s each on the 1 GB heap, and none failed out of memory.
- After the stop, 1.3 GB RAM was free and no Java process was left.
- A run at the `!` prompt is stopped whenever system memory gets critically low. Running it in a separate Git Bash window avoids that.
