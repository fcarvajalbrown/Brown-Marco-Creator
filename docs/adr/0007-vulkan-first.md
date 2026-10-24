# 0007. Vulkan only at first

- Status: Proposed
- Date: 2026-10-24
- Deciders: Felipe Carvajal Brown

## Context

The renderer (phase D) needs a graphics API for Windows, Linux and Steam Deck (ADR 0002).

## Decision

Vulkan is the only backend at first.

## Consequences

- One backend covers Windows, Linux and Steam Deck.
- Console backends are added in phase M, each on that console's own API.

## Alternatives considered

- D3D12 on Windows plus Vulkan on Linux: two backends from the start.
