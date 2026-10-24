# 0001. Own engine, UE 4.27 as study material only

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

Felipe loves Unreal Engine 4.27 and wants it "deconstructed but made my own, remove all the grease and maintain for newer game exports needs". His reasons: UE 5.5 asks too much of most players' hardware, and Epic plans to deprecate Blueprints in UE6 ([research](../research/ue6-blueprints.md)). The UE 4.27.2 launcher install on his desktop ships DLLs and headers, not engine source. The `ue55-rea` repo already studies those DLLs with REA. Minga3D follows the same pattern for SketchUp.

## Decision

Brown Marco Creator is a new engine written from scratch. UE 4.27 is study material only: its workflow is kept, Epic's code is not used.

## Consequences

- Every behaviour taken from 4.27 is learned through REA, the editor or Epic's docs, never copied.
- The engine is free to differ from 4.27 internally wherever the workflow stays the same.
- The `ue55-rea` import graph and module study feed phase A.

## Alternatives considered

- Fork UE 4.27 source from Epic's GitHub and strip it. Needs Felipe's Epic-linked GitHub login and means maintaining millions of lines of someone else's code.
- Stay on the 4.27 binary and add plugins and tools for the new needs. Removes nothing.
