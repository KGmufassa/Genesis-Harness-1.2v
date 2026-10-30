---
pattern_id: split-pane
pattern_type: layout
aliases: [split-view, resizable-pane]
use_when: [two persistent work areas, compare or compose while referencing]
avoid_when: [small mobile-first screens, simple forms]
requires: [pane priority, resize behavior, responsive collapse rule]
---

# Layout Pattern — split-pane

Use when:

- two related work surfaces must remain visible together
- users compare or transfer information between panes

Avoid when:

- content can be handled by simple master-detail
- mobile is primary and both panes cannot remain legible

Requires:

- pane priority
- resize/collapse behavior
- mobile transformation
- focus order between panes
