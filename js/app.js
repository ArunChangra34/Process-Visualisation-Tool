/**
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
