const { listNames } = require('./app.cjs');
exports.heading = people => listNames(people).join(', ');
