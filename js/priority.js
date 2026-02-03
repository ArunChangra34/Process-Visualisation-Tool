/**
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
