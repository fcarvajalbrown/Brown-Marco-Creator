# Input

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/input-in-unreal-engine?application_version=4.27

- PlayerInput, a UObject inside PlayerController spawned only on the client, turns hardware input into data Actors use. [docs]
- ActionMappings bind a discrete key or button to a friendly name for event-driven behaviour. [docs]
- AxisMappings bind keyboard, controller or mouse input to a friendly name for continuous behaviour; they are polled every frame even at zero. [docs]
- Unusual devices are configured through the RawInput plugin. [docs]

## For Brown Marco Creator

Phase F on SDL3 ([ADR 0011](../../adr/0011-sdl3.md)): action and axis mappings by friendly name, with gamepad defaults first.
