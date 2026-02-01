/**
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
