---
pattern_id: content-list
pattern_type: layout
aliases: [list, feed, activity-list]
use_when: [chronological content, lightweight comparison, mobile-friendly scanning]
avoid_when: [many sortable columns, image-first browsing]
requires: [item anatomy, pagination or infinite loading, empty and loading states]
---

# Layout Pattern — content-list

Use when:

- users scan chronological, feed-like, activity, message, or simple record content
- each item has a compact repeated structure

Avoid when:

- dense cross-field comparison is required
- visual browsing is primary

Requires:

- item anatomy
- pagination or loading behavior
- no-results and empty states
- item action behavior
