# Brown Marco Creator product requirements

## Vision

A game engine and editor of Felipe's own that keeps the Unreal Engine 4.27 way of working and drops what he does not need. Two reasons, in his words: UE 5.5 asks too much of most players' hardware, and Blueprints are critical while Epic plans to deprecate them in UE6 ([research](research/ue6-blueprints.md)). The engine is his protest. See [ADR 0001](adr/0001-own-engine-ue427-study-only.md).

## Scope

Kept from UE 4.27, as workflow and not as code ([ADR 0002](adr/0002-scope-and-platforms.md)):

- Editor: layout and viewport, Content Browser, Details panel and World Outliner, Play In Editor.
- Scripting: Blueprint-style visual scripting, Animation Blueprint-style graphs, behaviour trees and AI.
- Content: material editor, Sequencer-style cinematics, Cascade/Niagara-style particles, UMG-style UI, LODs and HLODs, level streaming.
- Rendering: 4.27-level quality without the toon-ish UE4 look, Lightmass-style baked light, post-process volumes.
- Runtime: gameplay framework, gamepad-first input, physics, a MetaSound-style parameterised audio graph.
- Shipping: packaging and cooking.

Rule: study everything in 4.27 first, then cut.

Platforms: current Windows, Linux and Steam Deck, current consoles. No mobile, no iOS.

Out: mobile, iOS, `.uasset` or any other proprietary asset container ([ADR 0003](adr/0003-source-assets-no-container.md)), separate editor modes ([ADR 0005](adr/0005-single-editor-mode.md)).

## Architecture

- C++ with Dear ImGui docking for the editor ([ADR 0004](adr/0004-cpp-and-dear-imgui.md)).
- Imported assets stay as their source files on disk; the Content Browser reads them in place, like Godot and Unity, with derived data kept in a rebuildable cache ([ADR 0003](adr/0003-source-assets-no-container.md)).
- One editor mode. Landscape, foliage and mesh editing are tools inside it, including modeling tools such as auto UV, like UE4's beta and UE5's modeling mode ([ADR 0005](adr/0005-single-editor-mode.md)).
- Apache-2.0 licence ([ADR 0006](adr/0006-apache-2-licence.md)), Vulkan only at first ([ADR 0007](adr/0007-vulkan-first.md)), Jolt Physics ([ADR 0008](adr/0008-jolt-physics.md)).
- CMake ([ADR 0009](adr/0009-cmake.md)); GPU-ready data in a rebuildable cache, import settings in a plain-text sidecar beside each source asset ([ADR 0010](adr/0010-asset-cache-and-sidecars.md)); SDL3 for windowing and input ([ADR 0011](adr/0011-sdl3.md)).

## Phases

A phase ends on a check that has to pass. Status lives in `ROADMAP.md`. Order is dependency first.

### A. Study UE 4.27 with REA

The module import graph and per-module study run in `ue55-rea` (`fcarvajalbrown/ue55-rea`). Here: a note per kept feature in `docs/research/ue427/`, then a cut list of what 4.27 carries that this engine drops.

Exit: a note per kept feature and a cut list, each claim tagged as found by REA, observed in the 4.27 editor, or read in Epic's docs.

### B. Workspace and editor shell

A C++ workspace that builds on Windows and Linux, a window with Dear ImGui docking and an empty dockable layout.

Exit: the empty editor opens on Windows and Linux; the build and its tests are clean.

### C. Core and source-asset registry

Math, memory, logging, a module system, and the asset registry that watches source files and fills the derived-data cache.

Exit: dropping a glTF and a PNG into the project shows both in the registry; deleting the cache and reopening rebuilds it.

### D. Renderer

Deferred renderer at 4.27-level quality, without the toon-ish look; post-process volumes.

Exit: a test scene renders on Windows and Linux, frame time measured on this desktop (RTX 3060) and recorded.

### E. Editor panels

Viewport, Content Browser on source files, Details, World Outliner, in the single mode.

Exit: a level is built from the Content Browser, saved, reloaded and matches.

### F. Gameplay framework, input, Play In Editor

Actor and component model, game mode, pawn and controller, gamepad-first input, Play In Editor.

Exit: a pawn moves on an Xbox controller in Play In Editor.

### G. Visual scripting

Blueprint-style graphs: events, functions, variables, debugging.

Exit: the pawn's movement from F rebuilt as a graph, same result on the pad.

### H. Material editor

Node graph to shader, material instances.

Exit: a material built in the graph renders the same in the viewport and in a packaged build.

### I. Physics, animation, AI

Physics, Animation Blueprint-style graphs, behaviour trees.

Exit: an animated character walks, collides and follows an AI patrol.

### J. Audio, UI, cinematics, particles

MetaSound-style audio graph, UMG-style UI, Sequencer-style cinematics, Cascade/Niagara-style particles.

Exit: a menu driven by the pad, a cutscene with a parameterised sound and a particle effect, in Play In Editor.

### K. Lighting and world scale

Lightmass-style baked light, LODs and HLODs, level streaming.

Exit: a level with baked light streams in and out, frame time measured and recorded.

### L. Modeling tools

Mesh editing in the single mode, auto UV.

Exit: a box edited into a simple prop, auto-UV'd and lightmapped without overlap.

### M. Packaging and cooking

Windows, Linux and Steam Deck first; consoles once their developer programmes are open to Felipe.

Exit: the test game packaged and run on Windows, Linux and a Steam Deck.
