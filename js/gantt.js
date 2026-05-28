/**
 * gantt.js — Gantt Chart Rendering Engine
 *
 * Renders a horizontal bar chart showing process execution timeline.
 */

'use strict';

// Color palette for processes
const GANTT_COLORS = [
    '#4f46e5', '#22c55e', '#f59e0b', '#ef4444', '#8b5cf6',
    '#06b6d4', '#ec4899', '#14b8a6', '#f97316', '#6366f1',
    '#a855f7', '#84cc16', '#0ea5e9', '#d946ef', '#10b981',
];

/**
 * Assign consistent colors to process IDs
 */
function buildColorMap(timeline) {
    const map = {};
    let idx = 0;
    for (const block of timeline) {
        if (block.id !== 'idle' && !(block.id in map)) {
            map[block.id] = GANTT_COLORS[idx % GANTT_COLORS.length];
            idx++;
        }
    }
    return map;
}

/**
 * Render the Gantt chart into the given container
 */
function renderGanttChart(timeline) {
    const section = document.getElementById('gantt-section');
    const container = document.getElementById('gantt-container');
    if (!section || !container) return;

    section.style.display = 'block';
    container.innerHTML = '';

    if (timeline.length === 0) {
        container.innerHTML = '<p class="text-muted">No data to display.</p>';
        return;
    }

    const colorMap = buildColorMap(timeline);
    const totalTime = timeline[timeline.length - 1].end;

    // Create the bar track
    const track = createElement('div', 'gantt-track');

    timeline.forEach(block => {
        const width = ((block.end - block.start) / totalTime) * 100;
        const bar = createElement('div', 'gantt-bar' + (block.id === 'idle' ? ' gantt-idle' : ''));
        bar.style.width = width + '%';

        if (block.id !== 'idle') {
            bar.style.background = colorMap[block.id];
        }

        // Label
        const label = createElement('span', 'gantt-label', block.id);
        bar.appendChild(label);

        // Tooltip
        bar.title = `${block.id}: ${block.start} → ${block.end} (${block.end - block.start} units)`;

        track.appendChild(bar);
    });

    container.appendChild(track);

    // Time markers
    const markers = createElement('div', 'gantt-markers');
    const timestamps = [0];
    timeline.forEach(b => { if (!timestamps.includes(b.end)) timestamps.push(b.end); });
    timestamps.sort((a, b) => a - b);

    timestamps.forEach(t => {
        const marker = createElement('span', 'gantt-marker', String(t));
        marker.style.left = ((t / totalTime) * 100) + '%';
        markers.appendChild(marker);
    });

    container.appendChild(markers);

    // Legend
    const legend = createElement('div', 'gantt-legend');
    for (const [id, color] of Object.entries(colorMap)) {
        const item = createElement('div', 'gantt-legend-item');
        const swatch = createElement('span', 'gantt-swatch');
        swatch.style.background = color;
        item.appendChild(swatch);
        item.appendChild(document.createTextNode(id));
        legend.appendChild(item);
    }
    container.appendChild(legend);
}

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment

// style adjustment
