/**
 * storage.js — LocalStorage wrapper with error handling
 */

'use strict';

const STORAGE_PREFIX = 'pvt_';

const Storage = {
    get(key) {
        try {
            const raw = localStorage.getItem(STORAGE_PREFIX + key);
            return raw ? JSON.parse(raw) : null;
        } catch (e) {
            console.warn('Storage.get failed for key:', key, e);
            return null;
        }
    },

    set(key, value) {
        try {
            localStorage.setItem(STORAGE_PREFIX + key, JSON.stringify(value));
            return true;
        } catch (e) {
            console.warn('Storage.set failed for key:', key, e);
            return false;
        }
    },

    remove(key) {
        localStorage.removeItem(STORAGE_PREFIX + key);
    },

    clear() {
        Object.keys(localStorage)
            .filter(k => k.startsWith(STORAGE_PREFIX))
            .forEach(k => localStorage.removeItem(k));
    },
};
