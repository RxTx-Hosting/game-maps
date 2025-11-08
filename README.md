# Game Maps

Community-contributed map data for various games, used by [RxTx Hosting](https://rxtx-hosting.com).

## Overview

This repository contains map data, markers, and grid systems for interactive game maps. Contributors can add new maps, update existing ones, and test their changes locally before submitting.

## Structure

```
├── icarus/              # Icarus game maps
│   └── olympus.py      # Olympus map data
├── grids/              # Grid system definitions
│   └── icarus_16x16.js # 16x16 grid system for Icarus
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
python test/preview.py icarus/olympus.py
```

This creates `preview.html` that you can open in your browser to see exactly how your map will look on the website.

## Adding a New Map

1. Create a new Python file in the appropriate game directory (e.g., `icarus/new_map.py`)
2. Define your map data using the models (see examples below)
3. Test with `python test/preview.py path/to/your/map.py`
4. Submit a pull request

### Example Map Structure

```python
from ..game_map import GameMapData, GridStyleOptions
from ..map_category import MapCategoryData
from ..map_data import MapData
from ..map_marker import MapMarkerData

DATA = MapData(
    map=GameMapData(
        name="Map Name",
        slug="map-slug",
        description="Map description",
        image_url="https://cdn.example.com/map.webp",
        image_width=2048,
        image_height=2048,
        min_zoom=-1,
        max_zoom=2,
        default_zoom=0,
        default_center_x=0.5,
        default_center_y=0.5,
        grid_system="icarus_16x16",  # Optional
        grid_options=GridStyleOptions(  # Optional
            line_color="#ffffff",
            line_opacity=0.9,
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
            icon="https://cdn.example.com/icon.svg",  # Optional
            default_description="Default description",  # Optional
        ),
    ],
    markers=[
        MapMarkerData(
            name="Marker Name",
            category_slug="category-slug",
            position_x=0.5,  # 0.0 to 1.0 (percentage of map width)
            position_y=0.5,  # 0.0 to 1.0 (percentage of map height)
            description="Custom description",  # Optional, uses category default if not set
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
- `image_url`: URL to the map image (WEBP recommended)
- `image_width`: Image width in pixels
- `image_height`: Image height in pixels
- `min_zoom`: Minimum zoom level (e.g., -1)
- `max_zoom`: Maximum zoom level (e.g., 2)
- `default_zoom`: Starting zoom level
- `default_center_x`: Starting X position (0.0-1.0)
- `default_center_y`: Starting Y position (0.0-1.0)
- `grid_system`: Optional grid system name
- `grid_options`: Optional grid styling

### MapCategoryData

- `slug`: URL-friendly identifier
- `name`: Display name
- `color`: Hex color code for markers
- `is_visible_by_default`: Show on map load (default: True)
- `icon`: Optional URL to category icon
- `default_description`: Optional default description for markers in this category

### MapMarkerData

- `name`: Marker name
- `category_slug`: Category this marker belongs to
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
