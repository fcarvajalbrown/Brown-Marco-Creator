# Modeling Tools mode

Sources: https://docs.unrealengine.com/4.27/API/Plugins/ModelingToolsEditorMode/index.html (4.27 API reference) and https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine (current, unversioned guide)

- The 4.27 API reference lists a ModelingToolsEditorMode plugin; no 4.27 user guide for it was found. [docs]
- The current guide describes Modeling Mode as a toolset for creating, sculpting and editing geometry: topology edits, UV creation, multiple material assignments, collision editing and texture baking. It may differ from 4.27. [docs, UE5 page]
- In the current guide the mode is enabled through Edit > Plugins > Modeling Tools Editor Mode and has panels for Tool Category, Tool Palette, Tool Properties and Quick Settings. [docs, UE5 page]

## For Brown Marco Creator

Phase L. The 4.27 behaviour needs the editor or REA on the plugin's DLLs; UE5's guide only sets the feature list Felipe asked for (auto UV and the like). Tools live in the single mode of [ADR 0005](../../adr/0005-single-editor-mode.md).

