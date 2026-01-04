/**
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
