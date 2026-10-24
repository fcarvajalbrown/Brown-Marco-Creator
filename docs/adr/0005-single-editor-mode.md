# 0005. One editor mode

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

UE 4.27 splits editing into modes (place, paint, landscape, foliage, mesh paint, and modeling in its beta plugin). Felipe wants one mode with no separate tabs for landscape and the like, and mesh editing with modeling tools like UE5's and UE4's beta (auto UV and similar).

## Decision

The editor has a single mode. Landscape, foliage, mesh painting and modeling are tools picked inside it, acting on the selection in the same viewport.

## Consequences

- Tool switching and selection rules are designed once for all tools.
- Modeling tools, auto UV included, are in scope (phase L).

## Alternatives considered

- UE 4.27's mode tabs. Rejected by Felipe.
