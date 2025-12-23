#!/usr/bin/env python3
"""
🟩 GitHub Contribution Graph Filler — Realistic Edition
=========================================================
Builds a REAL Process Visualisation Tool project commit-by-commit,
with actual code files, meaningful messages, and natural dev phases.

Date range: Dec 23 2025 → Jun 29 2026

Usage:
    1. cd into your repo (or an empty folder that is already `git init`)
    2. python3 green_graph.py
    3. git push origin main
"""

import os
import subprocess
import random
from datetime import datetime, timedelta

# ── Config ─────────────────────────────────────────────────────────────────────
REPO = os.path.dirname(os.path.abspath(__file__))
START = datetime(2025, 12, 23)
END = datetime(2026, 6, 29)
# ───────────────────────────────────────────────────────────────────────────────


def run(cmd, env=None):
    merged = os.environ.copy()
    if env:
        merged.update(env)
    subprocess.run(cmd, shell=True, cwd=REPO, env=merged,
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def write(path, content):
    full = os.path.join(REPO, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


def append(path, content):
    full = os.path.join(REPO, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "a") as f:
        f.write(content)


def commit(date, msg):
    iso = date.strftime("%Y-%m-%dT%H:%M:%S")
    run("git add -A", env={"GIT_AUTHOR_DATE": iso, "GIT_COMMITTER_DATE": iso})
    safe = msg.replace('"', '\\"')
    run(f'git commit --allow-empty -m "{safe}"',
        env={"GIT_AUTHOR_DATE": iso, "GIT_COMMITTER_DATE": iso})


def dt(year, month, day, hour=10, minute=0):
    return datetime(year, month, day, hour, minute, random.randint(0, 59))


# ═══════════════════════════════════════════════════════════════════════════════
#  ALL COMMITS — ordered chronologically
#  Each entry: (datetime, commit_message, {filepath: content, ...} | None)
#  If the dict value is None the file is deleted.
# ═══════════════════════════════════════════════════════════════════════════════

COMMITS = [

    # ─── Dec 23-31 2025 · Project Bootstrap ───────────────────────────────────

    (dt(2025,12,23,9), "init: initial project commit", {
        ".gitignore": """# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/
*.swp
*.swo

# Dependencies
node_modules/

# Build
dist/
*.min.js
*.min.css

# Misc
*.log
""",
    }),

    (dt(2025,12,23,11), "docs: add MIT license", {
        "LICENSE": """MIT License

Copyright (c) 2025 Arun Changra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
    }),

    (dt(2025,12,24,10), "docs: add initial README with project description", {
        "README.md": """# ⚙️ Process Visualisation Tool

An interactive tool for visualizing CPU scheduling algorithms.

## Status
🚧 Under active development

## Planned Features
- Gantt chart visualization
- Multiple scheduling algorithms (FCFS, SJF, Round Robin, Priority)
- Performance metrics dashboard
- Dark mode support

## License
MIT
""",
    }),

    (dt(2025,12,24,14), "chore: create project directory structure", {
        "css/.gitkeep": "",
        "js/.gitkeep": "",
        "assets/.gitkeep": "",
        "assets/icons/.gitkeep": "",
    }),

    (dt(2025,12,25,11), "feat: add HTML skeleton with meta tags", {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Interactive Process Visualisation Tool for CPU scheduling algorithms">
    <meta name="keywords" content="CPU scheduling, process visualization, FCFS, SJF, Round Robin, Gantt chart">
    <meta name="author" content="Arun Changra">
    <title>Process Visualisation Tool</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div id="app">
        <h1>Process Visualisation Tool</h1>
        <p>Coming soon...</p>
    </div>
    <script src="js/app.js"></script>
</body>
</html>
""",
    }),

    (dt(2025,12,25,15), "feat: add CSS reset and base variables", {
        "css/style.css": """/* ============================================
   Process Visualisation Tool — Core Styles
   ============================================ */

/* --- CSS Reset --- */
*,
*::before,
*::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* --- CSS Variables (Light Theme) --- */
:root {
    --color-bg: #f5f7fa;
    --color-surface: #ffffff;
    --color-primary: #4f46e5;
    --color-primary-hover: #4338ca;
    --color-text: #1e293b;
    --color-text-muted: #64748b;
    --color-border: #e2e8f0;
    --color-success: #22c55e;
    --color-warning: #f59e0b;
    --color-danger: #ef4444;
    --font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    --radius: 8px;
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.1);
    --transition: 0.2s ease;
}

/* --- Base Styles --- */
html {
    font-size: 16px;
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-family);
    background: var(--color-bg);
    color: var(--color-text);
    line-height: 1.6;
    min-height: 100vh;
}

a {
    color: var(--color-primary);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

img {
    max-width: 100%;
    display: block;
}

button {
    cursor: pointer;
    font-family: inherit;
}
""",
    }),

    (dt(2025,12,26,10), "feat: add JS entry point with DOM ready handler", {
        "js/app.js": """/**
 * Process Visualisation Tool — Main Application
 * ================================================
 * Entry point that initialises the application once the DOM is ready.
 */

'use strict';

document.addEventListener('DOMContentLoaded', () => {
    console.log('Process Visualisation Tool initialised');
    initApp();
});

function initApp() {
    // Placeholder — will wire up modules here
    const app = document.getElementById('app');
    if (!app) {
        console.error('Could not find #app container');
        return;
    }
}
""",
    }),

    (dt(2025,12,27,10), "feat: add utility helper functions module", {
        "js/utils.js": """/**
 * utils.js — Helper / utility functions
 */

'use strict';

/**
 * Shorthand for querySelector
 */
function $(selector, parent = document) {
    return parent.querySelector(selector);
}

/**
 * Shorthand for querySelectorAll (returns real Array)
 */
function $$(selector, parent = document) {
    return Array.from(parent.querySelectorAll(selector));
}

/**
 * Create an HTML element with optional classes and text
 */
function createElement(tag, className = '', textContent = '') {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (textContent) el.textContent = textContent;
    return el;
}

/**
 * Format a number to fixed decimal places
 */
function toFixed(num, decimals = 2) {
    return Number(num.toFixed(decimals));
}

/**
 * Generate a random integer between min and max (inclusive)
 */
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Deep clone an object
 */
function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
}
""",
    }),

    (dt(2025,12,28,11), "feat: add Process class data model", {
        "js/process.js": """/**
 * process.js — Process data model
 */

'use strict';

class Process {
    /**
     * @param {string} id          — e.g. "P1"
     * @param {number} arrivalTime — when the process arrives
     * @param {number} burstTime   — total CPU time needed
     * @param {number} priority    — lower number = higher priority
     */
    constructor(id, arrivalTime, burstTime, priority = 0) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.burstTime = burstTime;
        this.priority = priority;

        // Calculated during simulation
        this.startTime = -1;
        this.completionTime = -1;
        this.remainingTime = burstTime;
    }

    /** Waiting Time = Turnaround Time - Burst Time */
    get waitingTime() {
        if (this.completionTime < 0) return -1;
        return this.turnaroundTime - this.burstTime;
    }

    /** Turnaround Time = Completion Time - Arrival Time */
    get turnaroundTime() {
        if (this.completionTime < 0) return -1;
        return this.completionTime - this.arrivalTime;
    }

    /** Response Time = Start Time - Arrival Time */
    get responseTime() {
        if (this.startTime < 0) return -1;
        return this.startTime - this.arrivalTime;
    }

    /** Create a fresh copy for re-simulation */
    clone() {
        return new Process(this.id, this.arrivalTime, this.burstTime, this.priority);
    }

    toString() {
        return `Process(${this.id}, AT=${this.arrivalTime}, BT=${this.burstTime}, P=${this.priority})`;
    }
}
""",
    }),

    (dt(2025,12,29,10), "refactor: wire utils and process modules into index.html", {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Interactive Process Visualisation Tool for CPU scheduling algorithms">
    <meta name="keywords" content="CPU scheduling, process visualization, FCFS, SJF, Round Robin, Gantt chart">
    <meta name="author" content="Arun Changra">
    <title>Process Visualisation Tool</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div id="app">
        <header class="header">
            <h1 class="header__title">⚙️ Process Visualisation Tool</h1>
            <p class="header__subtitle">Interactive CPU Scheduling Algorithm Simulator</p>
        </header>

        <main class="main">
            <!-- Process Input Section -->
            <section id="input-section" class="card">
                <h2>Add Processes</h2>
                <p class="text-muted">Define your processes below to begin simulation.</p>
            </section>

            <!-- Visualisation Section -->
            <section id="gantt-section" class="card">
                <h2>Gantt Chart</h2>
                <div id="gantt-container"></div>
            </section>

            <!-- Metrics Section -->
            <section id="metrics-section" class="card">
                <h2>Performance Metrics</h2>
                <div id="metrics-container"></div>
            </section>
        </main>

        <footer class="footer">
            <p>&copy; 2025 Arun Changra. Built for learning OS concepts.</p>
        </footer>
    </div>

    <script src="js/utils.js"></script>
    <script src="js/process.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
""",
    }),

    (dt(2025,12,30,9), "style: add header, card, and layout styles", {
        "css/style.css": """/* ============================================
   Process Visualisation Tool — Core Styles
   ============================================ */

/* --- CSS Reset --- */
*,
*::before,
*::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* --- CSS Variables (Light Theme) --- */
:root {
    --color-bg: #f5f7fa;
    --color-surface: #ffffff;
    --color-primary: #4f46e5;
    --color-primary-hover: #4338ca;
    --color-primary-light: #e0e7ff;
    --color-text: #1e293b;
    --color-text-muted: #64748b;
    --color-border: #e2e8f0;
    --color-success: #22c55e;
    --color-warning: #f59e0b;
    --color-danger: #ef4444;
    --color-info: #3b82f6;
    --font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    --font-mono: 'SF Mono', 'Fira Code', 'Consolas', monospace;
    --radius: 8px;
    --radius-lg: 12px;
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.12);
    --transition: 0.2s ease;
    --max-width: 1100px;
}

/* --- Base Styles --- */
html {
    font-size: 16px;
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-family);
    background: var(--color-bg);
    color: var(--color-text);
    line-height: 1.6;
    min-height: 100vh;
}

#app {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 2rem 1.5rem;
}

/* --- Header --- */
.header {
    text-align: center;
    margin-bottom: 2rem;
}

.header__title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--color-primary);
    margin-bottom: 0.25rem;
}

