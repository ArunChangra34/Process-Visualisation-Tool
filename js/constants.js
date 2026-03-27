/**
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
