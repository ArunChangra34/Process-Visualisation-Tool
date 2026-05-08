/**
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

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update

// minor update
