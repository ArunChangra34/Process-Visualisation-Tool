/**
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
