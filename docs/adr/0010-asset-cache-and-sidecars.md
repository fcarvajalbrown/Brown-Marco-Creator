# 0010. Rebuildable asset cache and plain-text import sidecars

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

Source assets stay as they are (ADR 0003), but the engine still needs GPU-ready data and per-asset import settings stored somewhere.

## Decision

GPU-ready data goes to a git-ignored cache folder that can be deleted and rebuilt. Each source asset gets a small plain-text settings sidecar beside it, as in Godot's `.import` model.

## Consequences

- Deleting the cache loses nothing; reopening the project rebuilds it.
- Sidecars live in version control and diff as text.
- The asset registry watches the file system and rebuilds cache entries when a source or its sidecar changes.

## Alternatives considered

- One project-wide settings database plus the cache.
