const assert = require('node:assert/strict');
const { reportLabel } = require('./app.cjs');
assert.equal(reportLabel(' north_team '), 'North Team');
assert.equal(reportLabel(''), '');
