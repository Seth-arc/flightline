# DEC-001: Immediate revocation

Status: accepted.
After `revoke(id)` returns, the next `canAccess(id)` must return false.
Reason: removal of access must take effect before the next operation.
Assumption: every grant change passes through this instance's grant/revoke methods.
Revisit when grant state can change outside this instance. Performance work does
not authorize delayed revocation or removal of this requirement.
