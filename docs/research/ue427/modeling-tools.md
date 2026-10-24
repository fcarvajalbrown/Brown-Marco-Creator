# Modeling Tools Editor Mode

Sources: the UE 4.27.2 install's plugin descriptors `Engine/Plugins/Experimental/ModelingToolsEditorMode/ModelingToolsEditorMode.uplugin` and `Engine/Plugins/Experimental/MeshModelingToolset/MeshModelingToolset.uplugin`; API index https://docs.unrealengine.com/4.27/API/Plugins/ModelingToolsEditorMode/index.html

- Modeling Tools Editor Mode is a beta plugin under Experimental: "Modeling Tools Mode includes a suite of interactive tools for creating and editing meshes in the Editor". [install]
- It depends on the Mesh Modeling Toolset (beta): "A set of modules implementing 3D mesh creation and editing based on the Interactive Tools Framework", plus StylusInput. [install]
- The toolset's modules: ModelingComponents, ModelingOperators, ModelingOperatorsEditorOnly, MeshModelingTools, MeshModelingToolsEditorOnly; it depends on GeometryProcessing, ProxyLODPlugin and HairStrands. [install]
- The API exposes UModelingToolsEditorModeSettings, FModelingToolsEditorMode and FModelingToolsEditorModeToolkit. [docs]

## For Brown Marco Creator

Phase L. The user guide page for 4.27 is not found yet; the tool list (auto UV and others) should come from REA on `UE4Editor-MeshModelingTools.dll` if the deferred plugin batch runs in `study/ue427-rea`.

