---
pattern_id: offline
pattern_type: state
aliases: [network-offline, disconnected]
use_when: [network unavailable or degraded]
avoid_when: [server-side validation error]
requires: [available offline actions, retry behavior]
---

# State Pattern — offline

Define offline banner, disabled actions, retry behavior, queued changes, and recovery once connection returns.
