/**
 * compare.js — Algorithm Comparison Mode
 *
 * Runs all scheduling algorithms on the same process set
 * and displays a side-by-side metrics comparison table.
 */

'use strict';

const ALGORITHM_MAP = {
    fcfs: { name: 'FCFS', fn: scheduleFCFS },
    sjf: { name: 'SJF', fn: scheduleSJF },
    srtf: { name: 'SRTF', fn: scheduleSRTF },
    rr: { name: 'Round Robin', fn: (p) => scheduleRR(p, 2) },
    priority: { name: 'Priority', fn: schedulePriority },
};

function runComparison(processes) {
    const results = {};

    for (const [key, algo] of Object.entries(ALGORITHM_MAP)) {
        const result = algo.fn(processes);
        const metrics = calculateMetrics(result.processes);
        results[key] = {
            name: algo.name,
            metrics,
            timeline: result.timeline,
            processes: result.processes,
        };
    }

    return results;
}

function renderComparisonTable(results) {
    const container = document.getElementById('comparison-container');
    if (!container) return;

    const keys = Object.keys(results);
    const metrics = ['avgWaitingTime', 'avgTurnaroundTime', 'avgResponseTime', 'cpuUtilisation', 'throughput'];
    const labels = ['Avg WT', 'Avg TAT', 'Avg RT', 'CPU Util %', 'Throughput'];

    let html = '<table class="data-table comparison-table"><thead><tr><th>Metric</th>';
    keys.forEach(k => { html += `<th>${results[k].name}</th>`; });
    html += '</tr></thead><tbody>';

    metrics.forEach((m, i) => {
        html += `<tr><td><strong>${labels[i]}</strong></td>`;
        const values = keys.map(k => results[k].metrics[m]);
        const best = m === 'cpuUtilisation' || m === 'throughput'
            ? Math.max(...values) : Math.min(...values);

        keys.forEach(k => {
            const val = results[k].metrics[m];
            const isBest = val === best;
            html += `<td class="${isBest ? 'best-value' : ''}">${val}${m === 'cpuUtilisation' ? '%' : ''}</td>`;
        });
        html += '</tr>';
    });

    html += '</tbody></table>';
    container.innerHTML = html;

    document.getElementById('comparison-section').style.display = 'block';
}
