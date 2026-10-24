# Content Browser

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine?application_version=4.27

- Browses all assets in the game, saved or unsaved. [docs]
- Search box matches Name, Path, Tags or Type; a '-' prefix excludes a token. A Filters button filters by asset type and other criteria. [docs]
- Collections (local, private, shared) organise assets without checking packages out of source control. [docs]
- Shows assets that may contain problems; Migrate moves assets with all their dependencies to other content folders. [docs]
- Up to four Content Browser instances can be open at once; docked lower left by default, re-dockable or floating. [docs]
- Subtopics in the docs: sources panel, folders, Developers folder, source control, Replace References, Reference Viewer. [docs]

## For Brown Marco Creator

Kept: text and type filters with exclusion, collections, multiple dockable instances, migrate with dependencies, a reference viewer. Changed: entries are source files on disk with sidecars ([ADR 0003](../../adr/0003-source-assets-no-container.md), [ADR 0010](../../adr/0010-asset-cache-and-sidecars.md)), not packages.
