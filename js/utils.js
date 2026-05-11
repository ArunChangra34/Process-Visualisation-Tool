/**
 * utils.js — Helper / utility functions
 */

'use strict';

/**
 * Shorthand for querySelector
 */
function $(selector, parent = document) {
    return parent.querySelector(selector);
}

/**
 * Shorthand for querySelectorAll (returns real Array)
 */
function $$(selector, parent = document) {
    return Array.from(parent.querySelectorAll(selector));
}

/**
 * Create an HTML element with optional classes and text
 */
function createElement(tag, className = '', textContent = '') {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (textContent) el.textContent = textContent;
    return el;
}

/**
 * Format a number to fixed decimal places
 */
function toFixed(num, decimals = 2) {
    return Number(num.toFixed(decimals));
}

/**
 * Generate a random integer between min and max (inclusive)
 */
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Deep clone an object
 */
function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
}

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup

// cleanup
