# UE 4.27 core module study order

Built by `tools/study-order/study_order.py` from the REA import data in `snapshots/imports-ue4.27` (398 core modules). Layer 0 imports no other Unreal module; each module sits one layer above its highest dependency. Within a layer, the module with the most direct dependents comes first, then by name. Imported data labels are not in the REA data, so a module imported only for data is missing as a dependency.

Cycles (modules studied as one group): PacketHandler, ReliabilityHandlerComponent; ActorPickerMode, AddContentDialog, AdvancedPreviewScene, AnimGraph, AnimGraphRuntime, AnimationCore, AssetTools, AudioMixer, AugmentedReality, BlueprintCompilerCppBackend, BlueprintGraph, BlueprintNativeCodeGen, CinematicCamera, ClassViewer, ClothingSystemEditor, ClothingSystemRuntimeCommon, ClothingSystemRuntimeNv, CommonMenuExtensions, ContentBrowser, ContentBrowserData, CurveEditor, EditorInteractiveToolsFramework, EditorSubsystem, EditorWidgets, Engine, Foliage, GameProjectGeneration, GameplayTags, GraphEditor, HardwareTargeting, HeadMountedDisplay, HierarchicalLODUtilities, ImageWriteQueue, InteractiveToolsFramework, Kismet, KismetCompiler, KismetWidgets, Landscape, LevelEditor, LevelSequence, Localization, MRMesh, MaterialBaking, MaterialEditor, MaterialUtilities, MediaAssets, MediaUtils, MovieScene, MovieSceneCapture, MovieSceneTools, MovieSceneTracks, NavigationSystem, PIEPreviewDeviceProfileSelector, PropertyEditor, Renderer, SceneDepthPickerMode, SequenceRecorder, Sequencer, SharedSettingsWidgets, SkeletalMeshUtilitiesCommon, SoundFieldRendering, SourceControl, SourceControlWindows, StatsViewer, TimeManagement, UMG, UnrealEd, VREditor, ViewportInteraction.

Unreal imports with no matching core module: none.

