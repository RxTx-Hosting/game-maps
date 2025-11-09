# Game Maps

Community-contributed map data for various games, used by [RxTx Hosting](https://rxtx-hosting.com).

## Overview

This repository contains map data, markers, and grid systems for interactive game maps. Contributors can add new maps, update existing ones, and test their changes locally before submitting.

## Structure

```
├── games/              # Game-specific map data
│   ├── icarus/         # Icarus game maps
│   │   └── olympus.py  # Olympus map data
│   └── enshrouded/     # Enshrouded game maps
│       └── embervale.py # Embervale map data
├── grids/              # Grid system definitions
│   ├── icarus_16x16.js # 16x16 grid system for Icarus
│   ├── generic_8x8.js  # Generic 8x8 grid
│   ├── generic_10x10.js # Generic 10x10 grid
│   └── generic_16x16.js # Generic 16x16 grid
├── test/               # Testing tools
│   └── preview.py      # Generate HTML preview of maps
├── game_map.py         # GameMapData model
├── map_data.py         # MapData model
├── map_category.py     # MapCategoryData model
└── map_marker.py       # MapMarkerData model
```

## Quick Start

### Prerequisites

```bash
pip install -r requirements.txt
```

### Testing Your Changes

After making changes to a map file, generate a preview:

```bash
python test/preview.py games/icarus/olympus.py
```

This creates `preview.html` that you can open in your browser to see exactly how your map will look on the website.

## Adding a New Map

1. Create a new Python file in the appropriate game directory (e.g., `games/icarus/new_map.py`)
2. Define your map data using the models (see examples below)
3. Test with `python test/preview.py games/your_game/your_map.py`
4. Submit a pull request

### Example Map Structure

```python
from ...game_map import GameMapData, GridStyleOptions
from ...map_category import MapCategoryData
from ...map_data import MapData
from ...map_marker import MapMarkerData

DATA = MapData(
    map=GameMapData(
        name="Map Name",
        slug="map-slug",
        description="Map description",
        image_url="https://cdn.example.com/map.webp",  # For single image maps
        # OR for tile-based maps:
        # tile_url="https://cdn.example.com/tiles/{x}_{y}.webp",
        # tile_size=1280,
        image_width=2048,
        image_height=2048,
        min_zoom=-1,
        max_zoom=2,
        default_zoom=0,
        default_center_x=0.5,
        default_center_y=0.5,
        grid_system="generic_16x16",  # Optional: icarus_16x16, generic_8x8, generic_10x10, generic_16x16
        grid_options=GridStyleOptions(  # Optional
            line_color="#ffffff",
            line_opacity=0.5,
            line_weight=1.5,
            label_color="#ffffff",
            label_opacity=0.9,
            label_size=20,
        ),
    ),
    categories=[
        MapCategoryData(
            slug="category-slug",
            name="Category Name",
            color="#3F7791",
            icon="https://cdn.example.com/icon.svg",  # Optional 64x64 SVG/PNG/WEBP
            use_pin_style=True,  # True for pin markers, False for simple icons (default: True)
            default_description="Default description",  # Optional
            markers=[
                MapMarkerData(
                    name="Marker Name",
                    position_x=0.5,  # 0.0 to 1.0 (percentage of map width)
                    position_y=0.5,  # 0.0 to 1.0 (percentage of map height)
                    description="Custom description",  # Optional, uses category default if not set
                    icon="https://cdn.example.com/custom-icon.svg",  # Optional, overrides category icon
                ),
            ],
        ),
    ],
)
```

### Finding Coordinates

1. Open the map preview in your browser
2. Click on the map where you want to place a marker
3. Check the browser console for the coordinates
4. Or use the coordinates overlay feature if available

## Models Reference

### GameMapData

- `name`: Display name of the map
- `slug`: URL-friendly identifier
- `description`: Optional description
- `image_url`: URL to the map image (WEBP recommended) - for single image maps
- `tile_url`: URL pattern for tile-based maps (e.g., `https://cdn.../tiles/{x}_{y}.webp`)
- `tile_size`: Size of each tile in pixels (required if using `tile_url`)
- `image_width`: Total map width in pixels
- `image_height`: Total map height in pixels
- `min_zoom`: Minimum zoom level (e.g., -4)
- `max_zoom`: Maximum zoom level (e.g., 2)
- `default_zoom`: Starting zoom level
- `default_center_x`: Starting X position (0.0-1.0)
- `default_center_y`: Starting Y position (0.0-1.0)
- `grid_system`: Optional grid system name (e.g., `generic_8x8`, `generic_16x16`, `icarus_16x16`)
- `grid_options`: Optional grid styling (`GridStyleOptions`)

### MapCategoryData

- `slug`: URL-friendly identifier
- `name`: Display name
- `color`: Hex color code for markers
- `is_visible_by_default`: Show on map load (default: True)
- `use_pin_style`: True for pin-style markers, False for simple icon overlays (default: True)
- `icon`: Optional URL to category icon (64x64 SVG/PNG/WEBP recommended)
- `default_description`: Optional default description for markers in this category
- `markers`: List of `MapMarkerData` objects belonging to this category

### MapMarkerData

- `name`: Marker name
- `position_x`: X position (0.0-1.0, percentage of map width)
- `position_y`: Y position (0.0-1.0, percentage of map height)
- `description`: Optional custom description (uses category default if not set)
- `icon`: Optional custom icon URL (uses category icon if not set)

## Grid Systems

Grid systems provide coordinate overlays on maps. See `grids/` for examples.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## License

This repository is open source. Map data contributions are welcome from the community.
