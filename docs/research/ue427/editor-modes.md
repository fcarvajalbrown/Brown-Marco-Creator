# Level Editor modes

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine?application_version=4.27

- The Level Editor switches between modes from a Modes dropdown: Select (Shift+1), Landscape (Shift+2), Foliage (Shift+3), Brush Editing (Shift+4), Mesh Paint (Shift+5), Fracture (Shift+6). [docs]
- Each mode brings its own panel, such as the Landscape panel. [docs]

## For Brown Marco Creator

[ADR 0005](../../adr/0005-single-editor-mode.md) folds all of these into one mode as tools. Brush Editing (BSP) and Fracture are not on the kept list in ADR 0002; they go to the cut-list review.
