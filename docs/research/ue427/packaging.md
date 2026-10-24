# Packaging and cooking

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-unreal-engine-projects?application_version=4.27

- Packaging compiles project code, cooks content into the target platform's format, then bundles code and cooked content into a distributable set of files. [docs]
- Started from File > Package Project > [Platform]; a Game Default Map must be set under Project Settings > Maps & Modes or a blank project starts on a black screen. [docs]

## For Brown Marco Creator

Phase M. Cooking reads source files plus the cache ([ADR 0010](../../adr/0010-asset-cache-and-sidecars.md)); a default-map check belongs in the packaging step.
