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
- Download zips kept in `C:\tools\dl`.
- `rea-agents@6.7.0 doctor --provider ghidra --json`, run from this folder: `"healthy": true`; all ten Ghidra checks pass, including native decompiler and Windows native authority (local NTFS only). Global client registrations report `missing`, which is expected: REA is meant to be registered at local scope only.
- Run REA commands from this folder, never from the REA source checkout: there, `npx rea-agents@6.7.0` resolves to the checkout's own package and fails with "'rea' is not recognized".
- From the `!` prompt (Git Bash), `cmd /c` is rewritten to a drive path; use Bash env-prefix syntax or `cmd.exe //d //c`.

- Registered: `claude mcp add --scope local rea` with `GHIDRA_INSTALL_DIR` and `JAVA_HOME` env, stored in `~/.claude.json` under project `C:\Projects\ue55-rea`; `claude mcp list` from this folder reports `rea` connected.

## Readiness checks

1. `npx -y rea-agents@6.7.0 doctor --provider ghidra --json` with `GHIDRA_INSTALL_DIR` and `JAVA_HOME` set: expect `"healthy": true`.
2. `claude mcp list` from this folder: `rea` connected.
3. In a session here, call `binary_session` with `{}` and read `tool_availability`, then open one DLL.

## Rebuild timeline (parked)

Derived estimate, order of magnitude only.

- Godot: in-house from 2001, open-sourced February 2014; about 2.1M lines (Open Hub, secondary snippet); about 3,980 contributors including anonymous (GitHub API).
- O3DE: CryEngine code licensed to Amazon in 2015, released as O3DE July 2021; 127.6 MB of C++ and about 350 contributors (GitHub API). It grew by inheriting code, so it gives no from-scratch rate.
- UE 5.5 headers alone are about 4.1 times Godot's whole codebase; at Godot's pace (about 25 years for 2.1M lines) that is about 100 years.
- AI factor: METR 2025 RCT, experienced developers on large mature repos, 19% slower (about 120 years). Peng et al. 2023, small greenfield task, 55.8% faster (about 45 years). METR's 2026 follow-up reported its design no longer gives a reliable signal.
- Range: about 45 to 120 years at Godot-community pace. Lines are not features, Godot's growth was not linear, and both studies predate current models.

Sources: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ , https://arxiv.org/abs/2302.06590 , https://blog.robbowley.net/2026/04/04/metrs-developer-productivity-research-2026-update/ , https://www.wikipedia.org/wiki/O3DE , https://www.openhub.net/p/godotengine
