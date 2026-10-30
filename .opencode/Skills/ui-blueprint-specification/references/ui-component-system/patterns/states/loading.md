---
pattern_id: loading
pattern_type: state
aliases: [pending, skeleton, spinner]
use_when: [async data or action in progress]
avoid_when: [instant local state changes]
requires: [scope, duration expectation, accessibility announcement]
---

# State Pattern — loading

Define skeleton/spinner/progress behavior, cancellability where applicable, and which controls remain available.
