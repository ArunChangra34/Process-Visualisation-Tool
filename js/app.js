/**
 * Process Visualisation Tool — Main Application
 * ================================================
 */

'use strict';

document.addEventListener('DOMContentLoaded', () => {
    console.log('Process Visualisation Tool initialised');
    initApp();

    // Quick FCFS smoke test
    const testProcs = [
        new Process('P1', 0, 5),
        new Process('P2', 2, 3),
        new Process('P3', 4, 8),
    ];
    const result = scheduleFCFS(testProcs);
    console.table(result.processes.map(p => ({
        id: p.id,
        AT: p.arrivalTime,
        BT: p.burstTime,
        CT: p.completionTime,
        TAT: p.turnaroundTime,
        WT: p.waitingTime,
    })));
});

// ── State ────────────────────────────────────────────────────────────────────
let processCounter = 1;
let processList = [];

// ── Init ─────────────────────────────────────────────────────────────────────
function initApp() {
    updateProcessIdField();
    bindEvents();
}

function updateProcessIdField() {
    const field = document.getElementById('process-id');
    if (field) field.value = 'P' + processCounter;
}

function bindEvents() {
    const addBtn = document.getElementById('add-process-btn');
    const clearBtn = document.getElementById('clear-all-btn');
    const presetBtn = document.getElementById('load-preset-btn');
    const runBtn = document.getElementById('run-btn');
    const algoSelect = document.getElementById('algorithm-select');

    if (addBtn) addBtn.addEventListener('click', addProcess);
    if (clearBtn) clearBtn.addEventListener('click', clearAll);
    if (presetBtn) presetBtn.addEventListener('click', loadPreset);
    if (runBtn) runBtn.addEventListener('click', runSimulation);
    if (algoSelect) algoSelect.addEventListener('change', onAlgorithmChange);
}

// ── Algorithm Select ─────────────────────────────────────────────────────────
function onAlgorithmChange() {
    const algo = document.getElementById('algorithm-select').value;
    const qGroup = document.getElementById('quantum-group');
    if (qGroup) qGroup.style.display = algo === 'rr' ? 'block' : 'none';
}

// ── Process Management ───────────────────────────────────────────────────────
function addProcess() {
    const at = parseInt(document.getElementById('arrival-time').value, 10);
    const bt = parseInt(document.getElementById('burst-time').value, 10);
    const pr = parseInt(document.getElementById('priority-input').value, 10) || 0;

    if (isNaN(at) || at < 0) return alert('Arrival time must be >= 0');
    if (isNaN(bt) || bt < 1) return alert('Burst time must be >= 1');

    const id = 'P' + processCounter++;
    processList.push(new Process(id, at, bt, pr));
    updateProcessIdField();
    renderProcessTable();

    // Reset inputs
    document.getElementById('arrival-time').value = '0';
    document.getElementById('burst-time').value = '1';
    document.getElementById('priority-input').value = '0';
}

function removeProcess(index) {
    processList.splice(index, 1);
    renderProcessTable();
}

function clearAll() {
    processList = [];
    processCounter = 1;
    updateProcessIdField();
    renderProcessTable();

    // Hide result sections
    ['gantt-section', 'metrics-section', 'results-section'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = 'none';
    });
}

function loadPreset() {
    clearAll();
    const presets = [
        new Process('P1', 0, 5, 2),
        new Process('P2', 1, 3, 1),
        new Process('P3', 2, 8, 4),
        new Process('P4', 3, 6, 3),
        new Process('P5', 4, 4, 5),
    ];
    processList = presets;
    processCounter = 6;
    updateProcessIdField();
    renderProcessTable();
}

