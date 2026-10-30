---
pattern_id: deletion
pattern_type: interaction
aliases: [delete, remove, archive]
use_when: [entity removal or archival]
avoid_when: [irreversible action without explicit confirmation]
requires: [confirmation, permission check, recovery or undo rule]
---

# Interaction Pattern — deletion

Define confirmation copy, consequence, permission, audit/recovery expectations, loading state, success destination, failure recovery, and undo availability.
