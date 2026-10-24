# UE 4.27 core module surface

Built by `tools/study-order/module_surface.py` from REA procedure-name searches for `::` (`snapshots/names-ue4.27`), in study order. Imported names are left out, so each row is the module's own named procedures; a name without `::` (a free function outside any class or namespace) is not counted. Top scopes are the full class or namespace path before the last `::`, with their procedure count.

| # | Module | Named procedures | Scopes | Top scopes |
|---|---|---|---|---|
| 1 | TraceLog | 22 | 4 | Trace 12, Trace::Private 7, Trace::FChannel 2, Trace::Private::FEventNode 1 |
| 2 | BuildSettings | 7 | 1 | BuildSettings 7 |
| 3 | UELibrary | 0 | 0 |  |
| 4 | Core | 5545 | 565 | FGenericPlatformMisc 189, FArchiveState 101, FString 101, FPaths 100, FGenericPlatformProcess 80, FWindowsPlatformMisc 71, FApp 70, FConfigCacheIni 70 |
| 5 | ApplicationCore | 276 | 18 | FWindowsApplication 61, FWindowsWindow 55, FGenericPlatformApplicationMisc 39, FGenericWindow 39, FWindowsPlatformApplicationMisc 19, FWindowsConsoleOutputDevice 10, FTaskbarList 8, FGenericPlatformSplash 7 |
| 6 | Json | 84 | 9 | FJsonObject 24, FJsonValue 17, FJsonValueString 8, FJsonValueBoolean 7, FJsonValueNumber 7, FJsonValueNumberString 7, FJsonValueArray 5, FJsonValueObject 5 |
| 7 | Sockets | 84 | 11 | ISocketSubsystem 27, FSocket 14, FInternetAddr 10, FServerTOC 7, FNFSMessageHeader 5, FRecvMulti 5, FSimpleAbstractSocket_FMultichannelTCPSocket 5, FSimpleAbstractSocket_FSocket 5 |
| 8 | SignalProcessing | 983 | 105 | Audio 73, Audio::IOscBase 35, Audio::FGranularSynth 34, Audio::FDynamicsProcessor 32, Audio::FEnvelope 27, Audio::FAmp 21, Audio::FVolumeFader 20, Audio::FEventQuantizer 19 |
| 9 | ImageCore | 5 | 1 | FImage 5 |
| 10 | XmlParser | 36 | 4 | FXmlFile 16, FXmlNode 14, FXmlAttribute 5, FFastXml 1 |
| 11 | MeshUtilitiesCommon | 47 | 3 | FAllocator2D 31, FLayoutUV 8, FOverlappingCorners 8 |
| 12 | NetworkReplayStreaming | 10 | 2 | FNetworkReplayStreaming 5, INetworkReplayStreamer 5 |
| 13 | Analytics | 0 | 0 |  |
| 14 | Cbor | 22 | 2 | FCborReader 12, FCborWriter 10 |
| 15 | RSA | 9 | 1 | FRSA 9 |
| 16 | SSL | 15 | 5 | FSslManager 7, ISslManager 3, switchD_180126140 3, FSslCertificateDelegates 1, FSslModule 1 |
| 17 | DirectoryWatcher | 32 | 3 | DirectoryWatcher::FFileCache 28, DirectoryWatcher::FMatchRules 3, DirectoryWatcher::FFileCacheCustomVersion 1 |
| 18 | GeForceNOWWrapper | 32 | 1 | GeForceNOWWrapper 32 |
| 19 | MeshBuilderCommon | 4 | 3 | BuildOptimizationThirdParty::NvTriStripHelper 2, BuildOptimizationThirdParty 1, std::exception 1 |
| 20 | Navmesh | 376 | 22 | dtNavMesh 63, dtCrowd 58, dtNavMeshQuery 50, dtTileCache 34, dtQueryFilter 30, dtPathCorridor 29, dtObstacleAvoidanceQuery 19, rcContext 18 |
| 21 | SandboxFile | 51 | 1 | FSandboxPlatformFile 51 |
| 22 | AVIWriter | 18 | 11 | CAMThread 3, CBasePin 3, FAVIWriter 3, CBaseInputPin 2, CBaseList 1, CBaseMediaFilter 1, CDynamicOutputPin 1, CMediaSample 1 |
| 23 | BackgroundHTTPFileHash | 19 | 1 | FBackgroundHttpFileHashHelper 19 |
| 24 | CEF3Utils | 2 | 1 | CEF3Utils 2 |
| 25 | CrunchCompression | 6 | 2 | CrunchCompression 5, FID_conflict:~vector<CHN*___ptr64,std 1 |
| 26 | FileUtilities | 7 | 1 | FZipArchiveWriter 7 |
| 27 | IESFile | 10 | 1 | FIESConverter 10 |
| 28 | Media | 1 | 1 | MediaTextureSampleFormat 1 |
| 29 | UELibSampleRate | 0 | 0 |  |
| 30 | UnrealAudio | 57 | 8 | UAudio::IUnrealAudioModule 18, UAudio 12, UAudio::IUnrealAudioDeviceModule 8, UAudio::IVoiceListener 6, UAudio::IIntermediateBuffer 4, UAudio::IEmitter 3, UAudio::ISoundFile 3, UAudio::IVoice 3 |
| 31 | Voronoi | 8 | 3 | FVoronoiDiagram 6, std::_Uninitialized_value_construct_n<std 1, std::exception 1 |
| 32 | Advertising | 0 | 0 |  |
| 33 | AudioCaptureCore | 29 | 2 | Audio::FAudioCapture 18, Audio::FAudioCaptureSynth 11 |
| 34 | AudioCaptureRtAudio | 53 | 4 | RtAudio 24, RtApi 22, RtAudioError 6, std::exception 1 |
| 35 | BlankModule | 0 | 0 |  |
| 36 | CUDA | 13 | 1 | FCUDAModule 13 |
| 37 | ChaosCore | 5 | 1 | FChaosCoreEngineModule 5 |
| 38 | ChaosVehiclesCore | 219 | 41 | Chaos::FSimpleWheelSim 36, Chaos::FSimpleTransmissionSim 17, Chaos::FSimpleSuspensionSim 16, Chaos::FAerofoil 14, Chaos::FSimpleEngineSim 11, Chaos::FSimpleThrustSim 11, Chaos::FPerformanceMeasure 10, Chaos::FTimeAndDistanceMeasure 7 |
| 39 | GraphColor | 0 | 0 |  |
| 40 | IPC | 0 | 0 |  |
| 41 | InputDevice | 0 | 0 |  |
| 42 | LauncherCheck | 0 | 0 |  |
| 43 | LauncherPlatform | 0 | 0 |  |
| 44 | MediaInfo | 0 | 0 |  |
| 45 | MeshReductionInterface | 0 | 0 |  |
| 46 | MessagingCommon | 0 | 0 |  |
| 47 | NetCommon | 0 | 0 |  |
| 48 | PosixShim | 0 | 0 |  |
| 49 | SerializedRecorderInterface | 3 | 1 | ISerializedRecorder 3 |
| 50 | TextureFormatASTC | 0 | 0 |  |
| 51 | UE4Game | 0 | 0 |  |
| 52 | ViewportSnapping | 0 | 0 |  |
| 53 | RHI | 907 | 162 | FDynamicRHI 133, FRHICommandListImmediate 128, FGenericDataDrivenShaderPlatformInfo 71, FRHICommandList 67, FRHICommandListBase 50, FRHIComputeCommandList 41, FPipelineFileCache 27, FRHITexture 27 |
| 54 | DesktopPlatform | 15 | 2 | PlatformInfo 9, FTargetReceipt 6 |
| 55 | HTTP | 176 | 17 | FWinHttpConnectionHttp 41, FHttpManager 23, FGenericPlatformHttp 21, FWinHttpErrorHelper 15, FHttpRequestImpl 12, FWinHttpHttpManager 10, FWindowsPlatformHttp 9, switchD_180107c6a 8 |
| 56 | AudioMixerCore | 65 | 7 | Audio::IAudioMixerPlatformInterface 35, Audio::IAudioMixerDeviceChangedLister 10, Audio::FOutputBuffer 8, Audio::FAudioRenderTimeAnalysis 4, Audio::FMixerNullCallback 3, FAudioPlatformSettings 3, Audio::IAudioMixer 2 |
| 57 | PakFile | 219 | 9 | FPakPlatformFile 94, FPakFile 74, FPakFileHandle<FPakCompressedReaderPolicy<FPakNoEncryption>_> 10, FPakFileHandle<FPakCompressedReaderPolicy<FPakSimpleEncryption>_> 10, FPakFileHandle<FPakReaderPolicy<FPakNoEncryption>_> 10, FPakFileHandle<FPakReaderPolicy<FPakSimpleEncryption>_> 10, FPakReaderPolicy<FPakNoEncryption> 4, FPakReaderPolicy<FPakSimpleEncryption> 4 |
| 58 | TraceAnalysis | 95 | 17 | Trace::FStoreClient 14, Trace::FControlClient 11, Trace::IAnalyzer::FEventData 8, Trace::IAnalyzer 8, Trace::FAnalysisProcessor 7, Trace::IAnalyzer::FEventTypeInfo 6, Trace::IAnalyzer::FThreadInfo 6, Trace::FAnalysisContext 5 |
| 59 | DerivedDataCache | 28 | 4 | FDDCCleanup 16, switchD_18010c92a 8, switchD_180109e9b 3, `protected:_void___cdecl_CWinApp::UpdatePrinterSelection(int)___ptr64'::__l1 1 |
| 60 | InstallBundleManager | 203 | 22 | InstallBundleUtil::PersistentStats::FPersistentStatContainerBase 38, InstallBundleUtil::PersistentStats::FPersistentStatsBase 25, IInstallBundleManager 23, FInstallBundleCache 18, FInstallBundleCombinedProgressTracker 14, InstallBundleUtil::PersistentStats::FSessionPersistentStats 8, InstallBundleUtil 7, InstallBundleUtil::FContentRequestStatsMap 7 |
| 61 | Networking | 11 | 5 | FIPv4Endpoint 4, FIPv4Address 2, FIPv4Subnet 2, FIPv4SubnetMask 2, FSteamEndpoint 1 |
| 62 | CollectionManager | 0 | 0 |  |
| 63 | HardwareSurvey | 0 | 0 |  |
| 64 | Icmp | 5 | 2 | FUDPPing 3, FIcmp 2 |
| 65 | SynthBenchmark | 0 | 0 |  |
| 66 | TextureCompressor | 4 | 1 | ITextureCompressorModule 4 |
| 67 | TextureFormatDXT | 0 | 0 |  |
| 68 | TextureFormatETC2 | 0 | 0 |  |
| 69 | TextureFormatIntelISPCTexComp | 0 | 0 |  |
| 70 | TextureFormatPVR | 0 | 0 |  |
| 71 | TextureFormatUncompressed | 0 | 0 |  |
| 72 | Projects | 93 | 14 | FProjectDescriptor 19, FModuleDescriptor 15, FPluginReferenceDescriptor 14, FLocalizationTargetDescriptor 11, FPluginDescriptor 10, FCustomBuildSteps 7, FPluginManifest 5, FPluginManifestEntry 3 |
| 73 | AnalyticsET | 23 | 2 | FAnalyticsProviderETEventCache 16, FAnalyticsET 7 |
| 74 | AVEncoder | 103 | 11 | AVEncoder::FVideoEncoderInputFrame 20, AVEncoder::FIMFSampleWrapper 15, AVEncoder::FVideoEncoder 15, AVEncoder::FVideoEncoderFactory 12, AVEncoder::FVideoEncoderInput 11, AVEncoder::FVideoDecoderFactory 9, AVEncoder::FAudioEncoderFactory 7, AVEncoder::FAudioEncoder 5 |
| 75 | HTTPServer | 18 | 4 | FHttpPath 8, FHttpServerModule 6, FHttpServerResponse 3, `private:_class_money_get<char,class_std::istreambuf_iterator<char,struct_std::char_traits<char>_>_>::basic_string<char,std::char_traits<char>,std::allocator<char>_>___cdecl_std::money_get<char,std::istreambuf_iterator<char,std::char_traits<char>_>_>::_Getmfld(money_get<char,class_std::istreambuf_iterator<char,struct_std::char_traits<char>_>_>::istreambuf_iterator<char,std::char_traits<char>_>&___ptr64,money_get<char,class_std::istreambuf_iterator<char,struct_std::char_traits<char>_>_>::istreambuf_iterator<char,std::char_traits<char>_>&___ptr64,bool,money_get<char,class_std::istreambuf_iterator<char,struct_std::char_traits<char>_>_>::ios_base&___ptr64)const___ptr64'::__l1 1 |
| 76 | PakFileUtilities | 4 | 2 | FPakOrderMap 3, `public:_virtual_int___cdecl_CMFCToolBar::SetButtons(unsigned_int_const*___ptr64,int,int)___ptr64'::__l1 1 |
| 77 | WebSockets | 11 | 2 | FWebSocketsModule 8, switchD_18009d480 3 |
| 78 | LauncherServices | 0 | 0 |  |
| 79 | TraceServices | 16 | 2 | Trace 15, `protected:_void___cdecl_CWinApp::UpdatePrinterSelection(int)___ptr64'::__l1 1 |
| 80 | AnalyticsSwrve | 0 | 0 |  |
| 81 | BackgroundHTTP | 54 | 9 | FBackgroundHttpRequestImpl 21, FBackgroundHttpNotificationObject 6, FGenericPlatformBackgroundHttp 6, FGenericPlatformBackgroundHttpRequest 5, TSharedFromThis<FBackgroundHttpNotificationObject,1> 5, FBackgroundHttpModule 3, FGenericPlatformBackgroundHttpManager 3, IBackgroundHttpResponse 3 |
| 82 | NullInstallBundleManager | 0 | 0 |  |
| 83 | SlackIntegrations | 0 | 0 |  |
| 84 | CoreUObject | 4494 | 373 | UObject 252, UClass 110, FProperty 88, TArray<FArchiveDiffInfo,TSizedDefaultAllocator<32>_> 82, FBulkDataBase 68, UPackage 67, FField 66, UEnum 65 |
| 85 | RenderCore | 1351 | 236 | FRDGBuilder 45, FShaderType 43, FShaderPipelineCache 40, FRenderTargetPool 34, FShaderMapContent 32, FShader 31, FRDGPass 30, FGlobalShaderMap 23 |
| 86 | EditorAnalyticsSession | 25 | 2 | FEditorAnalyticsSession 18, FEditorSessionSummarySender 7 |
| 87 | PerfCounters | 8 | 3 | IPerfCounters 6, IPerfCounters::Histograms 1, IPerfCountersModule 1 |
| 88 | CrashReportCore | 1 | 1 | `protected:_void___cdecl_CFrameImpl::LoadTearOffMenus(void)___ptr64'::__l1 1 |
| 89 | Stomp | 7 | 1 | FStompModule 7 |
| 90 | XMPP | 34 | 3 | FXmppModule 17, FXmppUserJid 14, switchD_18017d120 3 |
| 91 | InputCore | 95 | 9 | FKey 35, FKeyDetails 25, EKeys 16, FInputKeyManager 7, FGenericPlatformInput 6, FWindowsPlatformInput 3, StaticEnum<EConsoleForGamepadLabels 1, StaticEnum<ETouchIndex 1 |
| 92 | MeshDescription | 352 | 12 | UMeshDescriptionBase 200, FMeshDescription 119, UDEPRECATED_MeshDescription 12, FMeshDescriptionBulkData 10, FMeshAttributes 4, FEdgeID 1, FElementID 1, FPolygonGroupID 1 |
| 93 | JsonUtilities | 23 | 2 | FJsonObjectConverter 13, FJsonObjectWrapper 10 |
| 94 | DeveloperSettings | 22 | 1 | UDeveloperSettings 22 |
| 95 | EngineSettings | 108 | 11 | UGameMapsSettings 32, UConsoleSettings 12, UGameNetworkManagerSettings 12, UGameSessionSettings 12, UGeneralEngineSettings 12, UGeneralProjectSettings 12, UHudSettings 12, FAutoCompleteCommand 1 |
| 96 | Chaos | 3378 | 403 | Chaos::FJointConstraint 129, Chaos::FPBDRigidsSolver 77, Chaos::FPBDJointConstraints 63, Chaos::TPBDRigidParticle<float,3> 60, Chaos::FConvex 58, Chaos::FPBDEvolution 53, Chaos::TGeometryParticle<float,3> 52, Chaos::FGenericParticleHandleHandleImp 50 |
| 97 | ClothingSystemEditorInterface | 27 | 3 | UClothingAssetFactoryBase 18, FClothingSystemEditorInterfaceModule 7, IClothingAssetFactoryProvider 2 |
| 98 | ClothingSystemRuntimeInterface | 170 | 17 | UClothingSimulationInteractor 42, UClothingAssetBase 23, UClothingSimulationFactory 19, IClothingSimulation 15, UClothPhysicalMeshDataBase_Legacy 14, UClothConfigBase 12, UClothingInteractor 12, UDEPRECATED_ClothSharedSimConfigBase 11 |
| 99 | NetCore | 102 | 11 | FDDoSDetection 29, FNetTrace 24, FPacketAudit 15, FNetAnalyticsAggregator 8, FDDoSStateConfig 5, FNetAnalyticsData 5, TSharedFromThis<FNetAnalyticsData,0> 5, UE4PushModelPrivate 5 |
| 100 | RawMesh | 12 | 2 | FRawMeshBulkData 8, FRawMesh 4 |
| 101 | ShaderCompilerCommon | 46 | 10 | CrossCompiler::FShaderConductorContext 15, CrossCompiler::FHlslccHeader 7, FShaderParameterParser 6, CrossCompiler 4, CrossCompiler::FShaderConductorTarget 3, FDxcModuleWrapper 3, FShaderConductorModuleWrapper 3, CrossCompiler::FShaderConductorOptions 2 |
| 102 | ShaderPreprocessor | 0 | 0 |  |
| 103 | AssetRegistry | 54 | 6 | FAssetRegistryState 44, UAssetRegistry 3, UAssetRegistryHelpers::FTemporaryCachingModeScope 3, UE::AssetRegistry 2, FAssetRegistryDependencyOptions 1, FTagAndValue 1 |
| 104 | AudioExtensions | 247 | 25 | USoundfieldEffectBase 18, IAudioEndpoint 17, IAudioModulation 15, ISoundfieldEndpoint 15, IAudioEndpointFactory 14, ISoundfieldEndpointFactory 14, ISoundfieldFactory 14, USoundModulatorBase 14 |
| 105 | AutomationMessages | 21 | 21 | FAutomationScreenshotMetadata 1, FAutomationWorkerFindWorkers 1, FAutomationWorkerFindWorkersResponse 1, FAutomationWorkerImageComparisonResults 1, FAutomationWorkerNextNetworkCommandReply 1, FAutomationWorkerPerformanceDataRequest 1, FAutomationWorkerPerformanceDataResponse 1, FAutomationWorkerPing 1 |
| 106 | DirectLink | 93 | 21 | DirectLink::ISceneGraphNode 15, DirectLink::FEndpoint 14, DirectLink::FElementSnapshot 10, DirectLink::FParameterStore 9, DirectLink::FParameterStoreSnapshot 8, DirectLink::FSceneGraphSharedState 6, DirectLink 5, DirectLink::FReferenceSnapshot 5 |
| 107 | AudioPlatformConfiguration | 13 | 4 | Audio::FResampler 6, FPlatformRuntimeAudioCompressionOverrides 4, Audio 2, FPlatformAudioCookOverrides 1 |
| 108 | PropertyPath | 48 | 4 | FCachedPropertyPath 29, FPropertyPathSegment 11, PropertyPathHelpers 6, PropertyPathHelpersInternal 2 |
| 109 | EngineMessages | 7 | 7 | FEngineServiceAuthDeny 1, FEngineServiceAuthGrant 1, FEngineServiceExecuteCommand 1, FEngineServiceNotification 1, FEngineServicePing 1, FEngineServicePong 1, FEngineServiceTerminate 1 |
| 110 | MessagingRpc | 18 | 5 | FMessageRpcServer 14, FMessageRpcCancel 1, FMessageRpcProgress 1, FMessageRpcUnhandled 1, FRpcMessage 1 |
| 111 | NetworkFile | 58 | 1 | FNetworkPlatformFile 58 |
| 112 | ProfilerMessages | 11 | 11 | FProfilerServiceAuthorize 1, FProfilerServiceCapture 1, FProfilerServiceData2 1, FProfilerServiceFileChunk 1, FProfilerServicePing 1, FProfilerServicePong 1, FProfilerServicePreview 1, FProfilerServicePreviewAck 1 |
| 113 | ScriptDisassembler | 3 | 1 | FKismetBytecodeDisassembler 3 |
| 114 | UnrealEdMessages | 2 | 2 | FAssetEditorRequestOpenAsset 1, FFileServerReady 1 |
| 115 | BuildPatchServices | 63 | 19 | BuildPatchServices::FInstallerAction 18, BuildPatchServices 7, FBuildPatchServices 6, BuildPatchServices::FBuildPatchServicesInitSettings 3, BuildPatchServices::FChunkBuildConfiguration 3, BuildPatchServices::FChunkDeltaOptimiserConfiguration 3, BuildPatchServices::FCompactifyConfiguration 3, BuildPatchServices::FDiffManifestsConfiguration 3 |
| 116 | LiveLinkInterface | 417 | 63 | ULiveLinkVirtualSubject 41, ULiveLinkAnimationRole 18, ULiveLinkRole 18, ULiveLinkSourceFactory 18, ULiveLinkBasicRole 17, ULiveLinkCameraRole 16, ULiveLinkLightRole 16, ULiveLinkTransformRole 16 |
| 117 | PIEPreviewDeviceSpecification | 18 | 8 | UPIEPreviewDeviceSpecification 11, FPIEAndroidDeviceProperties 1, FPIEBezelProperties 1, FPIEIOSDeviceProperties 1, FPIEPreviewDeviceBezelViewportRect 1, FPIEPreviewDeviceSpecifications 1, FPIERHIOverrideState 1, FPIESwitchDeviceProperties 1 |
| 118 | PortalServices | 2 | 2 | FPortalUserDetails 1, FPortalUserIsEntitledToItemResult 1 |
| 119 | PropertyAccess | 21 | 11 | PropertyAccess 5, UPropertyAccess 3, UPropertyEventBroadcaster 3, UPropertyEventSubscriber 3, FPropertyAccessCopy 1, FPropertyAccessCopyBatch 1, FPropertyAccessIndirection 1, FPropertyAccessIndirectionChain 1 |
| 120 | RigVM | 396 | 30 | URigVM 92, FRigVMMemoryContainer 47, FRigVMByteCode 42, FRigVMRegisterOffset 21, FRigVMPrototype 18, FRigVMSlice 18, FRigVMStruct 18, FRigVMParameter 17 |
| 121 | Serialization | 58 | 15 | FJsonStructDeserializerBackend 13, FCborStructDeserializerBackend 11, FJsonStructSerializerBackend 11, FCborStructSerializerBackend 10, FStructDeserializer 2, FStructSerializer 2, FStructSerializerArrayTestStruct 1, FStructSerializerBooleanTestStruct 1 |

Not yet searched: 277 modules.
