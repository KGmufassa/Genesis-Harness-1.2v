---
pattern_id: dashboard-grid
pattern_type: layout
aliases: [dashboard, metrics-grid, kpi-grid]
use_when: [summary metrics, multiple widgets, operational overview]
avoid_when: [single task completion, deep record editing]
requires: [widget hierarchy, responsive stacking, loading and error states]
---

# Layout Pattern — dashboard-grid

Use when:

- the page summarizes multiple metrics, panels, charts, or operational regions
- users need a quick status overview before choosing a next action

Avoid when:

- one task or one record collection dominates the page
- the page is primarily form entry

Requires:

- region priorities
- responsive stacking rules
- stale/partial data behavior
- empty, error, and loading behavior per panel
