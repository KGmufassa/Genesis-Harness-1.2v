---
pattern_id: bulk-actions
pattern_type: interaction
aliases: [multi-select, batch-actions]
use_when: [multiple records can share an action]
avoid_when: [destructive action without confirmation, single-record workflows]
requires: [selection state, disabled state, confirmation rules]
---

# Interaction Pattern — bulk-actions

Define selection controls, select-all scope, eligibility rules, confirmation behavior, progress state, partial failure behavior, and undo/recovery.
