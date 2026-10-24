# UE 4.27 core module surface

Built by `tools/study-order/module_surface.py` from REA procedure-name searches for `::` (`snapshots/names-ue4.27`), in study order. Imported names are left out, so each row is the module's own named procedures; a name without `::` (a free function outside any class or namespace) is not counted. Top scopes are the full class or namespace path before the last `::`, with their procedure count.

| # | Module | Named procedures | Scopes | Top scopes |
|---|---|---|---|---|
| 1 | TraceLog | 22 | 4 | Trace 12, Trace::Private 7, Trace::FChannel 2, Trace::Private::FEventNode 1 |

Not yet searched: 397 modules.
