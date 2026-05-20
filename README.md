# MeasureIt X

A modernized fork of the classic **MeasureIt** add-on for Blender, focused on a cleaner, more streamlined workflow and proper integration with the 3D viewport.

> Original add-on by **Antonio Vazquez (antonioya)**. All credit for the foundation goes to the original author and the Blender community.

## What's different in MeasureIt X

- **Lives in 3D space, not screen space.** Measurements are drawn as real 3D overlays, so they behave correctly with camera movement, perspective, and depth — no more flat, screen-glued labels that ignore your scene.
- **Lean and focused UI.** Panels and options have been simplified to keep the workflow fast and uncluttered. Less noise, more measuring.
- **Built for Blender 5.x.** Packaged as a modern Blender extension (`blender_manifest.toml`) and updated for the current API.
- **Extra utilities.** Includes a *Sum Edge Lengths* operator in the Edit Mesh > Edges menu for quickly totaling selected edge lengths.

## Requirements

- **Blender 5.0 or newer**

## Installation

### Option 1 — Install from disk (recommended)

1. Download this repository as a ZIP (**Code > Download ZIP**) **or** clone it and zip the `MeasureIt-X` folder yourself.
2. In Blender, open **Edit > Preferences > Get Extensions** (or **Add-ons** in older builds).
3. Click the dropdown in the top-right and choose **Install from Disk...**
4. Select the ZIP file.
5. Enable **MeasureIt X** in the list.

### Option 2 — Manual install

1. Copy the `MeasureIt-X` folder into your Blender extensions / add-ons directory:
   - **Windows:** `%APPDATA%\Blender Foundation\Blender\<version>\extensions\user_default\`
   - **macOS:** `~/Library/Application Support/Blender/<version>/extensions/user_default/`
   - **Linux:** `~/.config/blender/<version>/extensions/user_default/`
2. Restart Blender.
3. Enable **MeasureIt X** in **Preferences > Add-ons**.

## Usage

1. Open the **N-panel** in the 3D Viewport and find the **Display** tab.
2. Select an object (or enter Edit Mode and pick vertices).
3. Use the MeasureIt X panel to add segments, angles, arcs, areas, labels, notes, or origins.
4. Measurements render directly in the viewport and follow your camera in true 3D.
5. For totaling edge lengths in Edit Mode: select edges, then **Edge menu > Sum Edge Lengths**.

## License

Released under the **GPL-3.0-or-later** license, matching the original MeasureIt add-on.

## Credits

- Original author: **Antonio Vazquez (antonioya)**
- Original project: https://projects.blender.org/extensions/measureit
- Fork maintained by the community as **MeasureIt X**.
