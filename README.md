# ue55-rea

Study of Unreal Engine 5.5 from its installed DLLs (`D:\EpicGames\UE_5.5\Engine\Binaries\Win64`), with every fact taken through REA and Ghidra. The long-term aim is to find legacy code worth removing. That removal needs Epic's full GitHub source, which this install does not have: the launcher ships headers and DLLs only.

| File | What it holds |
|---|---|
| `ROADMAP.md` | Open work, phase by phase, with the commands for each step |
| `docs/ROADMAP-HISTORY.md` | Finished items, newest first |
| `notes/findings.md` | Every measured result, with numbers and sources |
| `tools/rea-imports/rea_imports.py` | Batch: REA import search over all module DLLs |
| `snapshots/` | REA outputs. Git-ignored and large (Core's evidence export alone is 127 MB) |

## Before running anything

- Run every command from `C:\Projects\ue55-rea`. From `C:\Projects\rea` (the REA source checkout), `npx rea-agents@6.7.0` picks up the checkout instead and fails with "'rea' is not recognized".
- The `!` prompt is Git Bash, not cmd or PowerShell. Environment variables go in front of the command (`NAME=value command`), and `cmd /c` gets mangled into a drive path; use `cmd.exe //d //c` if you ever need it.
- Windows flags like `/F` get rewritten by Git Bash. Prefix the command with `MSYS_NO_PATHCONV=1`, or put the whole thing inside a single-quoted PowerShell string as in the pause command below.
- A command that runs longer than 120 s at the `!` prompt moves to the background on its own. It keeps running, but it stops if the session closes. For the long batch, a separate Git Bash window is safer (see below).

## Installed pieces

| Piece | Where |
|---|---|
| Ghidra 12.1.4 | `C:\tools\ghidra_12.1.4_PUBLIC` |
| JDK 21 (Temurin 21.0.12.1) | `C:\tools\jdk-21.0.12.1+1` |
| Download zips | `C:\tools\dl` |
| REA | `rea-agents@6.7.0` through `npx`, MCP server registered at local scope for this folder only |

REA accepts Ghidra 12.1.x only, so do not upgrade Ghidra to 12.2.

## Health checks

```
! GHIDRA_INSTALL_DIR='C:\tools\ghidra_12.1.4_PUBLIC' JAVA_HOME='C:\tools\jdk-21.0.12.1+1' npx -y rea-agents@6.7.0 doctor --provider ghidra --json
! claude mcp list
```

The first should report `"healthy": true`. Global client registrations show as `missing`, which is expected. The second should show `rea` connected.

## REA registration

Show the current entry:

```
! claude mcp get rea
```

Register it again (remove first, then add). `claude mcp add-json` with the same settings was rejected with "Invalid input", so use this form:

```
! claude mcp remove --scope local rea
! MSYS_NO_PATHCONV=1 claude mcp add --scope local rea -e 'GHIDRA_INSTALL_DIR=C:\tools\ghidra_12.1.4_PUBLIC' -e 'JAVA_HOME=C:\tools\jdk-21.0.12.1+1' -e REA_GHIDRA_STARTUP_TIMEOUT_MS=1800000 -- cmd.exe /d /c npx -y rea-agents@6.7.0 mcp
```

A running session keeps the old settings. After any change: `/exit`, then `claude --continue` from this folder.

Two settings you may need later:
- `REA_GHIDRA_STARTUP_TIMEOUT_MS`: how long Ghidra may take to import and analyse before REA gives up. Default 330000 (5.5 min) was too short for Core; it is now 1800000 (30 min).
- `GHIDRA_HEADLESS_MAXMEM`: Ghidra's heap, default 2G. Core fit in 2G. Raise it (add `-e GHIDRA_HEADLESS_MAXMEM=4G`) only if a DLL fails with out-of-memory.

## The import batch (Phase 1)

Start it:

```
! python -I tools/rea-imports/rea_imports.py --binaries 'D:/EpicGames/UE_5.5/Engine/Binaries/Win64' --out snapshots/imports
```

To keep it independent of the session, open Git Bash yourself, `cd /c/Projects/ue55-rea`, and run the same line without the `!`. Progress then prints in that window as `[n/498] Module ok 54s`.

Check progress from the prompt:

```
! ls snapshots/imports/*.search.json | wc -l
! ls snapshots/imports/*.error.txt
```

Pause it. This stops the batch together with the node and Ghidra processes it started:

```
! powershell -NoProfile -Command 'Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match "rea_imports" -and $_.Name -eq "python.exe" } | ForEach-Object { taskkill /T /F /PID $_.ProcessId }'
```

It finds two python processes. The second one usually comes back as "not found" because killing the first one's tree already ended it.

Resume: run the start line again. Finished DLLs are skipped. The DLL that was in progress when you paused starts over, because REA does not keep a half-finished Ghidra analysis.

Retry only the ones that failed:

```
! python -I tools/rea-imports/rea_imports.py --binaries 'D:/EpicGames/UE_5.5/Engine/Binaries/Win64' --out snapshots/imports --only Core CoreUObject
```

Timing so far: small DLLs take 32 to 172 s, Core took about 10 min. The first eight averaged 77 s each, so the full 498 is likely 10 hours or more, mostly in the big modules (Engine is 77 MB, almost four times Core).

## Single-DLL commands

Swap the DLL name at the end of the path. Each writes a JSON you can hand back for reading.

Overview (segments, procedure and string counts, PDB state):

```
! GHIDRA_INSTALL_DIR='C:\tools\ghidra_12.1.4_PUBLIC' JAVA_HOME='C:\tools\jdk-21.0.12.1+1' npx -y rea-agents@6.7.0 analyze 'D:\EpicGames\UE_5.5\Engine\Binaries\Win64\UnrealEditor-TraceLog.dll' --provider ghidra --json > snapshots/TraceLog.analyze.json
```

Imported functions, with the DLL each comes from:

```
! GHIDRA_INSTALL_DIR='C:\tools\ghidra_12.1.4_PUBLIC' JAVA_HOME='C:\tools\jdk-21.0.12.1+1' npx -y rea-agents@6.7.0 search 'D:\EpicGames\UE_5.5\Engine\Binaries\Win64\UnrealEditor-TraceLog.dll' "DLL::" --kind procedures --provider ghidra --json > snapshots/TraceLog.search.json
```

`search` looks at strings unless you pass `--kind procedures`. For a big DLL add `REA_GHIDRA_STARTUP_TIMEOUT_MS=1800000` to the front.

Command list and per-command options:

```
! npx -y rea-agents@6.7.0 --help
! npx -y rea-agents@6.7.0 search --help
```

## Phase 2 commands, only if Phase 1 fails

```
! winget install --id BrechtSanders.WinLibs.POSIX.UCRT -e
! objdump --version
! npx -y rea-agents@6.7.0 inspect-with-objdump 'D:\EpicGames\UE_5.5\Engine\Binaries\Win64\UnrealEditor-TraceLog.dll' file_headers --json > snapshots/TraceLog.objdump-headers.json
! npx -y rea-agents@6.7.0 inspect-with-objdump 'D:\EpicGames\UE_5.5\Engine\Binaries\Win64\UnrealEditor-TraceLog.dll' symbols --json > snapshots/TraceLog.objdump-symbols.json
```

WinLibs is open source; restart the terminal after installing so `objdump` is on `PATH`. REA documents no PE import-table option for objdump, so this is a test and may give nothing useful.

## Cleaning up

Leftover Ghidra runs as `java.exe`:

```
! tasklist | grep -i java
```

If one is left from a REA session, closing the target in the session (`close_binary`) stops it. Killing every `java.exe` would also hit unrelated Java programs, so find the PID first and kill only that one:

```
! MSYS_NO_PATHCONV=1 taskkill /T /F /PID <pid>
```

## Limits worth remembering

- No editor PDBs are installed, and REA would not load them anyway: it analyses a private copy and never copies a sibling PDB. Names come from exports (Core has 7,120) and Ghidra's own recovery. The launcher option "Editor symbols for debugging" downloads them if a run outside REA ever needs them.
- The import search finds imported functions only. A DLL imported purely for data (Core's `TBBMALLOC.DLL::scalable_allocation_command` is a data label) does not show as a dependency.
- MCP replies are capped at 10 MB. Core's full name list was 10.5 MB, so it went out through `export_evidence_bundle` to a file instead.
- A REA snapshot saved on close keeps cached answers, not Ghidra's database. Asking a new question about a DLL runs the full analysis again.
- These are editor builds. Editor-only code is compiled out of a shipping game, so a dependency seen here is not proof that the code ships.
