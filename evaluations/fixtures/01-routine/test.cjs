const assert = require('node:assert/strict');
const { normalizedName } = require('./app.cjs');
assert.equal(normalizedName('  ALPHA  '), 'alpha');
assert.equal(normalizedName('ALPHA'), 'alpha');
assert.equal(normalizedName('   '), '');
assert.equal(normalizedName('ALPHA BETA'), 'alpha beta');
