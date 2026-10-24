# Level Editor layout and viewport

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=4.27

- The Level Editor creates, views and modifies levels, mainly by placing, transforming and editing the properties of Actors. [docs]
- Any object placed in the world (light, mesh, character) is an Actor: a class with 3D position, rotation and scale. [docs]
- Default layout: tab bar and menu bar, toolbar, Place Actor / Modes panel, viewports, Content Browser, World Outliner, Details. [docs]
- The interface is highly customisable; tabs from other editor windows dock beside the level tab, like browser tabs. [docs]

## For Brown Marco Creator

Phases B and E on Dear ImGui docking ([ADR 0004](../../adr/0004-cpp-and-dear-imgui.md)). The Place Actor and Modes panel becomes the single tool palette of [ADR 0005](../../adr/0005-single-editor-mode.md).
