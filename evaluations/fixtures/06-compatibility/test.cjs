const assert = require('node:assert/strict');
const { listNames } = require('./app.cjs');
const { heading } = require('./consumer.cjs');
const people = [{ id: 1, name: 'Ada' }, { id: 2, name: 'Grace' }];
assert.deepEqual(listNames(people), ['Ada', 'Grace']);
assert.equal(heading(people), 'Ada, Grace');
assert.deepEqual(listNames([]), []);
