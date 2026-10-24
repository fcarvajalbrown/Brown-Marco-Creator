# 0003. Source assets stay as source files, no proprietary container

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

UE 4.27 converts every import into a `.uasset`, so the project holds Epic-format copies instead of the files the artist made. Felipe marked this critical: imports must stay as they are, with a friendly browser like Godot's and Unity's.

## Decision

Imported files stay in the project as they are (glTF, FBX, PNG, WAV and the like), with no conversion into a proprietary container. The Content Browser shows them in place, in the manner of Godot's and Unity's browsers.

## Consequences

- Assets stay editable in their own tools.
- The engine still needs GPU-ready data; where that and per-asset import settings live is open and needs its own ADR with Felipe's input.

## Alternatives considered

- An engine container like `.uasset`. Rejected by Felipe.
