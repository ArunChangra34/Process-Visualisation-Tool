<![CDATA[<div align="center">

# ⚙️ Process Visualisation Tool

[![GitHub license](https://img.shields.io/github/license/ArunChangra34/Process-Visualisation-Tool?style=for-the-badge&color=blue)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ArunChangra34/Process-Visualisation-Tool?style=for-the-badge&color=yellow)](https://github.com/ArunChangra34/Process-Visualisation-Tool/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ArunChangra34/Process-Visualisation-Tool?style=for-the-badge&color=green)](https://github.com/ArunChangra34/Process-Visualisation-Tool/network)
[![GitHub issues](https://img.shields.io/github/issues/ArunChangra34/Process-Visualisation-Tool?style=for-the-badge&color=red)](https://github.com/ArunChangra34/Process-Visualisation-Tool/issues)

**A powerful, interactive tool for visualizing and analyzing CPU scheduling algorithms in real-time.**

Built to help developers, students, and system administrators understand process scheduling, resource allocation, and system behavior through intuitive visual representations.

[Features](#-features) · [Installation](#-installation) · [Usage](#-usage) · [Architecture](#-architecture) · [Contributing](#-contributing)

---

</div>

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Scheduling Algorithms](#-scheduling-algorithms)
- [Comparison Mode](#-comparison-mode)
- [Keyboard Shortcuts](#-keyboard-shortcuts)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Gantt Chart Visualization** | Color-coded horizontal bar charts showing process execution timelines with time markers and legends |
| 🧮 **5 Scheduling Algorithms** | FCFS, SJF, SRTF (Preemptive SJF), Round Robin, and Priority Scheduling |
| 📈 **Performance Metrics** | Track avg waiting time, turnaround time, response time, CPU utilization, and throughput |
| ⚖️ **Algorithm Comparison** | Run all algorithms side-by-side with a comparison table highlighting the best performer |
| 🎯 **Interactive Process Input** | Add, edit, remove, and reorder processes with inline table editing and drag-and-drop |
| 🎲 **Preset Scenarios** | Load pre-built process sets (Basic, Same Arrival, Staggered, Heavy Load) for quick testing |
| 🌙 **Dark / Light Mode** | System-aware theme with manual toggle, persisted in localStorage |
| 💾 **Data Persistence** | Process lists auto-save to localStorage and restore on page reload |
| 📱 **Fully Responsive** | Works flawlessly across desktop, tablet, and mobile devices |
| ♿ **Accessible** | ARIA labels, keyboard navigation, focus management, and screen reader support |
| 📤 **Import / Export** | Import processes from JSON, export results as CSV, drag-and-drop file loading |
| 🖨️ **Print-Friendly** | Clean print styles that hide UI controls for report-ready output |

## 🛠 Tech Stack

<div align="center">

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **Visualization** | Custom Gantt chart engine (pure CSS + JS) |
| **Typography** | [Inter](https://fonts.google.com/specimen/Inter) via Google Fonts |
| **Theming** | CSS Custom Properties with `data-theme` attribute |
| **Persistence** | localStorage with error-safe wrapper |
| **Build Tool** | None — zero dependencies, no build step |
| **Version Control** | Git & GitHub |

</div>

## 🚀 Installation

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- [Git](https://git-scm.com/) installed on your machine

### Quick Start

```bash
# Clone the repository
git clone https://github.com/ArunChangra34/Process-Visualisation-Tool.git

# Navigate to the project directory
cd Process-Visualisation-Tool

# Option 1: Open directly in browser
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows

# Option 2: Run with Python's built-in server
python3 -m http.server 8080
# Then visit http://localhost:8080
```

## 💡 Usage

### 1. Add Processes

Create processes manually or load a preset scenario:

```
Process ID:    P1       P2       P3       P4       P5
Arrival Time:  0        1        2        3        4
Burst Time:    5        3        8        6        4
Priority:      2        1        4        3        5
```

### 2. Select Algorithm

Choose from the dropdown:
- **FCFS** — First Come First Served
- **SJF** — Shortest Job First
- **SRTF** — Shortest Remaining Time First
- **RR** — Round Robin (with configurable time quantum)
- **Priority** — Priority Scheduling (lower = higher priority)

### 3. Run Simulation

Click **"▶ Run Simulation"** to generate:
- **Gantt Chart** — color-coded timeline with time markers
- **Metrics Panel** — avg WT, TAT, RT, CPU utilization, throughput
- **Results Table** — per-process completion, turnaround, waiting, and response times

### 4. Compare Algorithms

Click **"Compare All"** to run all 5 algorithms on the same data and see a side-by-side metrics table with the best values highlighted in green.

## 🏗 Architecture

```
Process-Visualisation-Tool/
│
├── index.html                 # Main entry point
│
├── css/
│   ├── style.css              # Core styles, variables, components
│   └── responsive.css         # Media queries for mobile / tablet
│
├── js/
│   ├── app.js                 # Application entry, event binding, state
│   ├── constants.js           # App-wide constants and defaults
│   ├── utils.js               # DOM helpers and utility functions
│   ├── process.js             # Process data model class
│   ├── scheduler.js           # FCFS and SJF algorithms
│   ├── srtf.js                # SRTF preemptive algorithm
│   ├── roundrobin.js          # Round Robin algorithm
│   ├── priority.js            # Priority scheduling algorithm
│   ├── gantt.js               # Gantt chart rendering engine
│   ├── metrics.js             # Metrics calculation and display
│   ├── compare.js             # Algorithm comparison mode
│   ├── presets.js             # Predefined process sets
│   ├── theme.js               # Dark / light mode toggle
│   └── storage.js             # localStorage wrapper
│
├── tests/
│   └── test_fcfs.html         # Browser-based unit tests
│
├── CONTRIBUTING.md            # Contribution guidelines
├── LICENSE                    # MIT License
└── README.md
```

## 📚 Scheduling Algorithms

| Algorithm | Type | Preemptive | Description |
|-----------|------|------------|-------------|
| **FCFS** | Non-preemptive | ❌ | Processes execute in arrival order |
| **SJF** | Non-preemptive | ❌ | Selects the process with the smallest burst time |
| **SRTF** | Preemptive | ✅ | Preemptive version of SJF — re-evaluates at each time unit |
| **Round Robin** | Preemptive | ✅ | Time-sliced execution with configurable quantum |
| **Priority** | Non-preemptive | ❌ | Executes based on priority value (lower = higher priority) |

### Key Metrics

| Metric | Formula |
|--------|---------|
| **Waiting Time (WT)** | Turnaround Time − Burst Time |
| **Turnaround Time (TAT)** | Completion Time − Arrival Time |
| **Response Time (RT)** | Start Time − Arrival Time |
| **CPU Utilization** | (Total Burst Time / Makespan) × 100 |
| **Throughput** | Number of Processes / Makespan |

## ⚖️ Comparison Mode

Run all five algorithms on the same process set and compare:

| Metric | FCFS | SJF | SRTF | RR (q=2) | Priority |
|--------|------|-----|------|----------|----------|
| Avg WT | 4.60 | 3.00 | **2.40** | 5.20 | 3.80 |
| Avg TAT | 9.80 | 8.20 | **7.60** | 10.40 | 9.00 |
| CPU Util | 100% | 100% | 100% | 100% | 100% |

*Best values are highlighted in the UI*

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Add process (when input is focused) |
| `Ctrl + Enter` | Run simulation |
| `Escape` | Cancel edit / close modal |

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a PR.

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** using [Conventional Commits](https://www.conventionalcommits.org/): `git commit -m "feat: add amazing feature"`
4. **Push** and open a Pull Request

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

**Made with ❤️ by [Arun Changra](https://github.com/ArunChangra34)**

⭐ Star this repo if you found it useful!

</div>
]]>
