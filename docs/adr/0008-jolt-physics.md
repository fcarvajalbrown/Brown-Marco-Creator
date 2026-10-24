# 0008. Jolt Physics

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

Physics is in scope (ADR 0002, phase I). UE 4.27 used PhysX.

## Decision

Jolt Physics (MIT licence) is the physics library.

## Consequences

- Physics behaviour is Jolt's, not a PhysX match; the 4.27 study informs the gameplay-facing API, not the solver.

## Alternatives considered

- PhysX 5 (BSD-3), the family UE 4.27 used.
