const assert = require('node:assert/strict');
const { badge } = require('./app.cjs');
assert.equal(badge(), 'ready');
