# Roadmap history

Finished items, moved out of `ROADMAP.md`, newest first. Detail lives in `notes/findings.md`; git dates each entry.

- Confirmed REA CLI `analyze` gives no imports and the CLI has no `list-names` command.
- Read Core's imports through MCP `list_names` and `export_evidence_bundle`: 630 externals from 35 libraries.
- Reverted a module graph built with `llvm-readobj`: facts must come from REA.
- Opened `UnrealEditor-Core.dll` in REA: 44,286 procedures, PDB load state unknown, analysis about 10 min on the 2G heap.
- Raised `REA_GHIDRA_STARTUP_TIMEOUT_MS` to 1,800,000 after Core timed out at 330 s.
- Installed Ghidra 12.1.4 and JDK 21; `rea doctor --provider ghidra` healthy; REA registered at local scope.
- Measured UE 5.5 size on disk and parked the clean-room rebuild estimate.
