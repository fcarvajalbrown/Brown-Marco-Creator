# 0004. C++ with Dear ImGui docking for the editor

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

The engine and editor need a language and an editor UI toolkit. The code under study, UE 4.27, is C++.

## Decision

C++ for engine and editor, Dear ImGui with its docking branch for the editor UI. Felipe chose it after research: it is the most mature editor UI of the options he weighed, and C++ maps onto the 4.27 code being studied.

## Consequences

- The editor's dockable layout comes from Dear ImGui docking.
- Game UI (the UMG-style system) is separate from the editor UI.
- Felipe's Rust crates (SKP Forge) are not linked directly; any reuse goes through a C ABI or a port.

## Alternatives considered

- Rust, as in Minga3D and SKP Forge. Reuses his crates, but maps less directly onto the C++ under study.
