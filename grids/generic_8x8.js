// Generic 8x8 grid: Rows are letters (A-H), Columns are numbers (1-8)
// Grid cells: A1, A2, A3... B1, B2, B3... etc
MapGrids.generic_8x8 = function(gridLayerGroup, width, height, options = {}) {
    const gridRows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    const gridCols = 8;
    const cellWidth = width / gridCols;
    const cellHeight = height / gridRows.length;

    const lineColor = options.lineColor || '#ffffff';
    const lineOpacity = options.lineOpacity || 0.5;
    const lineWeight = options.lineWeight || 1.5;
    const labelColor = options.labelColor || '#ffffff';
    const labelOpacity = options.labelOpacity || 0.7;
    const labelSize = options.labelSize || 20;

    const gridCells = [];
    const overlayLayer = L.layerGroup();
    const labelMarkers = [];

    for (let row = 0; row < gridRows.length; row++) {
        for (let col = 0; col < gridCols; col++) {
            const x1 = col * cellWidth;
            const y1 = row * cellHeight;
            const x2 = x1 + cellWidth;
            const y2 = y1 + cellHeight;
            const gridLabel = gridRows[row] + (col + 1);

            L.rectangle([[y1, x1], [y2, x2]], {
                color: lineColor,
                weight: lineWeight,
                opacity: lineOpacity,
                fill: false,
                interactive: false
            }).addTo(gridLayerGroup);

            const clickRect = L.rectangle([[y1, x1], [y2, x2]], {
                color: 'transparent',
                weight: 0,
                opacity: 0,
                fill: true,
                fillOpacity: 0,
                interactive: true
            }).addTo(gridLayerGroup);

            gridCells.push({
                label: gridLabel,
                bounds: [[y1, x1], [y2, x2]],
                rectangle: clickRect
            });

            const labelX = x1 + cellWidth * 0.05;
            const labelY = y1 + cellHeight * 0.05;

            const labelMarker = L.marker([labelY, labelX], {
                icon: L.divIcon({
                    className: 'grid-label',
                    html: `<div class="grid-label-text" style="color: ${labelColor}; font-size: ${labelSize}px; font-weight: 700; text-shadow: 2px 2px 8px rgba(0,0,0,0.9); opacity: ${labelOpacity}; pointer-events: none; user-select: none;">${gridLabel}</div>`,
                    iconSize: [60, 30],
                    iconAnchor: [0, 0]
                }),
                interactive: false
            }).addTo(gridLayerGroup);

            labelMarkers.push({
                marker: labelMarker,
                label: gridLabel,
                baseSize: labelSize,
                color: labelColor,
                opacity: labelOpacity
            });
        }
    }

    return {
        cells: gridCells,
        overlayLayer: overlayLayer,
        labelMarkers: labelMarkers,
        width: width,
        height: height
    };
};
