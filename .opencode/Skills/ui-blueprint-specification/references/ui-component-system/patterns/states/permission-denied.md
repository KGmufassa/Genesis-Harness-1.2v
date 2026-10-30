---
pattern_id: permission-denied
pattern_type: state
aliases: [forbidden, no-access]
use_when: [user lacks permission for page action or data]
avoid_when: [unauthenticated login requirement]
requires: [reason, allowed recovery or request-access path]
---

# State Pattern — permission-denied

Define restricted-state copy, available fallback actions, request-access path, and whether the user can see read-only context.