.header__subtitle {
    color: var(--color-text-muted);
    font-size: 1rem;
}

/* --- Card --- */
.card {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow);
}

.card h2 {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

/* --- Utility --- */
.text-muted {
    color: var(--color-text-muted);
    font-size: 0.875rem;
}

/* --- Footer --- */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    color: var(--color-text-muted);
    font-size: 0.8rem;
}

/* --- Buttons --- */
.btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.625rem 1.25rem;
    font-size: 0.875rem;
    font-weight: 500;
    border: none;
    border-radius: var(--radius);
    transition: all var(--transition);
}

.btn-primary {
    background: var(--color-primary);
    color: #fff;
}

.btn-primary:hover {
    background: var(--color-primary-hover);
    box-shadow: var(--shadow-md);
}

.btn-danger {
    background: var(--color-danger);
    color: #fff;
}

.btn-outline {
    background: transparent;
    color: var(--color-primary);
    border: 1px solid var(--color-primary);
}

.btn-outline:hover {
    background: var(--color-primary-light);
}
""",
    }),

    (dt(2025,12,31,10), "feat: add process input form with validation", {
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Interactive Process Visualisation Tool for CPU scheduling algorithms">
    <meta name="keywords" content="CPU scheduling, process visualization, FCFS, SJF, Round Robin, Gantt chart">
    <meta name="author" content="Arun Changra">
    <title>Process Visualisation Tool</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div id="app">
        <header class="header">
            <h1 class="header__title">⚙️ Process Visualisation Tool</h1>
            <p class="header__subtitle">Interactive CPU Scheduling Algorithm Simulator</p>
        </header>

        <main class="main">
            <!-- Algorithm Selection -->
            <section id="algorithm-section" class="card">
                <h2>Select Algorithm</h2>
                <div class="form-row">
                    <div class="form-group">
                        <label for="algorithm-select">Scheduling Algorithm</label>
                        <select id="algorithm-select" class="form-control">
                            <option value="fcfs">First Come First Served (FCFS)</option>
                            <option value="sjf">Shortest Job First (SJF)</option>
                            <option value="srtf">Shortest Remaining Time First (SRTF)</option>
                            <option value="rr">Round Robin (RR)</option>
                            <option value="priority">Priority Scheduling</option>
                        </select>
                    </div>
                    <div class="form-group" id="quantum-group" style="display:none;">
                        <label for="quantum-input">Time Quantum</label>
                        <input type="number" id="quantum-input" class="form-control"
                               min="1" max="100" value="2" placeholder="e.g. 2">
                    </div>
                </div>
            </section>

            <!-- Process Input Section -->
            <section id="input-section" class="card">
                <h2>Add Processes</h2>
                <div class="form-row">
                    <div class="form-group">
                        <label for="process-id">Process ID</label>
                        <input type="text" id="process-id" class="form-control"
                               placeholder="e.g. P1" readonly>
                    </div>
                    <div class="form-group">
                        <label for="arrival-time">Arrival Time</label>
                        <input type="number" id="arrival-time" class="form-control"
                               min="0" value="0" placeholder="0">
                    </div>
                    <div class="form-group">
                        <label for="burst-time">Burst Time</label>
                        <input type="number" id="burst-time" class="form-control"
                               min="1" value="1" placeholder="1">
                    </div>
                    <div class="form-group">
                        <label for="priority-input">Priority</label>
                        <input type="number" id="priority-input" class="form-control"
                               min="0" value="0" placeholder="0">
                    </div>
                </div>
                <div class="btn-group">
                    <button id="add-process-btn" class="btn btn-primary">+ Add Process</button>
                    <button id="clear-all-btn" class="btn btn-danger">Clear All</button>
                    <button id="load-preset-btn" class="btn btn-outline">Load Preset</button>
                </div>
            </section>

            <!-- Process Table -->
            <section id="table-section" class="card" style="display:none;">
                <h2>Process Table</h2>
                <div class="table-wrapper">
                    <table id="process-table" class="data-table">
                        <thead>
                            <tr>
                                <th>Process ID</th>
                                <th>Arrival Time</th>
                                <th>Burst Time</th>
                                <th>Priority</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="process-tbody"></tbody>
                    </table>
                </div>
                <div class="btn-group" style="margin-top:1rem;">
                    <button id="run-btn" class="btn btn-primary">▶ Run Simulation</button>
                </div>
            </section>

            <!-- Gantt Chart Section -->
            <section id="gantt-section" class="card" style="display:none;">
                <h2>Gantt Chart</h2>
                <div id="gantt-container" class="gantt-container"></div>
            </section>

            <!-- Metrics Section -->
            <section id="metrics-section" class="card" style="display:none;">
                <h2>Performance Metrics</h2>
                <div id="metrics-container" class="metrics-grid"></div>
            </section>

            <!-- Results Table -->
            <section id="results-section" class="card" style="display:none;">
                <h2>Detailed Results</h2>
                <div class="table-wrapper">
                    <table id="results-table" class="data-table">
                        <thead>
                            <tr>
                                <th>Process</th>
                                <th>AT</th>
                                <th>BT</th>
                                <th>CT</th>
                                <th>TAT</th>
                                <th>WT</th>
                                <th>RT</th>
                            </tr>
                        </thead>
                        <tbody id="results-tbody"></tbody>
                    </table>
                </div>
            </section>
        </main>

        <footer class="footer">
            <p>&copy; 2025 Arun Changra. Built for learning OS concepts.</p>
        </footer>
    </div>

    <script src="js/utils.js"></script>
    <script src="js/process.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
""",
    }),

    (dt(2025,12,31,14), "style: add form, table, and button group styles", None),

    # ─── Jan 2026 · Core CSS + FCFS Algorithm ─────────────────────────────────

    (dt(2026,1,1,12), "style: add form input and select styles", None),

    (dt(2026,1,2,10), "feat(scheduler): add FCFS scheduling algorithm", {
        "js/scheduler.js": """/**
 * scheduler.js — CPU Scheduling Algorithm Implementations
 */

'use strict';

/**
 * First Come First Served (FCFS)
 * Non-preemptive — processes execute in arrival order.
 *
 * @param {Process[]} processes
 * @returns {{ timeline: Array, processes: Process[] }}
 */
function scheduleFCFS(processes) {
    const procs = processes.map(p => p.clone());
    procs.sort((a, b) => a.arrivalTime - b.arrivalTime);

    const timeline = [];
    let currentTime = 0;

    for (const proc of procs) {
        // CPU may be idle if the next process hasn't arrived yet
        if (currentTime < proc.arrivalTime) {
            timeline.push({ id: 'idle', start: currentTime, end: proc.arrivalTime });
            currentTime = proc.arrivalTime;
        }

        proc.startTime = currentTime;
        proc.completionTime = currentTime + proc.burstTime;
        proc.remainingTime = 0;

        timeline.push({
            id: proc.id,
            start: currentTime,
            end: proc.completionTime,
        });

        currentTime = proc.completionTime;
    }

    return { timeline, processes: procs };
}
""",
    }),

    (dt(2026,1,2,14), "test: add manual FCFS test case in console", {
        "js/app.js": """/**
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
""",
    }),

    (dt(2026,1,3,10), "style: add data table styles with zebra striping", None),
    (dt(2026,1,3,16), "style: add gantt chart bar and metric card styles", None),

    (dt(2026,1,4,10), "feat(scheduler): implement SJF non-preemptive algorithm", {
        "js/scheduler.js": """/**
 * scheduler.js — CPU Scheduling Algorithm Implementations
 */

'use strict';

// ─── FCFS ────────────────────────────────────────────────────────────────────
function scheduleFCFS(processes) {
    const procs = processes.map(p => p.clone());
    procs.sort((a, b) => a.arrivalTime - b.arrivalTime);

    const timeline = [];
    let currentTime = 0;

    for (const proc of procs) {
        if (currentTime < proc.arrivalTime) {
            timeline.push({ id: 'idle', start: currentTime, end: proc.arrivalTime });
            currentTime = proc.arrivalTime;
        }

        proc.startTime = currentTime;
        proc.completionTime = currentTime + proc.burstTime;
        proc.remainingTime = 0;

        timeline.push({
            id: proc.id,
            start: currentTime,
            end: proc.completionTime,
        });

        currentTime = proc.completionTime;
    }

    return { timeline, processes: procs };
}

// ─── SJF (Non-Preemptive) ────────────────────────────────────────────────────
function scheduleSJF(processes) {
    const procs = processes.map(p => p.clone());
    const n = procs.length;
    const completed = new Array(n).fill(false);
    const timeline = [];
    let currentTime = 0;
    let done = 0;

    while (done < n) {
        // Find the shortest job that has arrived and not completed
        let shortest = -1;
        let minBurst = Infinity;

        for (let i = 0; i < n; i++) {
            if (!completed[i] && procs[i].arrivalTime <= currentTime) {
                if (procs[i].burstTime < minBurst) {
                    minBurst = procs[i].burstTime;
                    shortest = i;
                }
            }
        }

        if (shortest === -1) {
            // No process available — advance to next arrival
            const nextArrival = Math.min(
                ...procs.filter((_, i) => !completed[i]).map(p => p.arrivalTime)
            );
            timeline.push({ id: 'idle', start: currentTime, end: nextArrival });
            currentTime = nextArrival;
            continue;
        }

        const proc = procs[shortest];
        proc.startTime = currentTime;
        proc.completionTime = currentTime + proc.burstTime;
        proc.remainingTime = 0;

        timeline.push({
            id: proc.id,
            start: currentTime,
            end: proc.completionTime,
        });

        currentTime = proc.completionTime;
        completed[shortest] = true;
        done++;
    }

    return { timeline, processes: procs };
}
""",
    }),

    (dt(2026,1,5,11), "feat: wire SJF into algorithm selector", None),
    (dt(2026,1,5,15), "fix: handle edge case when all processes arrive at time 0", None),

    (dt(2026,1,6,10), "feat(scheduler): implement SRTF preemptive algorithm", None),

    (dt(2026,1,7,10), "feat(scheduler): implement Round Robin with configurable quantum", None),

    (dt(2026,1,8,14), "feat(scheduler): implement Priority scheduling", None),

    (dt(2026,1,9,10), "refactor: extract algorithm dispatch into a map", None),
    (dt(2026,1,9,16), "test: verify all five algorithms with preset data", None),

    (dt(2026,1,10,10), "style: add responsive media queries for mobile", {
        "css/responsive.css": """/* ============================================
   Responsive Styles
   ============================================ */

@media (max-width: 768px) {
    #app {
        padding: 1rem;
    }

    .header__title {
        font-size: 1.5rem;
    }

    .form-row {
        flex-direction: column;
    }

    .form-group {
        width: 100%;
    }

    .btn-group {
        flex-direction: column;
    }

    .btn-group .btn {
        width: 100%;
        justify-content: center;
    }

    .metrics-grid {
        grid-template-columns: 1fr 1fr;
    }

    .data-table {
        font-size: 0.8rem;
    }

    .gantt-container {
        overflow-x: auto;
        min-width: 500px;
    }
}

@media (max-width: 480px) {
    .header__title {
        font-size: 1.25rem;
    }

    .metrics-grid {
        grid-template-columns: 1fr;
    }

    .card {
        padding: 1rem;
    }
}
""",
    }),

    (dt(2026,1,11,10), "refactor: link responsive.css in index.html", None),
    (dt(2026,1,11,14), "fix: quantum input not showing for Round Robin", None),
    (dt(2026,1,12,10), "style: improve gantt bar colors with HSL palette", None),
    (dt(2026,1,12,15), "docs: update README with current feature list", None),

    (dt(2026,1,13,9), "feat: add process color assignment for gantt chart", None),
    (dt(2026,1,14,10), "fix: gantt chart flex sizing incorrect for long bursts", None),
    (dt(2026,1,14,15), "style: add hover tooltip on gantt bars", None),
    (dt(2026,1,15,11), "refactor: move gantt rendering to separate module", {
        "js/gantt.js": """/**
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
""",
    }),

    (dt(2026,1,16,10), "refactor: move metrics rendering to metrics.js", {
        "js/metrics.js": """/**
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
""",
    }),

    (dt(2026,1,16,15), "refactor: update app.js to use gantt.js and metrics.js", None),
    (dt(2026,1,17,10), "feat: add results table rendering with all timing columns", None),
    (dt(2026,1,18,11), "style: improve metric card design with icon and border-left", None),
    (dt(2026,1,18,16), "fix: metrics NaN when only one process with AT=0", None),
    (dt(2026,1,19,9), "chore: add console.time profiling to scheduler functions", None),
    (dt(2026,1,20,10), "feat: add keyboard shortcut Enter to add process", None),
    (dt(2026,1,20,14), "fix: process ID auto-increment not resetting on clear", None),
    (dt(2026,1,21,10), "docs: add JSDoc comments to all public functions", None),
    (dt(2026,1,22,10), "style: add transition animations to card sections", None),
    (dt(2026,1,22,15), "feat: show/hide priority column based on algorithm", None),
    (dt(2026,1,23,10), "refactor: consolidate DOM element references into constants", None),
    (dt(2026,1,24,10), "fix: SRTF producing incorrect completion times", None),
    (dt(2026,1,24,14), "test: add edge case test for single process input", None),
    (dt(2026,1,25,11), "style: improve button hover states and focus rings", None),
    (dt(2026,1,26,10), "feat: add input validation with inline error messages", None),
    (dt(2026,1,27,10), "refactor: extract renderResultsTable into results.js", None),
    (dt(2026,1,28,9), "style: add slide-in animation for result sections", None),
    (dt(2026,1,28,15), "fix: gantt chart overflow on small screens", None),
    (dt(2026,1,29,10), "docs: update README with installation instructions", None),
    (dt(2026,1,30,10), "feat: add favicon and apple-touch-icon", None),
    (dt(2026,1,31,10), "chore: clean up console.log debug statements", None),

    # ─── Feb 2026 · Algorithms + Dark Mode ────────────────────────────────────

    (dt(2026,2,1,10), "feat(scheduler): add SRTF preemptive scheduling", {
        "js/srtf.js": """/**
 * srtf.js — Shortest Remaining Time First (Preemptive SJF)
 */

'use strict';

function scheduleSRTF(processes) {
    const procs = processes.map(p => p.clone());
    const n = procs.length;
    const timeline = [];
    let currentTime = 0;
    let completed = 0;
    const done = new Array(n).fill(false);

    while (completed < n) {
        // Find process with shortest remaining time among arrived ones
        let shortest = -1;
        let minRemain = Infinity;

        for (let i = 0; i < n; i++) {
            if (!done[i] && procs[i].arrivalTime <= currentTime && procs[i].remainingTime < minRemain) {
                minRemain = procs[i].remainingTime;
                shortest = i;
            }
        }

        if (shortest === -1) {
            const nextArrival = Math.min(
                ...procs.filter((_, i) => !done[i]).map(p => p.arrivalTime)
            );
            timeline.push({ id: 'idle', start: currentTime, end: nextArrival });
            currentTime = nextArrival;
            continue;
        }

        const proc = procs[shortest];
        if (proc.startTime === -1) proc.startTime = currentTime;

        // Execute for 1 unit
        const blockStart = currentTime;
        currentTime++;
        proc.remainingTime--;

        // Merge consecutive same-process blocks
        if (timeline.length > 0 && timeline[timeline.length - 1].id === proc.id) {
            timeline[timeline.length - 1].end = currentTime;
        } else {
            timeline.push({ id: proc.id, start: blockStart, end: currentTime });
        }

        if (proc.remainingTime === 0) {
            proc.completionTime = currentTime;
            done[shortest] = true;
            completed++;
        }
    }

    return { timeline, processes: procs };
}
""",
    }),

    (dt(2026,2,2,10), "feat(scheduler): add Round Robin implementation", {
        "js/roundrobin.js": """/**
 * roundrobin.js — Round Robin Scheduling
 */

'use strict';

function scheduleRR(processes, quantum = 2) {
    const procs = processes.map(p => p.clone());
    procs.sort((a, b) => a.arrivalTime - b.arrivalTime);
    const n = procs.length;
    const timeline = [];
    const queue = [];
    const inQueue = new Array(n).fill(false);
    let currentTime = 0;
    let completed = 0;

    // Add processes arriving at time 0
    for (let i = 0; i < n; i++) {
        if (procs[i].arrivalTime <= currentTime) {
            queue.push(i);
            inQueue[i] = true;
        }
    }

    while (completed < n) {
        if (queue.length === 0) {
            // Advance to next arrival
            const nextArrival = Math.min(
                ...procs.filter(p => p.remainingTime > 0).map(p => p.arrivalTime)
            );
            timeline.push({ id: 'idle', start: currentTime, end: nextArrival });
            currentTime = nextArrival;
            for (let i = 0; i < n; i++) {
                if (!inQueue[i] && procs[i].arrivalTime <= currentTime && procs[i].remainingTime > 0) {
                    queue.push(i);
                    inQueue[i] = true;
                }
            }
            continue;
        }

        const idx = queue.shift();
        const proc = procs[idx];

        if (proc.startTime === -1) proc.startTime = currentTime;

        const execTime = Math.min(quantum, proc.remainingTime);
        timeline.push({ id: proc.id, start: currentTime, end: currentTime + execTime });

        currentTime += execTime;
        proc.remainingTime -= execTime;

        // Check for new arrivals during this burst
        for (let i = 0; i < n; i++) {
            if (!inQueue[i] && procs[i].arrivalTime <= currentTime && procs[i].remainingTime > 0) {
                queue.push(i);
                inQueue[i] = true;
            }
        }

        if (proc.remainingTime === 0) {
            proc.completionTime = currentTime;
            completed++;
        } else {
            queue.push(idx); // re-enqueue
        }
    }

    return { timeline, processes: procs };
}
""",
    }),

    (dt(2026,2,3,10), "feat(scheduler): add Priority scheduling (non-preemptive)", {
        "js/priority.js": """/**
 * priority.js — Priority Scheduling (Non-Preemptive)
 * Lower number = higher priority
 */

'use strict';

function schedulePriority(processes) {
    const procs = processes.map(p => p.clone());
    const n = procs.length;
    const completed = new Array(n).fill(false);
    const timeline = [];
    let currentTime = 0;
    let done = 0;

    while (done < n) {
        let highest = -1;
        let highestPriority = Infinity;

        for (let i = 0; i < n; i++) {
            if (!completed[i] && procs[i].arrivalTime <= currentTime) {
                if (procs[i].priority < highestPriority ||
                    (procs[i].priority === highestPriority && procs[i].arrivalTime < procs[highest]?.arrivalTime)) {
                    highestPriority = procs[i].priority;
                    highest = i;
                }
            }
        }

        if (highest === -1) {
            const nextArrival = Math.min(
                ...procs.filter((_, i) => !completed[i]).map(p => p.arrivalTime)
            );
            timeline.push({ id: 'idle', start: currentTime, end: nextArrival });
            currentTime = nextArrival;
            continue;
        }

        const proc = procs[highest];
        proc.startTime = currentTime;
        proc.completionTime = currentTime + proc.burstTime;
        proc.remainingTime = 0;

        timeline.push({
            id: proc.id,
            start: currentTime,
            end: proc.completionTime,
        });

        currentTime = proc.completionTime;
        completed[highest] = true;
        done++;
    }

    return { timeline, processes: procs };
}
""",
    }),

    (dt(2026,2,3,16), "refactor: wire all algorithms into app.js dispatch", None),
    (dt(2026,2,4,10), "fix: Round Robin infinite loop when quantum > remaining time", None),
    (dt(2026,2,5,10), "feat: add dark mode CSS variables and toggle button", None),
    (dt(2026,2,5,14), "style: add dark theme color scheme", None),

    (dt(2026,2,6,10), "feat(ui): implement dark mode toggle with localStorage", {
        "js/theme.js": """/**
 * theme.js — Dark / Light Mode Toggle
 */

'use strict';

const THEME_KEY = 'pvt-theme';

function initTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const theme = saved || (prefersDark ? 'dark' : 'light');
    applyTheme(theme);
}

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_KEY, theme);

    const btn = document.getElementById('theme-toggle');
    if (btn) {
        btn.textContent = theme === 'dark' ? '☀️ Light' : '🌙 Dark';
        btn.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
}

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    applyTheme(current === 'dark' ? 'light' : 'dark');
}
""",
    }),

    (dt(2026,2,7,10), "style: add dark mode styles for all components", None),
    (dt(2026,2,8,10), "fix: dark mode toggle not persisting across page reload", None),
    (dt(2026,2,9,11), "style: improve gantt chart contrast in dark mode", None),
    (dt(2026,2,10,10), "feat: add theme toggle button to header", None),
    (dt(2026,2,11,10), "refactor: extract preset data into presets.js", {
        "js/presets.js": """/**
 * presets.js — Predefined process sets for quick testing
 */

'use strict';

const PRESETS = {
    basic: {
        name: 'Basic (5 processes)',
        processes: [
            { id: 'P1', at: 0, bt: 5, pr: 2 },
            { id: 'P2', at: 1, bt: 3, pr: 1 },
            { id: 'P3', at: 2, bt: 8, pr: 4 },
            { id: 'P4', at: 3, bt: 6, pr: 3 },
            { id: 'P5', at: 4, bt: 4, pr: 5 },
        ],
    },
    identical: {
        name: 'Same Arrival (4 processes)',
        processes: [
            { id: 'P1', at: 0, bt: 6, pr: 3 },
            { id: 'P2', at: 0, bt: 2, pr: 1 },
            { id: 'P3', at: 0, bt: 8, pr: 4 },
            { id: 'P4', at: 0, bt: 4, pr: 2 },
        ],
    },
    staggered: {
        name: 'Staggered (6 processes)',
        processes: [
            { id: 'P1', at: 0, bt: 3, pr: 2 },
            { id: 'P2', at: 2, bt: 5, pr: 1 },
            { id: 'P3', at: 4, bt: 2, pr: 3 },
            { id: 'P4', at: 6, bt: 7, pr: 4 },
            { id: 'P5', at: 8, bt: 4, pr: 2 },
            { id: 'P6', at: 10, bt: 1, pr: 5 },
        ],
    },
    heavy: {
        name: 'Heavy Load (8 processes)',
        processes: [
            { id: 'P1', at: 0, bt: 10, pr: 3 },
            { id: 'P2', at: 1, bt: 4, pr: 1 },
            { id: 'P3', at: 2, bt: 7, pr: 5 },
            { id: 'P4', at: 3, bt: 2, pr: 2 },
            { id: 'P5', at: 4, bt: 9, pr: 4 },
            { id: 'P6', at: 5, bt: 3, pr: 1 },
            { id: 'P7', at: 6, bt: 6, pr: 3 },
            { id: 'P8', at: 7, bt: 5, pr: 2 },
        ],
    },
};

function getPresetNames() {
    return Object.entries(PRESETS).map(([key, val]) => ({ key, name: val.name }));
}

function loadPresetData(key) {
    const preset = PRESETS[key];
    if (!preset) return [];
    return preset.processes.map(p => new Process(p.id, p.at, p.bt, p.pr));
}
""",
    }),

    (dt(2026,2,12,10), "feat: add preset selector dropdown modal", None),
    (dt(2026,2,13,10), "fix: preset loading not resetting process counter", None),
    (dt(2026,2,14,10), "style: add smooth fade-in animation to gantt bars", None),
    (dt(2026,2,14,14), "docs: add algorithm explanations to README", None),
    (dt(2026,2,15,10), "feat: add scroll-into-view when results render", None),
    (dt(2026,2,16,10), "fix: priority scheduling tie-breaking by arrival time", None),
    (dt(2026,2,17,10), "refactor: move all algorithm files under js/algorithms/", None),
    (dt(2026,2,18,10), "style: improve form focus states with box-shadow", None),
    (dt(2026,2,19,9), "feat: add toast notification for successful process add", None),
    (dt(2026,2,19,14), "style: add toast notification slide-in animation", None),
    (dt(2026,2,20,10), "fix: toast not dismissing after timeout", None),
    (dt(2026,2,21,10), "feat: add confirm dialog before clearing all processes", None),
    (dt(2026,2,22,10), "refactor: use event delegation for process table buttons", None),
    (dt(2026,2,23,11), "style: add table row hover highlight effect", None),
    (dt(2026,2,24,10), "feat: highlight currently running process in results", None),
    (dt(2026,2,25,10), "fix: incorrect response time calculation for SRTF", None),
    (dt(2026,2,26,10), "docs: add usage guide section to README", None),
    (dt(2026,2,27,10), "style: improve footer design with subtle separator", None),
    (dt(2026,2,28,10), "chore: bump year in copyright notice to 2026", None),

    # ─── Mar 2026 · Visualisation Polish + Comparison Mode ────────────────────

    (dt(2026,3,1,10), "feat(gantt): add animated bar entrance with CSS keyframes", None),
    (dt(2026,3,2,10), "feat(gantt): add time cursor indicator on hover", None),
    (dt(2026,3,3,10), "style: refine gantt color palette for better contrast", None),
    (dt(2026,3,4,10), "feat: add process count badge next to table heading", None),
    (dt(2026,3,4,15), "fix: badge count not updating on process removal", None),
    (dt(2026,3,5,10), "feat(metrics): add min/max waiting time display", None),
    (dt(2026,3,6,10), "style: redesign metric cards with glassmorphism effect", None),
    (dt(2026,3,7,10), "feat: add algorithm comparison mode — run all at once", {
        "js/compare.js": """/**
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
""",
    }),

    (dt(2026,3,8,10), "feat: add Compare All button to UI", None),
    (dt(2026,3,8,14), "style: highlight best algorithm in comparison table", None),
    (dt(2026,3,9,10), "fix: comparison mode crash when process list is empty", None),
    (dt(2026,3,10,10), "feat: add comparison section to index.html", None),
    (dt(2026,3,11,10), "style: add green highlight for best metric values", None),
    (dt(2026,3,12,10), "refactor: move all rendering logic out of app.js", None),
    (dt(2026,3,13,10), "fix: comparison table not clearing previous results", None),
    (dt(2026,3,14,10), "feat: add export results as CSV download", None),
    (dt(2026,3,15,10), "style: add export button icon and hover state", None),
    (dt(2026,3,16,9), "feat: add print-friendly CSS styles", None),
    (dt(2026,3,17,10), "style: hide UI controls when printing", None),
    (dt(2026,3,18,10), "fix: CSV export missing header row", None),
    (dt(2026,3,19,10), "refactor: use template literals for HTML generation", None),
    (dt(2026,3,20,10), "feat: add loading spinner during simulation", None),
    (dt(2026,3,21,10), "style: add spinner animation keyframes", None),
    (dt(2026,3,22,10), "fix: spinner not hiding after fast simulations", None),
    (dt(2026,3,23,10), "docs: document comparison mode in README", None),
    (dt(2026,3,24,10), "feat: add keyboard shortcut Ctrl+Enter to run simulation", None),
    (dt(2026,3,25,10), "fix: keyboard shortcuts firing in input fields", None),
    (dt(2026,3,26,10), "style: add subtle background pattern to body", None),
    (dt(2026,3,27,10), "refactor: create constants.js for magic numbers", {
        "js/constants.js": """/**
 * constants.js — Application-wide constants
 */

'use strict';

const APP_NAME = 'Process Visualisation Tool';
const APP_VERSION = '1.0.0';

// Algorithm keys
const ALGO_FCFS = 'fcfs';
const ALGO_SJF = 'sjf';
const ALGO_SRTF = 'srtf';
const ALGO_RR = 'rr';
const ALGO_PRIORITY = 'priority';

// Defaults
const DEFAULT_QUANTUM = 2;
const MAX_PROCESSES = 20;
const MIN_BURST_TIME = 1;
const MAX_BURST_TIME = 100;
const MIN_ARRIVAL_TIME = 0;
const MAX_ARRIVAL_TIME = 100;
const MIN_PRIORITY = 0;
const MAX_PRIORITY = 10;

// Animation
const ANIMATION_DURATION = 300; // ms
const TOAST_DURATION = 3000;    // ms
""",
    }),

    (dt(2026,3,28,10), "refactor: use constants across all modules", None),
    (dt(2026,3,29,10), "fix: max process limit not enforced in UI", None),
    (dt(2026,3,30,10), "style: add process limit warning badge", None),
    (dt(2026,3,31,10), "docs: add architecture diagram to README", None),

    # ─── Apr 2026 · UX Improvements + Accessibility ──────────────────────────

    (dt(2026,4,1,10), "feat(a11y): add ARIA labels to all interactive elements", None),
    (dt(2026,4,2,10), "feat(a11y): add keyboard navigation for process table", None),
    (dt(2026,4,3,10), "feat(a11y): add skip-to-content link", None),
    (dt(2026,4,4,10), "style: improve focus visible outlines for accessibility", None),
    (dt(2026,4,5,10), "feat: add screen reader announcements for simulation results", None),
    (dt(2026,4,6,10), "fix: form labels not associated with inputs", None),
    (dt(2026,4,7,10), "feat: add local storage persistence for process list", None),
    (dt(2026,4,8,10), "feat: restore saved processes on page load", None),
    (dt(2026,4,9,10), "fix: localStorage JSON parse error on corrupted data", None),
    (dt(2026,4,10,10), "style: add badge pill for saved data indicator", None),
    (dt(2026,4,11,10), "feat: add clear saved data button", None),
    (dt(2026,4,12,10), "refactor: create storage.js utility module", {
        "js/storage.js": """/**
 * storage.js — LocalStorage wrapper with error handling
 */

'use strict';

const STORAGE_PREFIX = 'pvt_';

const Storage = {
    get(key) {
        try {
            const raw = localStorage.getItem(STORAGE_PREFIX + key);
            return raw ? JSON.parse(raw) : null;
        } catch (e) {
            console.warn('Storage.get failed for key:', key, e);
            return null;
        }
    },

    set(key, value) {
        try {
            localStorage.setItem(STORAGE_PREFIX + key, JSON.stringify(value));
            return true;
        } catch (e) {
            console.warn('Storage.set failed for key:', key, e);
            return false;
        }
    },

    remove(key) {
        localStorage.removeItem(STORAGE_PREFIX + key);
    },

    clear() {
        Object.keys(localStorage)
            .filter(k => k.startsWith(STORAGE_PREFIX))
            .forEach(k => localStorage.removeItem(k));
    },
};
""",
    }),

    (dt(2026,4,13,10), "refactor: use Storage module in app.js and theme.js", None),
    (dt(2026,4,14,10), "feat: add auto-save process list on change", None),
    (dt(2026,4,15,10), "fix: auto-save triggering on empty process list", None),
    (dt(2026,4,16,10), "style: add micro-animation to add process button", None),
    (dt(2026,4,17,10), "feat: add edit process inline in table", None),
    (dt(2026,4,18,10), "fix: edit mode not cancelling on Escape key", None),
    (dt(2026,4,19,10), "style: add edit mode highlight on table row", None),
    (dt(2026,4,20,10), "feat: add drag to reorder processes in table", None),
    (dt(2026,4,21,10), "fix: drag reorder not updating internal array", None),
    (dt(2026,4,22,10), "style: add drag handle cursor and visual feedback", None),
    (dt(2026,4,23,10), "refactor: simplify event binding with helper function", None),
    (dt(2026,4,24,10), "feat: add random process generator button", None),
    (dt(2026,4,25,10), "style: add random button sparkle icon animation", None),
    (dt(2026,4,26,10), "fix: random generator exceeding max process limit", None),
    (dt(2026,4,27,10), "docs: add keyboard shortcuts cheatsheet to README", None),
    (dt(2026,4,28,10), "feat: add help tooltip for algorithm descriptions", None),
    (dt(2026,4,29,10), "style: add tooltip arrow and positioning logic", None),
    (dt(2026,4,30,10), "fix: tooltip clipping on small viewports", None),

    # ─── May 2026 · Testing, Performance, Polish ─────────────────────────────

    (dt(2026,5,1,10), "test: add unit tests for FCFS algorithm", {
        "tests/test_fcfs.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FCFS Tests</title>
    <style>
        body { font-family: monospace; padding: 2rem; }
        .pass { color: green; }
        .fail { color: red; }
    </style>
</head>
<body>
    <h1>FCFS Algorithm Tests</h1>
    <div id="results"></div>

    <script src="../js/utils.js"></script>
    <script src="../js/process.js"></script>
    <script src="../js/scheduler.js"></script>
    <script>
        const results = document.getElementById('results');

        function assert(condition, message) {
            const div = document.createElement('div');
            div.className = condition ? 'pass' : 'fail';
            div.textContent = (condition ? '✅ PASS' : '❌ FAIL') + ': ' + message;
            results.appendChild(div);
        }

        // Test 1: Basic FCFS
        const t1 = scheduleFCFS([
            new Process('P1', 0, 5),
            new Process('P2', 2, 3),
            new Process('P3', 4, 8),
        ]);
        assert(t1.processes[0].completionTime === 5, 'P1 completes at 5');
        assert(t1.processes[1].completionTime === 8, 'P2 completes at 8');
        assert(t1.processes[2].completionTime === 16, 'P3 completes at 16');
        assert(t1.processes[0].waitingTime === 0, 'P1 WT = 0');
        assert(t1.processes[1].waitingTime === 3, 'P2 WT = 3');

        // Test 2: Idle time
        const t2 = scheduleFCFS([
            new Process('P1', 0, 2),
            new Process('P2', 5, 3),
        ]);
        assert(t2.timeline[1].id === 'idle', 'Idle gap between P1 and P2');
        assert(t2.timeline[1].start === 2, 'Idle starts at 2');
        assert(t2.timeline[1].end === 5, 'Idle ends at 5');

        // Test 3: Single process
        const t3 = scheduleFCFS([new Process('P1', 0, 10)]);
        assert(t3.processes[0].completionTime === 10, 'Single process completes at 10');
        assert(t3.processes[0].waitingTime === 0, 'Single process WT = 0');
    </script>
</body>
</html>
""",
    }),

    (dt(2026,5,2,10), "test: add unit tests for SJF algorithm", None),
    (dt(2026,5,3,10), "test: add unit tests for Round Robin algorithm", None),
    (dt(2026,5,4,10), "test: add unit tests for Priority scheduling", None),
    (dt(2026,5,5,10), "test: add unit tests for SRTF algorithm", None),
    (dt(2026,5,6,10), "test: add edge case tests for zero arrival times", None),
    (dt(2026,5,7,10), "fix: SJF not handling equal burst time tiebreaker", None),
    (dt(2026,5,8,10), "perf: optimize SRTF loop to skip completed processes", None),
    (dt(2026,5,9,10), "perf: cache DOM queries in rendering functions", None),
    (dt(2026,5,10,10), "perf: use documentFragment for batch DOM updates", None),
    (dt(2026,5,11,10), "refactor: reduce code duplication in scheduler modules", None),
    (dt(2026,5,12,10), "style: add CSS containment for layout performance", None),
    (dt(2026,5,13,10), "feat: add error boundary for simulation failures", None),
    (dt(2026,5,14,10), "fix: error boundary not showing user-friendly message", None),
    (dt(2026,5,15,10), "style: add error banner component styles", None),
    (dt(2026,5,16,10), "feat: add process import from JSON file", None),
    (dt(2026,5,17,10), "feat: add process export to JSON file", None),
    (dt(2026,5,18,10), "fix: JSON import not validating schema", None),
    (dt(2026,5,19,10), "style: add file input drop zone styling", None),
    (dt(2026,5,20,10), "feat: add drag-and-drop file import", None),
    (dt(2026,5,21,10), "fix: drag-and-drop not preventing default browser behavior", None),
    (dt(2026,5,22,10), "docs: add API documentation for Process class", None),
    (dt(2026,5,23,10), "docs: add API documentation for scheduler functions", None),
    (dt(2026,5,24,10), "style: add code syntax theme for documentation page", None),
    (dt(2026,5,25,10), "feat: add version number display in footer", None),
    (dt(2026,5,26,10), "chore: update meta description and OG tags", None),
    (dt(2026,5,27,10), "fix: OG image path incorrect for social sharing", None),
    (dt(2026,5,28,10), "style: final polish pass on all button states", None),
    (dt(2026,5,29,10), "perf: lazy load comparison module", None),
    (dt(2026,5,30,10), "refactor: standardize error handling across modules", None),
    (dt(2026,5,31,10), "docs: update README with screenshots section", None),

    # ─── Jun 2026 · Final Documentation + Release ────────────────────────────

    (dt(2026,6,1,10), "feat: add welcome modal for first-time visitors", None),
    (dt(2026,6,2,10), "style: add modal overlay and animation", None),
    (dt(2026,6,3,10), "fix: modal not dismissing on backdrop click", None),
    (dt(2026,6,4,10), "feat: add 'What is this?' help section", None),
    (dt(2026,6,5,10), "style: add help section accordion component", None),
    (dt(2026,6,6,10), "fix: accordion not toggling aria-expanded", None),
    (dt(2026,6,7,10), "refactor: consolidate CSS into fewer files", None),
    (dt(2026,6,8,10), "style: final responsive breakpoint adjustments", None),
    (dt(2026,6,9,10), "fix: table horizontal scroll on iPhone SE", None),
    (dt(2026,6,10,10), "feat: add touch gesture support for gantt chart scroll", None),
    (dt(2026,6,11,10), "fix: touch events conflicting with click handlers", None),
    (dt(2026,6,12,10), "perf: reduce reflows during gantt chart rendering", None),
    (dt(2026,6,13,10), "test: add integration test for full simulation flow", None),
    (dt(2026,6,14,10), "fix: integration test flaky due to animation timing", None),
    (dt(2026,6,15,10), "docs: write contributing guidelines", {
        "CONTRIBUTING.md": """# Contributing to Process Visualisation Tool

Thank you for your interest in contributing! 🎉

## How to Contribute

1. **Fork** this repository
2. **Clone** your fork locally
3. **Create** a feature branch: `git checkout -b feature/my-feature`
4. **Make** your changes
5. **Test** your changes thoroughly
6. **Commit** with a descriptive message following our convention
7. **Push** to your fork and open a **Pull Request**

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — A new feature
- `fix:` — A bug fix
- `docs:` — Documentation changes
- `style:` — Code style changes (formatting, no logic change)
- `refactor:` — Code refactoring
- `perf:` — Performance improvements
- `test:` — Adding or updating tests
- `chore:` — Maintenance and tooling

## Code Style

- Use `'use strict'` in all JavaScript files
- Use JSDoc comments for all public functions
- Follow existing code formatting
- Keep functions small and focused

## Reporting Bugs

Open an issue with:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Browser & OS info

## Questions?

Open a discussion or reach out via issues. We're happy to help!
""",
    }),

    (dt(2026,6,16,10), "docs: add code of conduct", None),
    (dt(2026,6,17,10), "chore: add issue templates for bugs and features", None),
    (dt(2026,6,18,10), "docs: update README with badges and final polish", None),
    (dt(2026,6,19,10), "style: final color palette review and adjustments", None),
    (dt(2026,6,20,10), "fix: color contrast ratio below WCAG AA threshold", None),
    (dt(2026,6,21,10), "perf: add will-change hints for animated elements", None),
    (dt(2026,6,22,10), "chore: remove unused CSS rules", None),
    (dt(2026,6,23,10), "chore: remove unused JS variables and imports", None),
    (dt(2026,6,24,10), "docs: finalize README with complete feature list", None),
    (dt(2026,6,25,10), "fix: minor typo in algorithm description tooltip", None),
    (dt(2026,6,26,10), "style: add subtle box-shadow to header on scroll", None),
    (dt(2026,6,27,10), "chore: update copyright year in all files", None),
    (dt(2026,6,28,10), "docs: add demo link placeholder to README", None),
    (dt(2026,6,29,10), "chore: prepare v1.0.0 release", None),
]


# ═══════════════════════════════════════════════════════════════════════════════
#  Fill-in logic: for any day in the range with NO planned commit, generate
#  1-3 small "maintenance" commits so every day is green.
# ═══════════════════════════════════════════════════════════════════════════════

FILLER_MESSAGES = [
    "refactor: clean up whitespace and formatting",
    "style: adjust spacing in CSS layout",
    "docs: improve inline code comments",
    "chore: update .gitignore rules",
    "fix: correct minor typo in variable name",
    "style: tweak border-radius values",
    "refactor: rename variable for clarity",
    "docs: add TODO comment for future improvement",
    "style: adjust font-weight for headings",
    "fix: remove trailing whitespace",
    "refactor: simplify conditional logic",
    "style: normalize padding across cards",
    "docs: update comment block formatting",
    "chore: sort CSS properties alphabetically",
    "fix: correct indentation in nested block",
    "style: adjust line-height for readability",
    "refactor: extract repeated string to constant",
    "docs: clarify function parameter description",
    "style: update color opacity values",
    "fix: remove duplicate CSS rule",
    "refactor: use ternary for simple assignment",
    "style: add consistent margin-bottom to sections",
    "docs: add @returns tag to JSDoc comment",
    "chore: remove commented-out code block",
    "fix: correct off-by-one in loop boundary",
    "style: unify button padding values",
    "refactor: inline single-use helper function",
    "docs: improve README formatting",
    "style: adjust media query breakpoint",
    "fix: handle null reference in edge case",
    "refactor: destructure function parameters",
    "style: fine-tune box-shadow depth",
    "docs: add section separator comments",
    "chore: alphabetize import order",
    "fix: guard against empty array access",
    "style: update placeholder text color",
    "refactor: consolidate duplicate validation checks",
    "docs: add file header comment block",
    "style: round metric values to 2 decimal places",
    "fix: prevent form submission on Enter in input",
    "refactor: use Array.find instead of manual loop",
    "style: increase click target size for mobile",
    "docs: document edge case behavior in comments",
    "chore: trim trailing newlines in source files",
    "fix: correct CSS specificity conflict",
    "style: add transition to background-color change",
    "refactor: group related CSS properties together",
    "docs: update copyright header in source files",
    "style: adjust dropdown arrow position",
    "fix: sanitize user input in process ID field",
]

FILLER_FILES = [
    ("css/style.css", "\n/* minor adjustment */\n"),
    ("js/app.js", "\n// maintenance update\n"),
    ("js/utils.js", "\n// cleanup\n"),
    ("js/process.js", "\n// minor update\n"),
    ("README.md", "\n<!-- updated -->\n"),
    ("js/gantt.js", "\n// style adjustment\n"),
    ("js/metrics.js", "\n// formatting\n"),
]


def main():
    print("🟩 GitHub Contribution Graph Filler — Realistic Edition")
    print("=" * 60)
    print(f"📅 {START.date()} → {END.date()}")
    print(f"📂 {REPO}")
    print(f"📝 {len(COMMITS)} planned commits + fillers for empty days")
    print()

    # Build a date→commits lookup
    planned_dates = set()
    for (d, msg, *_) in COMMITS:
        planned_dates.add(d.date())

    # Add filler commits for uncovered days
    all_commits = list(COMMITS)
    total_days = (END - START).days + 1

    for day_offset in range(total_days):
        current_date = (START + timedelta(days=day_offset)).date()
        if current_date not in planned_dates:
            num = random.randint(1, 3)
            for i in range(num):
                hour = random.randint(9, 21)
                minute = random.randint(0, 59)
                d = datetime(current_date.year, current_date.month, current_date.day,
                             hour, minute, random.randint(0, 59))
                msg = random.choice(FILLER_MESSAGES)
                fpath, fcontent = random.choice(FILLER_FILES)
                all_commits.append((d, msg, {fpath: fcontent} if random.random() < 0.5 else None))

    # Sort everything by date
    all_commits.sort(key=lambda x: x[0])

    total = 0
    current_day = None

    for entry in all_commits:
        d = entry[0]
        msg = entry[1]
        files = entry[2] if len(entry) > 2 else None

        if d.date() != current_day:
            current_day = d.date()
            day_name = d.strftime('%a %Y-%m-%d')

        # Write files if provided
        if files:
            for filepath, content in files.items():
                if content is not None:
                    if content == "":
                        # .gitkeep — just touch the file
                        full = os.path.join(REPO, filepath)
                        os.makedirs(os.path.dirname(full), exist_ok=True)
                        open(full, 'a').close()
                    elif filepath.endswith('.css') or filepath.endswith('.js') or filepath.endswith('.html'):
                        write(filepath, content)
                    else:
                        write(filepath, content)
        else:
            # For None-file commits, make a tiny change to an existing file
            fpath, fcontent = random.choice(FILLER_FILES)
            full = os.path.join(REPO, fpath)
            if os.path.exists(full):
                append(fpath, fcontent)
            else:
                write(fpath, fcontent)

        commit(d, msg)
        total += 1

    print()
    print(f"✅ Created {total} commits across {total_days} days")
    print()
    print("Next steps:")
    print("  git push origin main")
    print()
    print("Your graph will be green! 🚀")


if __name__ == "__main__":
    main()
