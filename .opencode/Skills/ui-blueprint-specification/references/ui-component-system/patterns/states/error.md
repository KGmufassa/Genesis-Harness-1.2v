---
pattern_id: error
pattern_type: state
aliases: [failure, problem-state]
use_when: [request failure, validation failure, system failure]
avoid_when: [permission denial, planned empty content]
requires: [message, recovery action, support or retry path]
---

# State Pattern — error

Define user message, recovery action, retry behavior, field or page scope, and whether technical details are shown.
