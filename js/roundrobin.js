/**
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
