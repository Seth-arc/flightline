# Public list contract

Accepted: `listNames(people)` returns an array of strings. External consumers
use this interface and cannot all be updated in one release. Keep it working.
Add new interfaces for different response shapes. Revisit only when consumers
have migrated and a breaking release is explicitly authorized.
