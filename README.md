# Brown Marco Creator

A C++ game engine and editor built around the Unreal Engine 4.27 workflow, with Blueprint-style visual scripting, source assets kept as they are, and lighter hardware needs than UE5.

![Status](https://img.shields.io/badge/status-planning-orange)
![Language](https://img.shields.io/badge/language-C%2B%2B-blue)
![Editor UI](https://img.shields.io/badge/editor-Dear%20ImGui-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20Steam%20Deck-blue)

## Why

UE 4.27 is the engine I love working in. I think UE 5.5 asks more of a player's machine than most players have, and the next version is dropping the part I care about most.

At Unreal Fest in June 2026 Epic published ["The road to UE 6"](https://www.unrealengine.com/news/the-road-to-ue-6). Gameplay programming moves to Verse and a new Scene Graph framework. In Epic's words, as [quoted by 80 Level](https://80.lv/articles/upd-unreal-engine-6-will-combine-uefn-and-ue-into-a-unified-engine): "Actors and Blueprints will be in early versions of UE6. Eventually, these will be deprecated when the new framework is sufficiently mature, and you'll have conversion tools to move projects from one framework to the other." [CG Channel](https://www.cgchannel.com/?p=176658) reports early access planned for the end of 2027 and a stable release 12 to 18 months later, and calls the loss of Blueprints "one of the most controversial parts of this week's announcements".

CG Channel also notes what Blueprints give people: artists and designers without a programming background can build content that works in game, with over a decade of learning material online. This engine keeps that way of working, and it is my protest. Sources and exact quotes: [docs/research/ue6-blueprints.md](docs/research/ue6-blueprints.md).

## What it keeps from UE 4.27

The workflow, not Epic's code. Everything here is written from scratch; UE 4.27 is studied, never copied.

- Editor layout and viewport, Content Browser, Details panel, World Outliner, Play In Editor
- Blueprint-style visual scripting and animation graphs, behaviour trees
- Material editor, Sequencer-style cinematics, particles, UMG-style UI
- 4.27-level rendering without the toon-ish look, baked lighting, post-process volumes, LODs and HLODs, level streaming
- Gameplay framework, gamepad-first input, physics, a parameterised audio graph
- Packaging and cooking

## What it drops

- `.uasset`. Your imports stay as the files you made (glTF, FBX, PNG, WAV), browsable the way Godot and Unity show them.
- Editor modes. Landscape, foliage and mesh editing are tools in one mode, with modeling tools and auto UV built in.
- Mobile and iOS. Targets are current Windows, Linux and Steam Deck, then consoles.

Everything else in 4.27 gets studied first and cut only after that.

## Status

Planning. Scope, phases and decisions are written down; no engine code yet. The study of the UE 4.27 binaries runs in [study/ue427-rea](study/ue427-rea/README.md).

- Roadmap: [ROADMAP.md](ROADMAP.md)
- Product requirements and phases: [docs/PRD.md](docs/PRD.md)
- Decisions: [docs/adr](docs/adr/README.md)

Licensed under Apache-2.0, see [LICENSE](LICENSE).

Made by Brøwn Marcó Studios, Santiago, Chile.