| # | Layer | Module | Direct dependents | Imports from |
|---|---|---|---|---|
| 1 | 0 | TraceLog | 11 |  |
| 2 | 0 | BuildSettings | 2 |  |
| 3 | 0 | UELibrary | 0 |  |
| 4 | 1 | Core | 394 | BuildSettings, TraceLog |
| 5 | 2 | ApplicationCore | 52 | Core |
| 6 | 2 | Json | 41 | Core |
| 7 | 2 | Sockets | 11 | Core |
| 8 | 2 | SignalProcessing | 8 | Core |
| 9 | 2 | ImageCore | 7 | Core |
| 10 | 2 | XmlParser | 6 | Core |
| 11 | 2 | MeshUtilitiesCommon | 5 | Core |
| 12 | 2 | NetworkReplayStreaming | 5 | Core |
| 13 | 2 | Analytics | 3 | Core |
| 14 | 2 | Cbor | 3 | Core |
| 15 | 2 | RSA | 3 | Core |
| 16 | 2 | SSL | 3 | Core |
| 17 | 2 | DirectoryWatcher | 2 | Core |
| 18 | 2 | GeForceNOWWrapper | 2 | Core |
| 19 | 2 | MeshBuilderCommon | 2 | Core |
| 20 | 2 | Navmesh | 2 | Core |
| 21 | 2 | SandboxFile | 2 | Core |
| 22 | 2 | AVIWriter | 1 | Core |
| 23 | 2 | BackgroundHTTPFileHash | 1 | Core |
| 24 | 2 | CEF3Utils | 1 | Core |
| 25 | 2 | CrunchCompression | 1 | Core |
| 26 | 2 | FileUtilities | 1 | Core |
| 27 | 2 | IESFile | 1 | Core |
| 28 | 2 | Media | 1 | Core |
| 29 | 2 | UELibSampleRate | 1 | Core |
| 30 | 2 | UnrealAudio | 1 | Core |
| 31 | 2 | Voronoi | 1 | Core |
| 32 | 2 | Advertising | 0 | Core |
| 33 | 2 | AudioCaptureCore | 0 | Core |
| 34 | 2 | AudioCaptureRtAudio | 0 | Core |
| 35 | 2 | BlankModule | 0 | Core |
| 36 | 2 | CUDA | 0 | Core |
| 37 | 2 | ChaosCore | 0 | Core |
| 38 | 2 | ChaosVehiclesCore | 0 | Core |
| 39 | 2 | GraphColor | 0 | Core |
| 40 | 2 | IPC | 0 | Core |
| 41 | 2 | InputDevice | 0 | Core |
| 42 | 2 | LauncherCheck | 0 | Core |
| 43 | 2 | LauncherPlatform | 0 | Core |
| 44 | 2 | MediaInfo | 0 | Core |
| 45 | 2 | MeshReductionInterface | 0 | Core |
| 46 | 2 | MessagingCommon | 0 | Core |
| 47 | 2 | NetCommon | 0 | Core |
| 48 | 2 | PosixShim | 0 | Core |
| 49 | 2 | SerializedRecorderInterface | 0 | Core |
| 50 | 2 | TextureFormatASTC | 0 | Core |
| 51 | 2 | UE4Game | 0 | Core |
| 52 | 2 | ViewportSnapping | 0 | Core |
| 53 | 3 | RHI | 48 | ApplicationCore, Core, GeForceNOWWrapper, TraceLog |
| 54 | 3 | DesktopPlatform | 27 | ApplicationCore, Core, Json |
| 55 | 3 | HTTP | 13 | Core, SSL, Sockets |
| 56 | 3 | AudioMixerCore | 5 | Core, SignalProcessing |
| 57 | 3 | PakFile | 4 | Core, RSA |
| 58 | 3 | TraceAnalysis | 2 | Cbor, Core, Sockets, TraceLog |
| 59 | 3 | DerivedDataCache | 1 | Core, Json, SSL |
| 60 | 3 | InstallBundleManager | 1 | Core, Json |
| 61 | 3 | Networking | 1 | Core, Sockets |
| 62 | 3 | CollectionManager | 0 | Core, DirectoryWatcher |
| 63 | 3 | HardwareSurvey | 0 | ApplicationCore, Core |
| 64 | 3 | Icmp | 0 | Core, Sockets |
| 65 | 3 | SynthBenchmark | 0 | ApplicationCore, Core |
| 66 | 3 | TextureCompressor | 0 | Core, ImageCore |
| 67 | 3 | TextureFormatDXT | 0 | Core, ImageCore |
| 68 | 3 | TextureFormatETC2 | 0 | Core, ImageCore |
| 69 | 3 | TextureFormatIntelISPCTexComp | 0 | Core, ImageCore |
| 70 | 3 | TextureFormatPVR | 0 | Core, ImageCore |
| 71 | 3 | TextureFormatUncompressed | 0 | Core, ImageCore |
| 72 | 4 | Projects | 20 | Core, DesktopPlatform, Json |
| 73 | 4 | AnalyticsET | 5 | Core, HTTP |
| 74 | 4 | AVEncoder | 2 | Core, RHI |
| 75 | 4 | HTTPServer | 2 | Core, HTTP, Sockets |
| 76 | 4 | PakFileUtilities | 2 | Core, Json, PakFile, RSA |
| 77 | 4 | WebSockets | 2 | Core, HTTP, SSL |
| 78 | 4 | LauncherServices | 1 | Core, DesktopPlatform, Json |
| 79 | 4 | TraceServices | 1 | Core, TraceAnalysis |
| 80 | 4 | AnalyticsSwrve | 0 | Analytics, Core, HTTP, Json |
| 81 | 4 | BackgroundHTTP | 0 | BackgroundHTTPFileHash, Core, HTTP |
| 82 | 4 | NullInstallBundleManager | 0 | Core, InstallBundleManager |
| 83 | 4 | SlackIntegrations | 0 | Core, HTTP |
| 84 | 5 | CoreUObject | 249 | Core, Json, Projects, TraceLog |
| 85 | 5 | RenderCore | 56 | ApplicationCore, Core, Json, PakFileUtilities, Projects, RHI, TraceLog |
| 86 | 5 | EditorAnalyticsSession | 1 | AnalyticsET, Core |
| 87 | 5 | PerfCounters | 1 | Core, HTTPServer |
| 88 | 5 | CrashReportCore | 0 | Analytics, AnalyticsET, Core, HTTP, Json, XmlParser |
| 89 | 5 | Stomp | 0 | Core, WebSockets |
| 90 | 5 | XMPP | 0 | Core, Json, WebSockets |
| 91 | 6 | InputCore | 110 | Core, CoreUObject |
| 92 | 6 | MeshDescription | 17 | Core, CoreUObject |
| 93 | 6 | JsonUtilities | 14 | Core, CoreUObject, Json |
| 94 | 6 | DeveloperSettings | 13 | Core, CoreUObject |
| 95 | 6 | EngineSettings | 9 | Core, CoreUObject |
| 96 | 6 | Chaos | 7 | Core, CoreUObject, TraceLog, Voronoi |
| 97 | 6 | ClothingSystemEditorInterface | 5 | Core, CoreUObject |
| 98 | 6 | ClothingSystemRuntimeInterface | 5 | Core, CoreUObject |
| 99 | 6 | NetCore | 5 | Core, CoreUObject, TraceLog |
| 100 | 6 | RawMesh | 5 | Core, CoreUObject |
| 101 | 6 | ShaderCompilerCommon | 5 | Core, RenderCore |
| 102 | 6 | ShaderPreprocessor | 5 | Core, RenderCore |
| 103 | 6 | AssetRegistry | 4 | Core, CoreUObject, Projects |
| 104 | 6 | AudioExtensions | 4 | AudioMixerCore, Core, CoreUObject, SignalProcessing |
| 105 | 6 | AutomationMessages | 4 | Core, CoreUObject |
| 106 | 6 | DirectLink | 4 | Core, CoreUObject |
| 107 | 6 | AudioPlatformConfiguration | 3 | Core, CoreUObject, UELibSampleRate |
| 108 | 6 | PropertyPath | 3 | Core, CoreUObject |
| 109 | 6 | EngineMessages | 2 | Core, CoreUObject |
| 110 | 6 | MessagingRpc | 2 | Core, CoreUObject |
| 111 | 6 | NetworkFile | 2 | Core, CoreUObject, Networking, Sockets |
| 112 | 6 | ProfilerMessages | 2 | Core, CoreUObject |
| 113 | 6 | ScriptDisassembler | 2 | Core, CoreUObject |
| 114 | 6 | UnrealEdMessages | 2 | Core, CoreUObject |
| 115 | 6 | BuildPatchServices | 1 | Core, CoreUObject, HTTP, Json |
| 116 | 6 | LiveLinkInterface | 1 | Core, CoreUObject |
| 117 | 6 | PIEPreviewDeviceSpecification | 1 | Core, CoreUObject |
| 118 | 6 | PortalServices | 1 | Core, CoreUObject |
| 119 | 6 | PropertyAccess | 1 | Core, CoreUObject |
| 120 | 6 | RigVM | 1 | Core, CoreUObject |
| 121 | 6 | Serialization | 1 | Cbor, Core, CoreUObject |
| 122 | 6 | SessionMessages | 1 | Core, CoreUObject |
| 123 | 6 | SwarmInterface | 1 | Core, CoreUObject |
| 124 | 6 | VectorVM | 1 | Core, CoreUObject |
| 125 | 6 | BlueprintRuntime | 0 | Core, CoreUObject |
| 126 | 6 | ChaosVehiclesEngine | 0 | Core, CoreUObject |
| 127 | 6 | ClientPilot | 0 | Core, CoreUObject |
| 128 | 6 | ExternalRpcRegistry | 0 | Core, CoreUObject, HTTPServer |
| 129 | 6 | ImageWrapper | 0 | Core, CoreUObject |
| 130 | 6 | LaunchDaemonMessages | 0 | Core, CoreUObject |
| 131 | 6 | LiveCoding | 0 | Core, CoreUObject |
| 132 | 6 | Messaging | 0 | Core, CoreUObject |
| 133 | 6 | NullDrv | 0 | Core, RHI, RenderCore |
| 134 | 6 | Settings | 0 | Core, CoreUObject |
| 135 | 6 | StageDataCore | 0 | Core, CoreUObject |
| 136 | 6 | TargetDeviceServices | 0 | Core, CoreUObject, DesktopPlatform |
| 137 | 7 | SlateCore | 154 | ApplicationCore, Core, CoreUObject, InputCore, TraceLog |
| 138 | 7 | PhysicsCore | 12 | Chaos, Core, CoreUObject, DeveloperSettings |
| 139 | 7 | StaticMeshDescription | 12 | Core, CoreUObject, MeshDescription, MeshUtilitiesCommon, RawMesh |
| 140 | 7 | PacketHandler | 2 | Core, CoreUObject, NetCore, ReliabilityHandlerComponent |
| 141 | 7 | AutomationController | 1 | AutomationMessages, Core, CoreUObject, JsonUtilities, UnrealEdMessages |
| 142 | 7 | IoStoreUtilities | 1 | AssetRegistry, Core, CoreUObject, Json, RSA |
| 143 | 7 | PortalMessages | 1 | Core, CoreUObject, MessagingRpc, PortalServices |
| 144 | 7 | ReliabilityHandlerComponent | 1 | Core, NetCore, PacketHandler |
| 145 | 7 | ScreenShotComparisonTools | 1 | AutomationMessages, Core, CoreUObject, Json, JsonUtilities |
| 146 | 7 | AnalyticsVisualEditing | 0 | Core, CoreUObject, DeveloperSettings |
| 147 | 7 | CookedIterativeFile | 0 | Core, NetworkFile, Sockets |
| 148 | 7 | LiveLinkMessageBusFramework | 0 | Core, CoreUObject, LiveLinkInterface |
| 149 | 7 | MetalShaderFormat | 0 | Core, FileUtilities, RenderCore, ShaderCompilerCommon, ShaderPreprocessor |
| 150 | 7 | PortalRpc | 0 | Core, CoreUObject, MessagingRpc |
| 151 | 7 | ProfilerClient | 0 | Core, CoreUObject, ProfilerMessages |
| 152 | 7 | ProfilerService | 0 | Core, CoreUObject, ProfilerMessages |
| 153 | 7 | SessionServices | 0 | Core, CoreUObject, EngineMessages, SessionMessages |
| 154 | 7 | ShaderFormatD3D | 0 | Core, RenderCore, ShaderCompilerCommon, ShaderPreprocessor |
| 155 | 7 | ShaderFormatOpenGL | 0 | Core, RenderCore, ShaderCompilerCommon, ShaderPreprocessor |
| 156 | 7 | ShaderFormatVectorVM | 0 | Core, ShaderCompilerCommon, ShaderPreprocessor, VectorVM |
| 157 | 7 | StreamingFile | 0 | Core, NetworkFile, Sockets |
| 158 | 7 | VulkanShaderFormat | 0 | Core, RenderCore, ShaderCompilerCommon, ShaderPreprocessor |
| 159 | 8 | Slate | 151 | ApplicationCore, Core, CoreUObject, InputCore, Json, SlateCore |
| 160 | 8 | DatasmithCore | 2 | Core, CoreUObject, DirectLink, Json, MeshDescription, RawMesh, StaticMeshDescription, XmlParser |
| 161 | 8 | ImageDownload | 0 | Core, HTTP, SlateCore |
| 162 | 8 | MeshDescriptionOperations | 0 | Core, MeshDescription, StaticMeshDescription |
| 163 | 8 | PhysXCooking | 0 | Core, PhysicsCore |
| 164 | 8 | PortalProxies | 0 | Core, CoreUObject, PortalMessages |
| 165 | 8 | QuadricMeshReduction | 0 | Core, MeshDescription, MeshUtilitiesCommon, StaticMeshDescription |
| 166 | 8 | StandaloneRenderer | 0 | Core, SlateCore |
| 167 | 9 | EditorStyle | 116 | Core, CoreUObject, DesktopPlatform, Slate, SlateCore |
| 168 | 9 | ToolMenus | 32 | ApplicationCore, Core, CoreUObject, Slate, SlateCore |
| 169 | 9 | AppFramework | 19 | ApplicationCore, Core, CoreUObject, InputCore, Slate, SlateCore |
| 170 | 9 | TargetPlatform | 12 | Core, DesktopPlatform, Projects, Slate, SlateCore |
| 171 | 9 | DesktopWidgets | 4 | Core, Slate, SlateCore |
| 172 | 9 | DatasmithExporter | 2 | Core, CoreUObject, DatasmithCore, DirectLink, MeshDescription, RawMesh, StaticMeshDescription |
| 173 | 9 | WidgetCarousel | 1 | Core, CoreUObject, Slate, SlateCore |
| 174 | 9 | AutomationDriver | 0 | ApplicationCore, Core, CoreUObject, InputCore, Slate, SlateCore |
| 175 | 9 | FriendsAndChat | 0 | Core, CoreUObject, Slate, SlateCore |
| 176 | 9 | ModuleUI | 0 | Core, CoreUObject, InputCore, Slate, SlateCore |
| 177 | 9 | SlateFileDialogs | 0 | Core, CoreUObject, InputCore, Slate, SlateCore |
| 178 | 9 | SourceCodeAccess | 0 | Core, CoreUObject, Slate |
| 179 | 9 | TreeMap | 0 | Core, InputCore, Slate, SlateCore, XmlParser |
| 180 | 9 | WebBrowser | 0 | ApplicationCore, CEF3Utils, Core, CoreUObject, HTTP, InputCore, Serialization, Slate, SlateCore |
| 181 | 10 | MaterialShaderQualitySettings | 4 | Core, CoreUObject, EditorStyle, InputCore, RHI, Slate, SlateCore |
| 182 | 10 | PinnedCommandList | 3 | Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore |
| 183 | 10 | AssetTagsEditor | 2 | Core, EditorStyle, Slate, SlateCore |
| 184 | 10 | ConfigEditor | 1 | Core, CoreUObject, EditorStyle, Slate, SlateCore |
| 185 | 10 | DatasmithExporterUI | 0 | Core, CoreUObject, DatasmithExporter, DirectLink, InputCore, Slate, SlateCore |
| 186 | 10 | DatasmithFacade | 0 | Core, DatasmithCore, DatasmithExporter, DirectLink |
| 187 | 10 | DeviceManager | 0 | Core, DesktopPlatform, EditorStyle, InputCore, Slate, SlateCore |
| 188 | 10 | GammaUI | 0 | Core, EditorStyle, InputCore, Slate, SlateCore |
| 189 | 10 | LocalizationService | 0 | Core, CoreUObject, EditorStyle, Slate, SlateCore |
| 190 | 10 | MessageLog | 0 | ApplicationCore, Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore |
| 191 | 10 | NewLevelDialog | 0 | Core, CoreUObject, EditorStyle, InputCore, RHI, RenderCore, Slate, SlateCore |
| 192 | 10 | OutputLog | 0 | Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore |
| 193 | 10 | PListEditor | 0 | Core, EditorStyle, InputCore, Slate, SlateCore, XmlParser |
| 194 | 10 | ProjectLauncher | 0 | ApplicationCore, Core, DesktopPlatform, EditorStyle, InputCore, Slate, SlateCore, TargetPlatform |
| 195 | 10 | SequencerWidgets | 0 | Core, EditorStyle, InputCore, Slate, SlateCore |
| 196 | 10 | SessionFrontend | 0 | ApplicationCore, Core, DesktopPlatform, EditorStyle, InputCore, Json, Slate, SlateCore |
| 197 | 10 | ToolMenusEditor | 0 | Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore, ToolMenus |
| 198 | 10 | Toolbox | 0 | AppFramework, Core, EditorStyle, Slate, SlateCore |
| 199 | 10 | WorkspaceMenuStructure | 0 | Core, EditorStyle, SlateCore |
| 200 | 11 | Engine | 184 | Analytics, AnalyticsET, AppFramework, ApplicationCore, AssetRegistry, AudioExtensions, AudioMixer, AudioPlatformConfiguration, Chaos, ClothingSystemEditorInterface, ClothingSystemRuntimeInterface, Core, CoreUObject, CrunchCompression, DeveloperSettings, EditorAnalyticsSession, EditorStyle, EngineMessages, EngineSettings, GameplayTags, ImageCore, InputCore, Json, Kismet, Landscape, MaterialShaderQualitySettings, MeshDescription, NetCore, PacketHandler, PakFile, PerfCounters, PhysicsCore, Projects, PropertyAccess, RHI, RawMesh, RenderCore, SignalProcessing, Slate, SlateCore, Sockets, StaticMeshDescription, TraceLog, UMG, UnrealEd |
| 201 | 11 | UnrealEd | 109 | AddContentDialog, AnalyticsET, AnimGraph, AppFramework, ApplicationCore, AssetRegistry, AssetTagsEditor, BlueprintGraph, CinematicCamera, ClothingSystemEditor, ClothingSystemRuntimeCommon, Core, CoreUObject, CurveEditor, DerivedDataCache, DesktopPlatform, DeveloperSettings, DirectoryWatcher, EditorInteractiveToolsFramework, EditorStyle, EditorSubsystem, EditorWidgets, Engine, EngineSettings, Foliage, GameProjectGeneration, GraphEditor, HTTP, HierarchicalLODUtilities, IESFile, ImageWriteQueue, InputCore, InteractiveToolsFramework, IoStoreUtilities, Json, JsonUtilities, Kismet, Landscape, LevelSequence, Localization, MaterialEditor, MaterialShaderQualitySettings, MaterialUtilities, MeshDescription, MovieScene, MovieSceneTracks, NavigationSystem, PIEPreviewDeviceProfileSelector, PakFile, PakFileUtilities, PhysicsCore, Projects, PropertyEditor, RHI, RenderCore, SandboxFile, ScriptDisassembler, SkeletalMeshUtilitiesCommon, Slate, SlateCore, SourceControl, StaticMeshDescription, StatsViewer, SwarmInterface, TargetPlatform, TimeManagement, ToolMenus, TraceLog, UMG, UnrealAudio, UnrealEdMessages, VREditor, ViewportInteraction |
| 202 | 11 | Kismet | 23 | AnimGraph, AppFramework, ApplicationCore, BlueprintGraph, BlueprintNativeCodeGen, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, EngineSettings, GraphEditor, InputCore, Json, JsonUtilities, KismetCompiler, KismetWidgets, PropertyEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl, ToolMenus, UMG, UnrealEd |
| 203 | 11 | PropertyEditor | 21 | ActorPickerMode, AppFramework, ApplicationCore, Core, CoreUObject, DesktopPlatform, EditorStyle, EditorWidgets, Engine, InputCore, PropertyPath, SceneDepthPickerMode, Slate, SlateCore, UnrealEd |
| 204 | 11 | BlueprintGraph | 19 | Core, CoreUObject, EditorStyle, EditorSubsystem, Engine, GraphEditor, InputCore, Kismet, KismetCompiler, KismetWidgets, PropertyEditor, Slate, SlateCore, ToolMenus, UnrealEd |
| 205 | 11 | GraphEditor | 18 | AppFramework, BlueprintGraph, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, InputCore, KismetWidgets, RHI, RenderCore, Slate, SlateCore, ToolMenus, UnrealEd |
| 206 | 11 | SourceControl | 13 | Core, CoreUObject, EditorStyle, Engine, Slate, SlateCore |
| 207 | 11 | Landscape | 12 | ApplicationCore, Core, CoreUObject, DeveloperSettings, Engine, Foliage, MaterialUtilities, MeshDescription, PhysicsCore, RHI, RenderCore, Renderer, Slate, SlateCore, UnrealEd |
| 208 | 11 | EditorWidgets | 11 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 209 | 11 | MovieScene | 11 | Core, CoreUObject, Engine |
| 210 | 11 | UMG | 10 | Core, CoreUObject, Engine, HTTP, InputCore, MovieScene, MovieSceneTracks, PropertyPath, RHI, RenderCore, Slate, SlateCore |
| 211 | 11 | KismetWidgets | 9 | BlueprintGraph, ClassViewer, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 212 | 11 | MovieSceneTracks | 9 | AnimGraphRuntime, AnimationCore, Core, CoreUObject, Engine, MovieScene, PropertyPath, SlateCore, UnrealEd |
| 213 | 11 | AnimGraph | 8 | AnimGraphRuntime, BlueprintGraph, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, GraphEditor, InputCore, KismetCompiler, KismetWidgets, PropertyEditor, Slate, SlateCore, ToolMenus, UnrealEd |
| 214 | 11 | KismetCompiler | 8 | BlueprintGraph, Core, CoreUObject, Engine, Kismet, ScriptDisassembler, UnrealEd |
| 215 | 11 | ClothingSystemRuntimeCommon | 7 | Chaos, ClothingSystemRuntimeInterface, Core, CoreUObject, Engine, Slate |
| 216 | 11 | Foliage | 7 | Core, CoreUObject, Engine, RenderCore |
| 217 | 11 | LevelSequence | 7 | Core, CoreUObject, DeveloperSettings, Engine, MediaAssets, MovieScene, MovieSceneTracks, UMG |
| 218 | 11 | ViewportInteraction | 7 | Core, CoreUObject, Engine, InputCore, LevelEditor, Slate, SlateCore, UnrealEd |
| 219 | 11 | AdvancedPreviewScene | 6 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 220 | 11 | AudioMixer | 6 | AudioExtensions, AudioMixerCore, AudioPlatformConfiguration, Core, CoreUObject, Engine, SignalProcessing, SoundFieldRendering |
| 221 | 11 | CurveEditor | 6 | ApplicationCore, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, TimeManagement, UnrealEd |
| 222 | 11 | TimeManagement | 6 | Core, CoreUObject, Engine, Slate, SlateCore |
| 223 | 11 | CinematicCamera | 5 | Core, CoreUObject, Engine |
| 224 | 11 | ContentBrowserData | 5 | Core, CoreUObject, EditorSubsystem, Engine, Projects, Slate, SlateCore, UnrealEd |
| 225 | 11 | EditorSubsystem | 5 | Core, CoreUObject, Engine |
| 226 | 11 | MaterialUtilities | 5 | Core, CoreUObject, Engine, Landscape, MaterialBaking, MeshDescription, RHI, RenderCore, UnrealEd |
| 227 | 11 | NavigationSystem | 5 | Core, CoreUObject, Engine, Navmesh, PhysicsCore, RHI, RenderCore, UnrealEd |
| 228 | 11 | VREditor | 5 | ApplicationCore, Core, CoreUObject, EditorStyle, Engine, HeadMountedDisplay, InputCore, LevelEditor, LevelSequence, Projects, Sequencer, Slate, SlateCore, UMG, UnrealEd, ViewportInteraction |
| 229 | 11 | AnimGraphRuntime | 4 | AnimationCore, Chaos, Core, CoreUObject, Engine, TraceLog |
| 230 | 11 | ImageWriteQueue | 4 | Core, CoreUObject, Engine, RHI, RenderCore |
| 231 | 11 | LevelEditor | 4 | ActorPickerMode, CommonMenuExtensions, Core, CoreUObject, DesktopPlatform, DeveloperSettings, EditorStyle, Engine, EngineSettings, Foliage, InputCore, Kismet, KismetWidgets, LevelSequence, Projects, PropertyEditor, RHI, RenderCore, Slate, SlateCore, SourceControl, SourceControlWindows, ToolMenus, UnrealEd |
| 232 | 11 | Localization | 4 | Core, CoreUObject, DesktopPlatform, Engine, Json, SourceControl |
| 233 | 11 | SharedSettingsWidgets | 4 | Core, EditorStyle, RHI, Slate, SlateCore, SourceControl |
| 234 | 11 | SkeletalMeshUtilitiesCommon | 4 | ClothingSystemRuntimeCommon, Core, CoreUObject, Engine, MeshUtilitiesCommon |
| 235 | 11 | SourceControlWindows | 4 | Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore, SourceControl, UnrealEd |
| 236 | 11 | ActorPickerMode | 3 | Core, CoreUObject, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 237 | 11 | AnimationCore | 3 | Core, CoreUObject, Engine |
| 238 | 11 | GameProjectGeneration | 3 | AddContentDialog, AppFramework, ApplicationCore, ClassViewer, Core, CoreUObject, DesktopPlatform, EditorStyle, EditorSubsystem, Engine, EngineSettings, HardwareTargeting, InputCore, Projects, Slate, SlateCore, UnrealEd |
| 239 | 11 | MaterialEditor | 3 | AdvancedPreviewScene, AppFramework, ApplicationCore, Core, CoreUObject, EditorStyle, Engine, GraphEditor, InputCore, MaterialUtilities, PropertyEditor, RHI, RenderCore, Slate, SlateCore, ToolMenus, UnrealEd |
| 240 | 11 | MovieSceneCapture | 3 | AVIWriter, AudioMixer, Core, CoreUObject, Engine, ImageWriteQueue, Json, JsonUtilities, RHI, RenderCore, Slate, SlateCore |
| 241 | 11 | MovieSceneTools | 3 | ActorPickerMode, AnimationCore, AppFramework, BlueprintGraph, CinematicCamera, Core, CoreUObject, CurveEditor, EditorStyle, EditorWidgets, Engine, GraphEditor, InputCore, Json, JsonUtilities, Kismet, KismetCompiler, LevelSequence, MovieScene, MovieSceneCapture, MovieSceneTracks, PropertyEditor, RHI, RenderCore, SequenceRecorder, Sequencer, Slate, SlateCore, ToolMenus, UnrealEd, XmlParser |
| 242 | 11 | Renderer | 3 | ApplicationCore, Core, CoreUObject, Engine, ImageWriteQueue, MaterialShaderQualitySettings, RHI, RenderCore |
| 243 | 11 | Sequencer | 3 | AppFramework, ApplicationCore, BlueprintGraph, CinematicCamera, ContentBrowser, Core, CoreUObject, CurveEditor, EditorStyle, Engine, GraphEditor, InputCore, LevelSequence, MovieScene, MovieSceneTools, MovieSceneTracks, Slate, SlateCore, TimeManagement, ToolMenus, UnrealEd, ViewportInteraction |
| 244 | 11 | AddContentDialog | 2 | ApplicationCore, Core, CoreUObject, EditorStyle, InputCore, Json, PakFile, Slate, SlateCore, UnrealEd, WidgetCarousel |
| 245 | 11 | AssetTools | 2 | ApplicationCore, Core, CoreUObject, DeveloperSettings, EditorStyle, Engine, Foliage, InputCore, Kismet, Landscape, MaterialEditor, PhysicsCore, Projects, Slate, SlateCore, SourceControl, ToolMenus, UnrealEd |
| 246 | 11 | ClassViewer | 2 | ContentBrowserData, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 247 | 11 | CommonMenuExtensions | 2 | Core, EditorStyle, Engine, Slate, SlateCore, ToolMenus, UnrealEd |
| 248 | 11 | GameplayTags | 2 | Core, CoreUObject, DeveloperSettings, Engine, Projects, Slate |
| 249 | 11 | HardwareTargeting | 2 | Core, CoreUObject, EditorStyle, Engine, EngineSettings, Slate, SlateCore, UnrealEd |
| 250 | 11 | HeadMountedDisplay | 2 | AugmentedReality, Core, CoreUObject, Engine, EngineSettings, InputCore, RHI, RenderCore, UnrealEd |
| 251 | 11 | InteractiveToolsFramework | 2 | Core, CoreUObject, Engine, InputCore, MeshDescription |
| 252 | 11 | MaterialBaking | 2 | Core, CoreUObject, EditorStyle, Engine, InputCore, MeshDescription, PropertyEditor, RHI, RenderCore, Slate, SlateCore, UnrealEd |
| 253 | 11 | MediaAssets | 2 | AudioMixer, Core, CoreUObject, Engine, MediaUtils, RHI, RenderCore, SignalProcessing |
| 254 | 11 | SequenceRecorder | 2 | CinematicCamera, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, InputCore, Kismet, LevelSequence, MovieScene, MovieSceneTracks, Slate, SlateCore, UnrealEd |
| 255 | 11 | AugmentedReality | 1 | Core, CoreUObject, Engine, MRMesh, RenderCore |
| 256 | 11 | BlueprintCompilerCppBackend | 1 | BlueprintGraph, Core, CoreUObject, Engine, KismetCompiler, MovieScene, UMG, UnrealEd |
| 257 | 11 | BlueprintNativeCodeGen | 1 | BlueprintCompilerCppBackend, Core, CoreUObject, DesktopPlatform, DesktopWidgets, EditorStyle, Engine, GameProjectGeneration, Json, JsonUtilities, Kismet, Projects, Slate, SlateCore, UnrealEd |
| 258 | 11 | ClothingSystemEditor | 1 | ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, ClothingSystemRuntimeNv, Core, CoreUObject, Engine, PhysicsCore, Slate, SlateCore, UnrealEd |
| 259 | 11 | ClothingSystemRuntimeNv | 1 | ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, Core, CoreUObject, Engine |
| 260 | 11 | ContentBrowser | 1 | AppFramework, ApplicationCore, AssetRegistry, AssetTagsEditor, AssetTools, ContentBrowserData, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, InputCore, Projects, Slate, SlateCore, SourceControlWindows, ToolMenus, UnrealEd |
| 261 | 11 | EditorInteractiveToolsFramework | 1 | Core, CoreUObject, Engine, InputCore, InteractiveToolsFramework, UnrealEd |
| 262 | 11 | HierarchicalLODUtilities | 1 | Core, CoreUObject, Engine, MeshDescription, Projects, StaticMeshDescription, UnrealEd |
| 263 | 11 | MRMesh | 1 | Core, CoreUObject, Engine, PhysicsCore, RHI, RenderCore |
| 264 | 11 | MediaUtils | 1 | Core, CoreUObject, ImageWriteQueue, Media |
| 265 | 11 | PIEPreviewDeviceProfileSelector | 1 | ApplicationCore, Core, CoreUObject, Engine, Json, JsonUtilities, MaterialShaderQualitySettings, PIEPreviewDeviceSpecification, RHI, Slate, SlateCore, UnrealEd |
| 266 | 11 | SceneDepthPickerMode | 1 | Core, CoreUObject, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 267 | 11 | SoundFieldRendering | 1 | AudioExtensions, AudioMixer, Core, Engine, SignalProcessing |
| 268 | 11 | StatsViewer | 1 | Core, CoreUObject, EditorStyle, Engine, Landscape, Slate, SlateCore, UnrealEd |
| 269 | 12 | Persona | 5 | AdvancedPreviewScene, AnimGraph, AnimGraphRuntime, AppFramework, ApplicationCore, BlueprintGraph, ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, CommonMenuExtensions, ContentBrowserData, Core, CoreUObject, CurveEditor, EditorStyle, EditorWidgets, Engine, GraphEditor, InputCore, Json, JsonUtilities, Kismet, KismetWidgets, PinnedCommandList, PropertyEditor, SkeletalMeshUtilitiesCommon, Slate, SlateCore, TimeManagement, ToolMenus, UnrealEd |
| 270 | 12 | GameplayTasks | 3 | Core, CoreUObject, Engine, NetCore |
| 271 | 12 | InternationalizationSettings | 3 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore |
| 272 | 12 | ChaosSolverEngine | 2 | Chaos, Core, CoreUObject, DeveloperSettings, Engine, PhysicsCore |
| 273 | 12 | DistCurveEditor | 2 | AppFramework, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 274 | 12 | LocalizationCommandletExecution | 2 | ApplicationCore, Core, CoreUObject, EditorStyle, Engine, InputCore, Localization, Slate, SlateCore, SourceControl, UnrealEd |
| 275 | 12 | MeshPaint | 2 | Core, CoreUObject, EditorStyle, Engine, InputCore, MeshDescription, RHI, RenderCore, Slate, SlateCore, StaticMeshDescription, UnrealEd, VREditor, ViewportInteraction |
| 276 | 12 | MoviePlayer | 2 | ApplicationCore, Core, CoreUObject, Engine, RHI, RenderCore, Slate, SlateCore |
| 277 | 12 | AnimationModifiers | 1 | Core, CoreUObject, EditorStyle, Engine, InputCore, Kismet, Slate, SlateCore, UnrealEd |
| 278 | 12 | AudioSettingsEditor | 1 | Core, CoreUObject, EditorStyle, Engine, InputCore, PropertyEditor, Slate, SlateCore |
| 279 | 12 | GameplayDebugger | 1 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 280 | 12 | GameplayMediaEncoder | 1 | AVEncoder, Core, CoreUObject, Engine, RHI, RenderCore, Slate |
| 281 | 12 | LandscapeEditorUtilities | 1 | Core, CoreUObject, Engine, Landscape |
| 282 | 12 | LocalFileNetworkReplayStreaming | 1 | Core, Engine, Json, NetworkReplayStreaming |
| 283 | 12 | Overlay | 1 | Core, CoreUObject, Engine |
| 284 | 12 | SlateReflector | 1 | ApplicationCore, Core, CoreUObject, EditorStyle, InputCore, Json, Slate, SlateCore, UnrealEd |
| 285 | 12 | TaskGraph | 1 | Core, EditorStyle, Engine, InputCore, Slate, SlateCore |
| 286 | 12 | WindowsTargetPlatform | 1 | AudioPlatformConfiguration, Core, CoreUObject, DesktopPlatform, Engine, RHI, TargetPlatform |
| 287 | 12 | AllDesktopTargetPlatform | 0 | Core, DesktopPlatform, Engine, TargetPlatform |
| 288 | 12 | AudioAnalyzer | 0 | Core, CoreUObject, Engine |
| 289 | 12 | AudioEditor | 0 | ApplicationCore, AudioExtensions, AudioMixer, Core, CoreUObject, EditorStyle, Engine, GameProjectGeneration, GraphEditor, InputCore, PropertyEditor, Slate, SlateCore, ToolMenus, UMG, UnrealEd |
| 290 | 12 | AudioFormatADPCM | 0 | Core, Engine |
| 291 | 12 | AudioFormatOgg | 0 | Core, Engine |
| 292 | 12 | AudioFormatOpus | 0 | Core, Engine |
| 293 | 12 | AudioMixerXAudio2 | 0 | AudioMixerCore, Core, Engine |
| 294 | 12 | AutomationWindow | 0 | ApplicationCore, Core, CoreUObject, EditorStyle, Engine, InputCore, Json, JsonUtilities, Slate, SlateCore, UnrealEd |
| 295 | 12 | AutomationWorker | 0 | AnalyticsET, AutomationMessages, Core, CoreUObject, Engine, JsonUtilities |
| 296 | 12 | CollisionAnalyzer | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore |
| 297 | 12 | CurveAssetEditor | 0 | Core, CoreUObject, CurveEditor, EditorStyle, Engine, Slate, SlateCore, UnrealEd |
| 298 | 12 | CurveTableEditor | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 299 | 12 | D3D11RHI | 0 | Core, Engine, RHI, RenderCore |
| 300 | 12 | D3D12RHI | 0 | Core, Engine, GeForceNOWWrapper, RHI, RenderCore |
| 301 | 12 | DataTableEditor | 0 | ApplicationCore, Core, CoreUObject, EditorStyle, Engine, InputCore, Json, Slate, SlateCore, UnrealEd |
| 302 | 12 | DeviceProfileEditor | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore |
| 303 | 12 | DeviceProfileServices | 0 | Core, CoreUObject, Engine |
| 304 | 12 | Documentation | 0 | Core, CoreUObject, EditorStyle, Engine, Slate, SlateCore, SourceControl, UnrealEd |
| 305 | 12 | EnvironmentLightingViewer | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 306 | 12 | ExternalImagePicker | 0 | Core, EditorStyle, PropertyEditor, Slate, SlateCore |
| 307 | 12 | EyeTracker | 0 | Core, CoreUObject, Engine |
| 308 | 12 | FontEditor | 0 | AppFramework, Core, CoreUObject, EditorStyle, Engine, InputCore, PropertyEditor, Slate, SlateCore, UnrealEd |
| 309 | 12 | GameMenuBuilder | 0 | Core, CoreUObject, Engine, InputCore, Slate, SlateCore |
| 310 | 12 | HierarchicalLODOutliner | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, ToolMenus, UnrealEd |
| 311 | 12 | HotReload | 0 | Core, CoreUObject, Engine, Projects, UnrealEd |
| 312 | 12 | HttpNetworkReplayStreaming | 0 | Core, Engine, HTTP, Json, NetworkReplayStreaming |
| 313 | 12 | InMemoryNetworkReplayStreaming | 0 | Core, Engine, Json, NetworkReplayStreaming |
| 314 | 12 | InputBindingEditor | 0 | Core, CoreUObject, DeveloperSettings, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 315 | 12 | IntroTutorials | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Kismet, Slate, SlateCore, ToolMenus, UnrealEd |
| 316 | 12 | Layers | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 317 | 12 | LogVisualizer | 0 | ApplicationCore, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 318 | 12 | MacClientTargetPlatform | 0 | Core, DesktopPlatform, Engine, TargetPlatform |
| 319 | 12 | MacNoEditorTargetPlatform | 0 | Core, DesktopPlatform, Engine, TargetPlatform |
| 320 | 12 | MacServerTargetPlatform | 0 | Core, DesktopPlatform, Engine, TargetPlatform |
| 321 | 12 | MacTargetPlatform | 0 | Core, CoreUObject, DesktopPlatform, Engine, TargetPlatform |
| 322 | 12 | Merge | 0 | Core, CoreUObject, EditorStyle, Engine, GraphEditor, Kismet, Slate, SlateCore, SourceControl, UnrealEd |
| 323 | 12 | MergeActors | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 324 | 12 | MeshBuilder | 0 | Core, CoreUObject, Engine, MeshBuilderCommon, MeshDescription, MeshUtilitiesCommon, RHI, RenderCore, SkeletalMeshUtilitiesCommon, StaticMeshDescription |
| 325 | 12 | MeshMergeUtilities | 0 | Core, CoreUObject, Engine, Landscape, MaterialBaking, MaterialUtilities, MeshDescription, RenderCore, Slate, SlateCore, StaticMeshDescription, ToolMenus, UnrealEd |
| 326 | 12 | MeshUtilities | 0 | Core, CoreUObject, EditorStyle, Engine, MeshBuilderCommon, MeshDescription, MeshUtilitiesCommon, RawMesh, Slate, SlateCore, StaticMeshDescription, ToolMenus, UnrealEd |
| 327 | 12 | MovieSceneCaptureDialog | 0 | Core, CoreUObject, Engine, Json, JsonUtilities, MovieSceneCapture, MovieSceneTools, Slate, SlateCore, UnrealEd |
| 328 | 12 | NetworkFileSystem | 0 | Core, CoreUObject, Engine, Projects, SandboxFile, Sockets |
| 329 | 12 | NonRealtimeAudioRenderer | 0 | AudioMixer, AudioMixerCore, Core, CoreUObject, Engine, SignalProcessing |
| 330 | 12 | NullNetworkReplayStreaming | 0 | Core, Engine, Json, NetworkReplayStreaming |
| 331 | 12 | OpenGLDrv | 0 | Core, Engine, RHI, RenderCore |
| 332 | 12 | PackagesDialog | 0 | Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore, UnrealEd |
| 333 | 12 | PixelInspectorModule | 0 | Core, CoreUObject, Engine, InputCore, RHI, RenderCore, Slate, SlateCore, UnrealEd |
| 334 | 12 | PlacementMode | 0 | ContentBrowserData, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 335 | 12 | PluginWarden | 0 | Core, CoreUObject, EditorStyle, Engine, Slate, SlateCore |
| 336 | 12 | PreLoadScreen | 0 | ApplicationCore, BuildPatchServices, Core, CoreUObject, Engine, Projects, RHI, RenderCore, Slate, SlateCore |
| 337 | 12 | Profiler | 0 | ApplicationCore, Core, EditorStyle, Engine, InputCore, Slate, SlateCore |
| 338 | 12 | ProjectTargetPlatformEditor | 0 | Core, DesktopPlatform, EditorStyle, Projects, Slate, SlateCore, UnrealEd |
| 339 | 12 | RigVMDeveloper | 0 | Core, CoreUObject, Engine, RigVM, UnrealEd |
| 340 | 12 | RuntimeAssetCache | 0 | Core, CoreUObject, Engine |
| 341 | 12 | SceneOutliner | 0 | ApplicationCore, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, ToolMenus, UnrealEd |
| 342 | 12 | ScreenShotComparison | 0 | AutomationMessages, Core, CoreUObject, DesktopWidgets, EditorStyle, InputCore, Json, JsonUtilities, ScreenShotComparisonTools, Slate, SlateCore, SourceControl |
| 343 | 12 | SequenceRecorderSections | 0 | Core, CoreUObject, Engine, MovieScene, MovieSceneTracks, SequenceRecorder |
| 344 | 12 | SettingsEditor | 0 | Core, CoreUObject, DeveloperSettings, EditorStyle, Engine, SharedSettingsWidgets, Slate, SlateCore |
| 345 | 12 | SlateNullRenderer | 0 | Core, CoreUObject, Engine, RHI, RenderCore, SlateCore |
| 346 | 12 | SlateRHIRenderer | 0 | Core, CoreUObject, Engine, RHI, RenderCore, Renderer, SlateCore |
| 347 | 12 | StaticMeshEditor | 0 | AdvancedPreviewScene, ApplicationCore, Core, CoreUObject, DesktopPlatform, DesktopWidgets, EditorStyle, Engine, InputCore, Json, JsonUtilities, PropertyEditor, RenderCore, Slate, SlateCore, UnrealEd |
| 348 | 12 | StringTableEditor | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 349 | 12 | StructViewer | 0 | ContentBrowserData, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 350 | 12 | TextureEditor | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, MediaAssets, RenderCore, Slate, SlateCore, UnrealEd |
| 351 | 12 | TimeManagementEditor | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, TimeManagement |
| 352 | 12 | TraceInsights | 0 | AppFramework, ApplicationCore, Cbor, Core, CoreUObject, EditorStyle, Engine, InputCore, Slate, SlateCore, Sockets, TraceAnalysis, TraceServices, XmlParser |
| 353 | 12 | UATHelper | 0 | Core, CoreUObject, Slate, SlateCore, UnrealEd |
| 354 | 12 | UndoHistory | 0 | ApplicationCore, Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore, UnrealEd |
| 355 | 12 | VirtualTexturingEditor | 0 | Core, CoreUObject, EditorStyle, Engine, Landscape, MaterialEditor, PropertyEditor, RHI, RenderCore, Renderer, Slate, SlateCore, UnrealEd |
| 356 | 12 | Voice | 0 | Core, Engine, SignalProcessing |
| 357 | 12 | VulkanRHI | 0 | ApplicationCore, BuildSettings, Core, Engine, RHI, RenderCore |
| 358 | 12 | WebBrowserTexture | 0 | Core, CoreUObject, Engine, RHI, RenderCore |
| 359 | 12 | WindowsClientTargetPlatform | 0 | Core, DesktopPlatform, Engine, RHI, TargetPlatform |
| 360 | 12 | WindowsNoEditorTargetPlatform | 0 | Core, DesktopPlatform, Engine, RHI, TargetPlatform |
| 361 | 12 | WindowsServerTargetPlatform | 0 | Core, DesktopPlatform, Engine, RHI, TargetPlatform |
| 362 | 12 | XAudio2 | 0 | AudioMixerCore, Core, CoreUObject, Engine |
| 363 | 13 | AIModule | 7 | Core, CoreUObject, Engine, GameplayDebugger, GameplayTags, GameplayTasks, NavigationSystem, Navmesh, RHI, RenderCore, UnrealEd |
| 364 | 13 | TranslationEditor | 2 | Core, CoreUObject, EditorStyle, InputCore, Json, Localization, LocalizationCommandletExecution, Slate, SlateCore, SourceControl, UnrealEd |
| 365 | 13 | FieldSystemEngine | 1 | Chaos, ChaosSolverEngine, Core, CoreUObject, Engine |
| 366 | 13 | LandscapeEditor | 1 | ApplicationCore, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, Foliage, InputCore, Landscape, LandscapeEditorUtilities, PropertyEditor, RenderCore, Slate, SlateCore, UnrealEd, VREditor, ViewportInteraction |
| 367 | 13 | SkeletonEditor | 1 | AnimGraph, ApplicationCore, BlueprintGraph, Core, CoreUObject, EditorStyle, Engine, InputCore, Kismet, Persona, PinnedCommandList, Slate, SlateCore, UnrealEd |
| 368 | 13 | AnimationBlueprintEditor | 0 | AnimGraph, BlueprintGraph, Core, CoreUObject, EditorStyle, Engine, GraphEditor, Kismet, KismetWidgets, Persona, Slate, SlateCore, UnrealEd |
| 369 | 13 | AnimationEditor | 0 | AnimGraph, Core, CoreUObject, EditorStyle, Engine, InputCore, Kismet, Persona, Slate, SlateCore, UnrealEd |
| 370 | 13 | Cascade | 0 | AppFramework, Core, CoreUObject, DistCurveEditor, EditorStyle, Engine, InputCore, Slate, SlateCore, UnrealEd |
| 371 | 13 | ClothPainter | 0 | AdvancedPreviewScene, ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, Core, CoreUObject, EditorStyle, Engine, InputCore, Kismet, MeshPaint, Slate, SlateCore, ToolMenus, UnrealEd |
| 372 | 13 | EditorSettingsViewer | 0 | BlueprintGraph, Core, CoreUObject, CurveEditor, EditorStyle, Engine, GraphEditor, InternationalizationSettings, Slate, SlateCore, ToolMenus, UnrealEd, VREditor |
| 373 | 13 | GameplayTasksEditor | 0 | BlueprintGraph, Core, CoreUObject, Engine, GameplayTasks, KismetCompiler, UnrealEd |
| 374 | 13 | Matinee | 0 | AppFramework, BlueprintGraph, Core, CoreUObject, DistCurveEditor, EditorStyle, Engine, InputCore, MovieSceneCapture, RenderCore, Slate, SlateCore, UnrealEd |
| 375 | 13 | MeshBoneReduction | 0 | AnimationModifiers, Core, CoreUObject, Engine, RenderCore |
| 376 | 13 | MeshPaintMode | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, MeshPaint, PropertyEditor, RHI, RenderCore, Slate, SlateCore, UnrealEd |
| 377 | 13 | OverlayEditor | 0 | Core, CoreUObject, Engine, Overlay, UnrealEd |
| 378 | 13 | RealtimeProfiler | 0 | Core, CoreUObject, EditorStyle, InputCore, Slate, SlateCore, TaskGraph |
| 379 | 13 | SaveGameNetworkReplayStreaming | 0 | Core, Engine, Json, LocalFileNetworkReplayStreaming, NetworkReplayStreaming |
| 380 | 13 | SkeletalMeshEditor | 0 | ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, Core, CoreUObject, EditorStyle, Engine, InputCore, Kismet, Persona, SkeletalMeshUtilitiesCommon, Slate, SlateCore, ToolMenus, UnrealEd |
| 381 | 13 | StreamingPauseRendering | 0 | Core, Engine, MoviePlayer, RHI, RenderCore, Slate, SlateCore |
| 382 | 13 | WindowsPlatformEditor | 0 | Core, CoreUObject, WindowsTargetPlatform |
| 383 | 13 | WindowsPlatformFeatures | 0 | AVEncoder, Core, Engine, GameplayMediaEncoder |
| 384 | 14 | AIGraph | 1 | AIModule, ApplicationCore, BlueprintGraph, Core, CoreUObject, EditorStyle, Engine, GraphEditor, InputCore, Slate, SlateCore, ToolMenus, UnrealEd |
| 385 | 14 | ComponentVisualizers | 1 | AIModule, Core, CoreUObject, EditorStyle, Engine, InputCore, LevelEditor, Slate, SlateCore, UnrealEd, ViewportInteraction |
| 386 | 14 | AITestSuite | 0 | AIModule, Core, CoreUObject, Engine, GameplayTasks |
| 387 | 14 | FunctionalTesting | 0 | AIModule, AutomationController, Core, CoreUObject, Engine, LevelEditor, NavigationSystem, RHI, RenderCore, Slate, SlateCore, UMG, UnrealEd |
| 388 | 14 | GeometryCollectionEngine | 0 | Chaos, ChaosSolverEngine, Core, CoreUObject, Engine, FieldSystemEngine, NetCore, PhysicsCore, RHI, RenderCore, UnrealEd |
| 389 | 14 | LocalizationDashboard | 0 | Core, CoreUObject, EditorStyle, Engine, InputCore, InternationalizationSettings, Localization, LocalizationCommandletExecution, SharedSettingsWidgets, Slate, SlateCore, ToolMenus, TranslationEditor, UnrealEd |
| 390 | 14 | MainFrame | 0 | ApplicationCore, Core, CoreUObject, DesktopPlatform, EditorStyle, Engine, EngineSettings, InputCore, LauncherServices, Projects, Slate, SlateCore, SourceControlWindows, TargetPlatform, ToolMenus, TranslationEditor, UnrealEd |
| 391 | 14 | PhysicsAssetEditor | 0 | AdvancedPreviewScene, AnimGraph, AnimGraphRuntime, Core, CoreUObject, EditorStyle, Engine, GraphEditor, InputCore, Kismet, Persona, PhysicsCore, PinnedCommandList, RenderCore, SkeletonEditor, Slate, SlateCore, ToolMenus, UnrealEd |
| 392 | 14 | ProjectSettingsViewer | 0 | AIModule, Core, CoreUObject, EditorStyle, Engine, EngineSettings, MoviePlayer, NavigationSystem, Slate, SlateCore, UnrealEd |
| 393 | 15 | DetailCustomizations | 2 | AIModule, AdvancedPreviewScene, AnimGraph, AppFramework, ApplicationCore, AudioSettingsEditor, BlueprintGraph, CinematicCamera, ComponentVisualizers, ConfigEditor, Core, CoreUObject, DesktopPlatform, DesktopWidgets, EditorStyle, EditorWidgets, Engine, GraphEditor, HardwareTargeting, HeadMountedDisplay, InputCore, InternationalizationSettings, Kismet, KismetWidgets, Landscape, LevelSequence, MovieScene, MovieSceneTracks, NavigationSystem, PhysicsCore, PropertyEditor, RenderCore, SharedSettingsWidgets, Slate, SlateCore, SourceControl, TimeManagement, ToolMenus, UnrealEd |
| 394 | 15 | BehaviorTreeEditor | 0 | AIGraph, AIModule, ApplicationCore, Core, CoreUObject, EditorStyle, Engine, GraphEditor, InputCore, Kismet, KismetWidgets, Slate, SlateCore, ToolMenus, UnrealEd |
| 395 | 16 | FoliageEdit | 1 | Core, CoreUObject, DetailCustomizations, EditorStyle, Engine, Foliage, InputCore, Landscape, PropertyEditor, Slate, SlateCore, UnrealEd, VREditor, ViewportInteraction |
| 396 | 16 | UMGEditor | 1 | ApplicationCore, BlueprintGraph, Core, CoreUObject, DetailCustomizations, DeveloperSettings, EditorStyle, Engine, GraphEditor, InputCore, Kismet, KismetCompiler, MovieScene, MovieSceneTools, MovieSceneTracks, PropertyEditor, RenderCore, Sequencer, Slate, SlateCore, SlateReflector, ToolMenus, UMG, UnrealEd |
| 397 | 17 | Blutility | 0 | AssetTools, BlueprintGraph, Core, CoreUObject, EditorStyle, EditorSubsystem, Engine, Kismet, KismetCompiler, Slate, SlateCore, ToolMenus, UMG, UMGEditor, UnrealEd |
| 398 | 17 | WorldBrowser | 0 | AppFramework, ApplicationCore, Core, CoreUObject, EditorStyle, Engine, Foliage, FoliageEdit, GraphEditor, InputCore, Json, Landscape, LandscapeEditor, MaterialUtilities, MeshDescription, PropertyEditor, RHI, RenderCore, Slate, SlateCore, SourceControlWindows, StaticMeshDescription, ToolMenus, UnrealEd |
