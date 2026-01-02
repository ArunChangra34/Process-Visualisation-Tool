/**
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
