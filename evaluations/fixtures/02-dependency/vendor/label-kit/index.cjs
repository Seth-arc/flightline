exports.formatLabel = value => value.trim().toLowerCase().replace(/_/g, ' ')
  .replace(/\b[a-z]/g, letter => letter.toUpperCase());