// ── Table Rendering ──────────────────────────────────────────────────────────
function renderProcessTable() {
    const section = document.getElementById('table-section');
    const tbody = document.getElementById('process-tbody');
    if (!section || !tbody) return;

    section.style.display = processList.length ? 'block' : 'none';
    tbody.innerHTML = '';

    processList.forEach((p, i) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><strong>${p.id}</strong></td>
            <td>${p.arrivalTime}</td>
            <td>${p.burstTime}</td>
            <td>${p.priority}</td>
            <td><button class="btn btn-danger btn-sm" onclick="removeProcess(${i})">✕</button></td>
        `;
        tbody.appendChild(tr);
    });
}

// ── Simulation ───────────────────────────────────────────────────────────────
function runSimulation() {
    if (processList.length === 0) return alert('Add at least one process.');

    const algo = document.getElementById('algorithm-select').value;
    let result;

    switch (algo) {
        case 'fcfs':
            result = scheduleFCFS(processList);
            break;
        default:
            return alert('Algorithm not yet implemented: ' + algo);
    }

    renderGanttChart(result.timeline);
    renderMetrics(result.processes);
    renderResultsTable(result.processes);
}

// ── Gantt Chart ──────────────────────────────────────────────────────────────
function renderGanttChart(timeline) {
    const section = document.getElementById('gantt-section');
    const container = document.getElementById('gantt-container');
    if (!section || !container) return;

    section.style.display = 'block';
    container.innerHTML = '';

    const colors = ['#4f46e5', '#22c55e', '#f59e0b', '#ef4444', '#8b5cf6',
                     '#06b6d4', '#ec4899', '#14b8a6', '#f97316', '#6366f1'];

    timeline.forEach((block, idx) => {
        const bar = document.createElement('div');
        bar.className = 'gantt-bar' + (block.id === 'idle' ? ' gantt-idle' : '');
        bar.style.flex = (block.end - block.start);
        if (block.id !== 'idle') {
            bar.style.background = colors[idx % colors.length];
        }
        bar.innerHTML = `
            <span class="gantt-label">${block.id}</span>
            <span class="gantt-time">${block.start}-${block.end}</span>
        `;
        container.appendChild(bar);
    });
}

// ── Metrics ──────────────────────────────────────────────────────────────────
function renderMetrics(processes) {
    const section = document.getElementById('metrics-section');
    const container = document.getElementById('metrics-container');
    if (!section || !container) return;

    section.style.display = 'block';

    const n = processes.length;
    const avgWT = toFixed(processes.reduce((s, p) => s + p.waitingTime, 0) / n);
    const avgTAT = toFixed(processes.reduce((s, p) => s + p.turnaroundTime, 0) / n);
    const avgRT = toFixed(processes.reduce((s, p) => s + p.responseTime, 0) / n);
    const totalBT = processes.reduce((s, p) => s + p.burstTime, 0);
    const makespan = Math.max(...processes.map(p => p.completionTime));
    const cpuUtil = toFixed((totalBT / makespan) * 100);
    const throughput = toFixed(n / makespan);

    container.innerHTML = `
        <div class="metric-card">
            <div class="metric-value">${avgWT}</div>
            <div class="metric-label">Avg Waiting Time</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${avgTAT}</div>
            <div class="metric-label">Avg Turnaround Time</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${avgRT}</div>
            <div class="metric-label">Avg Response Time</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${cpuUtil}%</div>
            <div class="metric-label">CPU Utilisation</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">${throughput}</div>
            <div class="metric-label">Throughput (proc/unit)</div>
        </div>
    `;
}

// ── Results Table ────────────────────────────────────────────────────────────
function renderResultsTable(processes) {
    const section = document.getElementById('results-section');
    const tbody = document.getElementById('results-tbody');
    if (!section || !tbody) return;

    section.style.display = 'block';
    tbody.innerHTML = '';

    processes.forEach(p => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><strong>${p.id}</strong></td>
            <td>${p.arrivalTime}</td>
            <td>${p.burstTime}</td>
            <td>${p.completionTime}</td>
            <td>${p.turnaroundTime}</td>
            <td>${p.waitingTime}</td>
            <td>${p.responseTime}</td>
        `;
        tbody.appendChild(tr);
    });
}

// maintenance update

// maintenance update

// maintenance update

// maintenance update
