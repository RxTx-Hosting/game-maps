import argparse
import importlib.util
import json
import sys
from pathlib import Path


def load_map_data(map_file: str):
    """Load map data from a Python module."""
    map_path = Path(map_file).resolve()
    if not map_path.exists():
        print(f"Error: Map file '{map_file}' not found")
        sys.exit(1)

    maps_root = Path(__file__).parent.parent.resolve()
    maps_parent = maps_root.parent
    maps_package_name = maps_root.name

    if str(maps_parent) not in sys.path:
        sys.path.insert(0, str(maps_parent))

    relative_path = map_path.relative_to(maps_root)
    module_name = f"{maps_package_name}.{str(relative_path.with_suffix('')).replace('/', '.')}"

    import importlib

    module = importlib.import_module(module_name)

    if not hasattr(module, "DATA"):
        print(f"Error: '{map_file}' must define a DATA variable")
        sys.exit(1)

    return module.DATA


def generate_html(map_data):
    """Generate standalone HTML for the map preview."""
    categories_dict = []
    category_slug_to_id = {}
    category_data = {}

    for idx, cat in enumerate(map_data.categories):
        cat_id = str(idx)
        categories_dict.append(
            {
                "id": cat_id,
                "slug": cat.slug,
                "name": cat.name,
                "color": cat.color,
                "is_visible_by_default": cat.is_visible_by_default,
                "icon": cat.icon,
            }
        )
        category_slug_to_id[cat.slug] = cat_id
        category_data[cat.slug] = cat

    markers_dict = []
    for marker in map_data.markers:
        category_id = category_slug_to_id.get(marker.category_slug)
        if not category_id:
            print(
                f"Warning: Category {marker.category_slug} not found for marker {marker.name}"
            )
            continue

        category = category_data.get(marker.category_slug)
        icon = marker.icon or (category.icon if category else None)
        description = marker.description or (
            category.default_description if category else None
        )

        markers_dict.append(
            {
                "name": marker.name,
                "description": description,
                "category_id": category_id,
                "position_x": marker.position_x,
                "position_y": marker.position_y,
                "icon": icon,
            }
        )

    grid_js = ""
    grids_dir = Path(__file__).parent.parent / "grids"
    if grids_dir.exists():
        grid_files = sorted(grids_dir.glob("*.js"))
        grid_js = "\n".join([f.read_text() for f in grid_files])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{map_data.map.name} - Map Preview</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin=""/>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, sans-serif;
            background: #1a1a1a;
            color: white;
        }}
        #map {{
            width: 100vw;
            height: 100vh;
        }}
        .category-toggle {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            cursor: pointer;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 6px;
            margin-bottom: 4px;
        }}
        .category-toggle:hover {{
            background: rgba(255, 255, 255, 0.1);
        }}
        .category-color {{
            width: 16px;
            height: 16px;
            border-radius: 50%;
        }}
        .category-label {{
            flex: 1;
        }}
        .marker-count {{
            color: #888;
            font-size: 12px;
        }}
        .sidebar {{
            position: fixed;
            top: 20px;
            left: 20px;
            width: 280px;
            max-height: calc(100vh - 40px);
            background: rgba(0, 0, 0, 0.9);
            border-radius: 8px;
            padding: 20px;
            overflow-y: auto;
            z-index: 1000;
        }}
        .sidebar h1 {{
            margin: 0 0 8px 0;
            font-size: 24px;
        }}
        .sidebar p {{
            margin: 0 0 20px 0;
            color: #888;
            font-size: 14px;
        }}
        .map-pin {{
            position: relative;
            width: 40px;
            height: 40px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 50% 50% 50% 0;
            transform: rotate(-45deg);
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .map-pin::after {{
            content: '';
            position: absolute;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.7);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }}
        .map-pin-content {{
            transform: rotate(45deg);
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1;
        }}
        .coords-overlay {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(8px);
            padding: 16px;
            border-radius: 8px;
            font-size: 14px;
            z-index: 1000;
            min-width: 200px;
        }}
        .coords-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }}
        .coords-label {{
            color: #888;
            margin-right: 12px;
        }}
        .coords-value {{
            font-family: monospace;
            color: #fff;
        }}
        .copy-btn {{
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            margin-top: 8px;
            width: 100%;
        }}
        .copy-btn:hover {{
            background: rgba(255, 255, 255, 0.2);
        }}
        .grid-selector {{
            width: 100%;
            padding: 8px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 4px;
            color: white;
            font-size: 14px;
            margin-bottom: 20px;
        }}
        .grid-selector option {{
            background: #1a1a1a;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="sidebar">
        <h1>{map_data.map.name}</h1>
        <p>Map Preview</p>
        <div style="margin-bottom: 20px;">
            <h3 style="margin-bottom: 12px;">Grid System</h3>
            <select class="grid-selector" id="grid-selector">
                <option value="">None</option>
            </select>
        </div>
        <div>
            <h3 style="margin-bottom: 12px;">Categories</h3>
            <div id="category-filters"></div>
        </div>
    </div>
    <div class="coords-overlay">
        <div style="font-weight: bold; margin-bottom: 12px;">Coordinates</div>
        <div class="coords-row">
            <span class="coords-label">Mouse:</span>
            <span class="coords-value" id="mouse-coords">-</span>
        </div>
        <div class="coords-row">
            <span class="coords-label">Clicked:</span>
            <span class="coords-value" id="clicked-coords">-</span>
        </div>
        <button class="copy-btn" id="copy-btn">Copy Clicked Position</button>
    </div>
    <div id="map"></div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>
    <script>
    {grid_js}

    const mapData = {{
        width: {map_data.map.image_width},
        height: {map_data.map.image_height},
        imageUrl: '{map_data.map.image_url}',
        minZoom: {map_data.map.min_zoom},
        maxZoom: {map_data.map.max_zoom},
        defaultZoom: {map_data.map.default_zoom},
        gridSystem: '{map_data.map.grid_system or ""}',
    }};

    const markers = {json.dumps(markers_dict)};
    const categories = {json.dumps(categories_dict)};

    const bounds = [[0, 0], [mapData.height, mapData.width]];
    const leafletMap = L.map('map', {{
        crs: L.CRS.Simple,
        minZoom: mapData.minZoom,
        maxZoom: mapData.maxZoom,
        attributionControl: false,
        zoomControl: true,
        zoomSnap: 0.25,
        zoomDelta: 0.25,
    }});

    const markerLayers = {{}};
    const categoryMap = {{}};
    categories.forEach(cat => {{
        categoryMap[cat.id] = cat;
        markerLayers[cat.id] = L.layerGroup().addTo(leafletMap);
    }});

    const img = new Image();
    img.onload = async function() {{
        const imgBounds = [[0, 0], [mapData.height, mapData.width]];
        L.imageOverlay(mapData.imageUrl, imgBounds).addTo(leafletMap);

        const center = [mapData.height / 2, mapData.width / 2];
        leafletMap.setView(center, mapData.minZoom);

        const padding = 0.5;
        const extendedBounds = [
            [-mapData.height * padding, -mapData.width * padding],
            [mapData.height * (1 + padding), mapData.width * (1 + padding)]
        ];
        leafletMap.setMaxBounds(extendedBounds);

        let currentGridLayer = null;
        const gridOptions = {
        json.dumps(
            {
                "lineColor": map_data.map.grid_options.line_color
                if map_data.map.grid_options
                else "#ffffff",
                "lineOpacity": map_data.map.grid_options.line_opacity
                if map_data.map.grid_options
                else 0.5,
                "lineWeight": map_data.map.grid_options.line_weight
                if map_data.map.grid_options
                else 1.5,
                "labelColor": map_data.map.grid_options.label_color
                if map_data.map.grid_options
                else "#ffffff",
                "labelOpacity": map_data.map.grid_options.label_opacity
                if map_data.map.grid_options
                else 0.7,
                "labelSize": map_data.map.grid_options.label_size
                if map_data.map.grid_options
                else 20,
            }
        )
    };

        function loadGrid(gridSystemName) {{
            if (currentGridLayer) {{
                leafletMap.removeLayer(currentGridLayer);
                currentGridLayer = null;
            }}

            if (gridSystemName && typeof MapGrids !== 'undefined' && MapGrids[gridSystemName]) {{
                currentGridLayer = L.layerGroup().addTo(leafletMap);
                MapGrids[gridSystemName](currentGridLayer, mapData.width, mapData.height, gridOptions);
            }}
        }}

        const gridSelector = document.getElementById('grid-selector');
        if (typeof MapGrids !== 'undefined') {{
            Object.keys(MapGrids).forEach(gridName => {{
                const option = document.createElement('option');
                option.value = gridName;
                option.textContent = gridName;
                if (gridName === mapData.gridSystem) {{
                    option.selected = true;
                }}
                gridSelector.appendChild(option);
            }});
        }}

        if (mapData.gridSystem) {{
            loadGrid(mapData.gridSystem);
        }}

        gridSelector.addEventListener('change', function(e) {{
            loadGrid(e.target.value);
        }})

        const svgCache = {{}};
        function hexToRgba(hex, alpha) {{
            const r = parseInt(hex.slice(1, 3), 16);
            const g = parseInt(hex.slice(3, 5), 16);
            const b = parseInt(hex.slice(5, 7), 16);
            return `rgba(${{r}}, ${{g}}, ${{b}}, ${{alpha}})`;
        }}

        async function loadAndColorSvg(iconUrl, color) {{
            try {{
                let svgText;
                if (svgCache[iconUrl]) {{
                    svgText = svgCache[iconUrl];
                }} else {{
                    const response = await fetch(iconUrl);
                    svgText = await response.text();
                    svgCache[iconUrl] = svgText;
                }}

                const coloredSvg = svgText
                    .replace(/fill="[^"]*"/g, (match) => {{
                        const fillValue = match.match(/fill="([^"]*)"/)[1];
                        if (fillValue.startsWith('#1') || fillValue.startsWith('#0') || fillValue === 'black') {{
                            return match;
                        }}
                        return `fill="${{color}}"`;
                    }})
                    .replace(/<svg/, '<svg style="width: 100%; height: 100%;"');

                return coloredSvg;
            }} catch (error) {{
                console.error('Failed to load SVG:', iconUrl, error);
                return '';
            }}
        }}

        // Create markers
        for (const marker of markers) {{
            const category = categoryMap[marker.category_id];
            if (!category) continue;

            const y = marker.position_y * mapData.height;
            const x = marker.position_x * mapData.width;

            let iconHtml;
            let iconSize = [16, 16];
            let iconAnchor = [8, 8];

            if (marker.icon) {{
                const iconUrl = marker.icon;
                const isSvg = iconUrl.toLowerCase().endsWith('.svg');

                if (isSvg) {{
                    const svgContent = await loadAndColorSvg(iconUrl, category.color || '#888888');
                    const borderColor = category.color || '#888888';
                    const rgbaColor = hexToRgba(borderColor, 0.7);
                    iconHtml = `
                        <div class="map-pin" style="border: 3px solid ${{rgbaColor}};">
                            <div class="map-pin-content">
                                <div style="width: 24px; height: 24px; display: flex; align-items: center; justify-content: center;">${{svgContent}}</div>
                            </div>
                        </div>`;
                }} else {{
                    const borderColor = category.color || '#888888';
                    const rgbaColor = hexToRgba(borderColor, 0.7);
                    iconHtml = `
                        <div class="map-pin" style="border: 3px solid ${{rgbaColor}};">
                            <div class="map-pin-content">
                                <img src="${{iconUrl}}" style="width: 24px; height: 24px;" />
                            </div>
                        </div>`;
                }}
                iconSize = [40, 40];
                iconAnchor = [12, 38];
            }} else {{
                iconHtml = `<div style="background-color: ${{category.color || '#888888'}}; width: 16px; height: 16px; border-radius: 50%; border: 2px solid white;"></div>`;
            }}

            const icon = L.divIcon({{
                className: 'custom-marker',
                html: iconHtml,
                iconSize: iconSize,
                iconAnchor: iconAnchor
            }});

            const leafletMarker = L.marker([y, x], {{ icon: icon }});
            leafletMarker.bindTooltip(marker.name, {{
                permanent: false,
                direction: 'top',
                offset: [8, -40]
            }});

            let popupContent = `<div><h4 style="margin: 0 0 8px 0;">${{marker.name}}</h4>`;
            if (marker.description) {{
                popupContent += `<p style="margin: 0 0 8px 0;">${{marker.description}}</p>`;
            }}
            popupContent += `<p style="margin: 0; color: ${{category.color}};">${{category.name}}</p></div>`;

            leafletMarker.bindPopup(popupContent, {{ offset: [8, -42] }});
            leafletMarker.addTo(markerLayers[marker.category_id]);
        }}

        // Update marker counts
        markers.forEach(marker => {{
            const countElem = document.getElementById(`count-${{marker.category_id}}`);
            if (countElem) {{
                const current = parseInt(countElem.textContent) || 0;
                countElem.textContent = current + 1;
            }}
        }});
    }};

    img.src = mapData.imageUrl;

    // Category filters
    const categoryFilters = document.getElementById('category-filters');
    categories.forEach(cat => {{
        const div = document.createElement('label');
        div.className = 'category-toggle';
        div.innerHTML = `
            <input type="checkbox" checked data-category-id="${{cat.id}}">
            <span class="category-color" style="background-color: ${{cat.color}};"></span>
            <span class="category-label">${{cat.name}}</span>
            <span class="marker-count" id="count-${{cat.id}}">0</span>
        `;
        categoryFilters.appendChild(div);

        const checkbox = div.querySelector('input');
        checkbox.addEventListener('change', function() {{
            if (this.checked) {{
                leafletMap.addLayer(markerLayers[cat.id]);
            }} else {{
                leafletMap.removeLayer(markerLayers[cat.id]);
            }}
        }});
    }});

    const mouseCoords = document.getElementById('mouse-coords');
    const clickedCoords = document.getElementById('clicked-coords');
    const copyBtn = document.getElementById('copy-btn');
    let clickedPosition = null;

    leafletMap.on('mousemove', function(e) {{
        const x = (e.latlng.lng / mapData.width).toFixed(6);
        const y = (e.latlng.lat / mapData.height).toFixed(6);
        mouseCoords.textContent = `x: ${{x}}, y: ${{y}}`;
    }});

    leafletMap.on('click', function(e) {{
        const x = (e.latlng.lng / mapData.width).toFixed(6);
        const y = (e.latlng.lat / mapData.height).toFixed(6);
        clickedPosition = {{ x, y }};
        clickedCoords.textContent = `x: ${{x}}, y: ${{y}}`;
        console.log(`Clicked position - x: ${{x}}, y: ${{y}}`);
    }});

    copyBtn.addEventListener('click', function() {{
        if (clickedPosition) {{
            const text = `position_x=${{clickedPosition.x}},\\nposition_y=${{clickedPosition.y}}`;
            navigator.clipboard.writeText(text).then(() => {{
                copyBtn.textContent = 'Copied!';
                setTimeout(() => {{
                    copyBtn.textContent = 'Copy Clicked Position';
                }}, 2000);
            }}).catch(err => {{
                console.error('Failed to copy:', err);
            }});
        }}
    }});
    </script>
</body>
</html>"""

    return html


def main():
    parser = argparse.ArgumentParser(description="Generate HTML preview of a game map")
    parser.add_argument(
        "map_file", help="Path to the map Python file (e.g., icarus/olympus.py)"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="preview.html",
        help="Output HTML file (default: preview.html)",
    )
    args = parser.parse_args()

    print(f"Loading map data from {args.map_file}...")
    map_data = load_map_data(args.map_file)

    print("Generating HTML preview...")
    html = generate_html(map_data)

    output_path = Path(args.output)
    output_path.write_text(html)

    print(f"Preview generated: {output_path.absolute()}")
    print(f"  Open {output_path.name} in your browser to view the map")


if __name__ == "__main__":
    main()
