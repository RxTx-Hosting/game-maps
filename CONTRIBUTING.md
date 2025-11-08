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
- Icarus Olympus: `icarus/olympus.py`

### Step 2: Add Your Marker

Add a new `MapMarkerData` entry to the `markers` list:

```python
MapMarkerData(
    name="My New Location",
    category_slug="locations-cave-t1",  # Use an existing category
    position_x=0.123456,
    position_y=0.654321,
    description="Optional description",  # Leave out to use category default
),
```

### Step 3: Finding Coordinates

**Method 1: Using the Preview Tool**
1. Run `python test/preview.py icarus/olympus.py`
2. Open `preview.html` in your browser
3. Open browser console (F12)
4. Click on the map where you want the marker
5. Copy the coordinates from the console

**Method 2: Manual Calculation**
- `position_x = pixel_x / image_width`
- `position_y = pixel_y / image_height`
- Values range from 0.0 (left/top) to 1.0 (right/bottom)

### Step 4: Test Your Changes

```bash
python test/preview.py icarus/olympus.py
```

Open `preview.html` and verify:
- ✓ Marker appears in the correct location
- ✓ Marker has the correct name
- ✓ Marker has the correct category/color
- ✓ Tooltip and popup work correctly

### Step 5: Submit a Pull Request

```bash
git add icarus/olympus.py
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
    icon="https://cdn.example.com/icon.svg",  # Optional
    default_description="Default marker description",  # Optional
),
```

**Tips:**
- Choose a descriptive slug (kebab-case)
- Pick a color that stands out but fits the theme
- If using an icon, it should be an SVG for best results
- The icon will be colored with the category color

## Adding a New Map

### Step 1: Create the Map File

Create a new file in the appropriate game directory:
```bash
touch icarus/new_map.py
```

### Step 2: Define the Map

```python
from ..game_map import GameMapData, GridStyleOptions
from ..map_category import MapCategoryData
from ..map_data import MapData
from ..map_marker import MapMarkerData


DATA = MapData(
    map=GameMapData(
        name="Map Display Name",
        slug="map-slug",
        description="Brief description of this map",
        image_url="https://cdn.example.com/map-image.webp",
        image_width=2048,  # Actual image width in pixels
        image_height=2048,  # Actual image height in pixels
        min_zoom=-1,  # How far users can zoom out
        max_zoom=2,   # How far users can zoom in
        default_zoom=0,  # Starting zoom level
        default_center_x=0.5,  # Starting X (0.5 = center)
        default_center_y=0.5,  # Starting Y (0.5 = center)
    ),
    categories=[
        # Add your categories here
    ],
    markers=[
        # Add your markers here
    ],
)
```

### Step 3: Register the Map

Add your map to `__init__.py`:

```python
from .icarus.new_map import DATA as icarus_new_map_data

MAPS: dict[tuple[str, str], MapData] = {
    # ... existing maps ...
    ("game_icarus", "new_map"): icarus_new_map_data,
}
```

### Step 4: Test

```bash
python test/preview.py icarus/new_map.py
```

## Creating a Grid System

Grid systems are JavaScript files that define coordinate overlays. See `grids/icarus_16x16.js` for an example.

Key components:
1. Grid definition function
2. Cell labeling logic
3. Interactive click handlers
4. Styling options

## Code Style

- Use relative imports (e.g., `from ..game_map import GameMapData`)
- Follow existing formatting patterns
- Keep marker lists alphabetically sorted by name (optional but helpful)
- Use descriptive names for categories and markers

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
