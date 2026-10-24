# 0002. Scope and platforms

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

UE 4.27 carries far more than Felipe uses. He named the parts he wants kept and the platforms "newer game exports" means.

## Decision

Kept, as workflow: editor layout and viewport, Content Browser, Details and World Outliner, Play In Editor, Blueprint-style visual scripting, material editor, 4.27-level renderer quality without the toon-ish UE4 look, Sequencer-style cinematics, Cascade/Niagara-style particles, level streaming, gameplay framework, gamepad-first input, UMG-style UI, behaviour trees and AI, Lightmass-style baked light, post-process volumes, LODs and HLODs, Animation Blueprint-style graphs, physics, a MetaSound-style parameterised audio graph, packaging and cooking.

Rule: study everything in 4.27 first, then cut.

Platforms: current Windows, Linux and Steam Deck, current consoles. No mobile, no iOS.

## Consequences

- Phase A covers every kept feature before any is cut.
- Console packaging depends on the console makers' developer programmes, which need Felipe's application.
- Mobile renderers, touch input and iOS packaging are never built.

## Alternatives considered

- Port all of 4.27, then trim later. Rejected by the study-then-cut rule.
- Add mobile and iOS. Felipe excluded both.
