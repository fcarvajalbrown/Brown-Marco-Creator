# Lightmass and global illumination

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine?application_version=4.27

- Global illumination is either precomputed (baked into lightmap textures) or dynamic; both can be blended. [docs]
- Baked lighting suits scenes whose lighting does not change; its cost is lightmap memory, its quality is set by lightmap resolution, and Static Meshes need a Lightmap UV. [docs]
- Lightmass bakes on the CPU, using a separate process, Unreal Swarm, that can also distribute builds to farms. [docs]
- GPU Lightmass is Beta in 4.27: it uses DX12 and ray tracing, runs in a single in-editor process, has no Swarm distribution, and supports multiple GPUs through SLI. [docs]
- Dynamic GI updates as lights change (time of day, a light switched on), at a higher real-time cost. [docs]

## For Brown Marco Creator

Phase K. Baked GI on Vulkan; a GPU baker fits the target hardware (RTX 3060 desktop), without Swarm. The lightmap UV comes from phase L's auto UV.
