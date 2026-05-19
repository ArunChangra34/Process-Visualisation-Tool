/**
 * metrics.js — Performance Metrics Calculation & Rendering
 */

'use strict';

/**
 * Calculate aggregate metrics from completed processes
 */
function calculateMetrics(processes) {
    const n = processes.length;
    if (n === 0) return null;

    const totalWT = processes.reduce((s, p) => s + p.waitingTime, 0);
    const totalTAT = processes.reduce((s, p) => s + p.turnaroundTime, 0);
    const totalRT = processes.reduce((s, p) => s + p.responseTime, 0);
    const totalBT = processes.reduce((s, p) => s + p.burstTime, 0);
    const makespan = Math.max(...processes.map(p => p.completionTime));

    return {
        avgWaitingTime: toFixed(totalWT / n),
        avgTurnaroundTime: toFixed(totalTAT / n),
        avgResponseTime: toFixed(totalRT / n),
        cpuUtilisation: toFixed((totalBT / makespan) * 100),
        throughput: toFixed(n / makespan),
        makespan,
    };
}

/**
 * Render the metrics cards
 */
function renderMetrics(processes) {
    const section = document.getElementById('metrics-section');
    const container = document.getElementById('metrics-container');
    if (!section || !container) return;

    const m = calculateMetrics(processes);
    if (!m) return;

    section.style.display = 'block';

    const cards = [
        { value: m.avgWaitingTime, label: 'Avg Waiting Time', icon: '⏳' },
        { value: m.avgTurnaroundTime, label: 'Avg Turnaround Time', icon: '🔄' },
        { value: m.avgResponseTime, label: 'Avg Response Time', icon: '⚡' },
        { value: m.cpuUtilisation + '%', label: 'CPU Utilisation', icon: '💻' },
        { value: m.throughput, label: 'Throughput', icon: '📈' },
    ];

    container.innerHTML = cards.map(c => `
        <div class="metric-card">
            <div class="metric-icon">${c.icon}</div>
            <div class="metric-value">${c.value}</div>
            <div class="metric-label">${c.label}</div>
        </div>
    `).join('');
}

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting

// formatting
