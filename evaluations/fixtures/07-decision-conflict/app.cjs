exports.createAccess = () => {
  const grants = new Set();
  return {
    grant: id => grants.add(id),
    revoke: id => grants.delete(id),
    canAccess: id => grants.has(id),
  };
};
