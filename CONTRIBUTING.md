# Contributing to Game Maps

Thank you for contributing! This guide will help you add or update game maps.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone git@github.com:YOUR_USERNAME/game-maps.git
   cd game-maps
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Adding Markers to an Existing Map

### Step 1: Find the Map File

Navigate to the game directory and find the map file. For example:
- Icarus Olympus: `games/icarus/olympus.py`
- Enshrouded Embervale: `games/enshrouded/embervale.py`

### Step 2: Add Your Marker

Find the appropriate category and add a new `MapMarkerData` entry to its `markers` list:

```python
MapCategoryData(
    slug="locations-cave-t1",
    name="Caves - Tier 1",
    color="#3F7791",
    markers=[
        # Existing markers...
        MapMarkerData(
            name="My New Cave",
            position_x=0.123456,
            position_y=0.654321,
            description="Optional description",  # Leave out to use category default
        ),
    ],
),
```

### Step 3: Finding Coordinates

**Method 1: Using the Preview Tool**
1. Run `python test/preview.py games/icarus/olympus.py`
2. Open `preview.html` in your browser
3. Click on the map where you want the marker
4. Check the coordinates overlay or browser console for the coordinates

**Method 2: Manual Calculation**
- `position_x = pixel_x / image_width`
- `position_y = pixel_y / image_height`
- Values range from 0.0 (left/top) to 1.0 (right/bottom)

### Step 4: Test Your Changes

```bash
python test/preview.py games/icarus/olympus.py
```

Open `preview.html` and verify:
- ✓ Marker appears in the correct location
- ✓ Marker has the correct name
- ✓ Marker has the correct category/color
- ✓ Tooltip and popup work correctly

### Step 5: Submit a Pull Request

```bash
git add games/icarus/olympus.py
git commit -m "Add [marker name] to Olympus map"
git push origin main
```

Then create a pull request on GitHub.

## Adding a New Category

If you need a new type of marker that doesn't fit existing categories:

```python
MapCategoryData(
    slug="my-category-slug",
    name="My Category Name",
    color="#FF5733",  # Hex color code
    icon="https://cdn.example.com/icon.svg",  # Optional 64x64 SVG/PNG/WEBP
    use_pin_style=True,  # True for pin markers, False for simple icons
    default_description="Default marker description",  # Optional
    markers=[
        # Add markers here
    ],
),
```

**Tips:**
- Choose a descriptive slug (kebab-case)
- Pick a color that stands out but fits the theme
- Icons should be 64x64 SVG/PNG/WEBP
- Set `use_pin_style=True` for pin-style markers with letter fallbacks
- Set `use_pin_style=False` for simple icon overlays (larger, centered)
- Custom icons need to be uploaded to the rxtx Hosting CDN - mention this in your PR if adding new icons

## Adding a New Map

### Step 1: Create the Map File

Create a new file in the appropriate game directory:
```bash
mkdir -p games/your_game
touch games/your_game/your_map.py
```

### Step 2: Define the Map

```python
from ...game_map import GameMapData, GridStyleOptions
from ...map_category import MapCategoryData
from ...map_data import MapData
from ...map_marker import MapMarkerData


DATA = MapData(
    map=GameMapData(
        name="Map Display Name",
        slug="map-slug",
        description="Brief description of this map",
        image_url="https://cdn.example.com/map-image.webp",  # For single image
        # OR for tile-based maps:
        # tile_url="https://cdn.example.com/tiles/{x}_{y}.webp",
        # tile_size=1280,
        image_width=2048,  # Total map width in pixels
        image_height=2048,  # Total map height in pixels
        min_zoom=-1,  # How far users can zoom out
        max_zoom=2,   # How far users can zoom in
        default_zoom=0,  # Starting zoom level
        default_center_x=0.5,  # Starting X (0.5 = center)
        default_center_y=0.5,  # Starting Y (0.5 = center)
        grid_system="generic_16x16",  # Optional grid system
    ),
    categories=[
        MapCategoryData(
            slug="category-slug",
            name="Category Name",
            color="#3F7791",
            markers=[
                # Add markers here
            ],
        ),
    ],
)
```

### Step 3: Register the Map

Add your map to `__init__.py`:

```python
from .games.your_game.your_map import DATA as your_game_your_map_data

MAPS: dict[tuple[str, str], MapData] = {
    # ... existing maps ...
    ("game_your_game", "your_map"): your_game_your_map_data,
}
```

### Step 4: Test

```bash
python test/preview.py games/your_game/your_map.py
```

## Creating a Grid System

Grid systems are JavaScript files that define coordinate overlays. See `grids/icarus_16x16.js` for an example.

Key components:
1. Grid definition function
2. Cell labeling logic
3. Interactive click handlers
4. Styling options

## Code Style

- Use relative imports from the games directory (e.g., `from ...game_map import GameMapData`)
- Follow existing formatting patterns
- Keep marker lists alphabetically sorted by name within each category (optional but helpful)
- Use descriptive names for categories and markers
- Markers are now nested under their categories, not in a separate top-level list

## Pull Request Guidelines

**Good PR:**
- Clear title describing what was added/changed
- Description explaining why (if not obvious)
- Single focused change
- Tested with preview tool

**Example PR titles:**
- `Add 15 cave markers to Olympus map`
- `Create Styx map with initial markers`
- `Fix coordinates for Northern caves on Olympus`
- `Add new "Resource Nodes" category`

## Questions?

- Check existing map files for examples
- Open an issue if you need help
- Tag maintainers in your PR if you need review

## Thank You!

Every contribution helps make these maps better for the community! 🎮
