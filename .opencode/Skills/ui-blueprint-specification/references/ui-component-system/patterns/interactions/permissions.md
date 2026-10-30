---
pattern_id: permissions
pattern_type: interaction
aliases: [access-control, role-gates]
use_when: [role-based actions, restricted pages]
avoid_when: [public unrestricted flows]
requires: [permission_denied state, disabled or hidden action policy]
---

# Interaction Pattern — permissions

Define visible affordances, disabled/hidden behavior, permission-denied state, request-access behavior, and role-specific navigation.
