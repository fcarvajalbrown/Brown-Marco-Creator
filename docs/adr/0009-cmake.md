# 0009. CMake

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

The C++ workspace (phase B) must build on Windows and Linux.

## Decision

CMake is the build system.

## Consequences

- Dear ImGui, the Vulkan SDK samples and Jolt Physics all ship CMake support, so they build in the same tree.

## Alternatives considered

- Premake.
- Meson.
