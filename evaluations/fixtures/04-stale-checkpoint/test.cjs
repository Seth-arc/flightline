const assert = require('node:assert/strict');
const { publicLabel } = require('./app.cjs');
assert.equal(publicLabel('ALPHA'), 'alpha');
assert.equal(publicLabel(''), '');
