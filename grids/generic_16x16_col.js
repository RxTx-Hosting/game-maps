MapGrids.generic_16x16_col = function(gridLayerGroup, width, height, options = {}) {
    const gridCols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'];
    const gridRows = 16;
    const cellWidth = width / gridCols.length;
    const cellHeight = height / gridRows;

    const lineColor = options.lineColor || '#ffffff';
    const lineOpacity = options.lineOpacity || 0.5;
    const lineWeight = options.lineWeight || 1.5;
    const labelColor = options.labelColor || '#ffffff';
    const labelOpacity = options.labelOpacity || 0.7;
    const labelSize = options.labelSize || 20;

    const gridCells = [];
    const overlayLayer = L.layerGroup();
    const labelMarkers = [];

    for (let row = 0; row < gridRows; row++) {
        for (let col = 0; col < gridCols.length; col++) {
            const x1 = col * cellWidth;
            const y1 = height - (row + 1) * cellHeight;
            const x2 = x1 + cellWidth;
            const y2 = height - row * cellHeight;
            const gridLabel = gridCols[col] + (row + 1);

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
            const labelY = y2 - cellHeight * 0.05;

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
