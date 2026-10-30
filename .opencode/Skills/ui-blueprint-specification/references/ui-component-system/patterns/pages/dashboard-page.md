---
pattern_id: dashboard-page
pattern_type: page
aliases: [overview, home-dashboard, metrics-page]
use_when: [operational summary, KPI monitoring, next actions]
avoid_when: [record-heavy management, data entry]
requires: [dashboard-grid or summary layout, widget states]
---

# Page Pattern — dashboard-page

Use for cross-surface summaries, operational status, and next-best-action entry.

Preferred layouts: `dashboard-grid`, `responsive-grid`.

Common components: metric cards, chart panels, activity lists, alert banners, quick actions.

Required states: loading, partial-data, empty, error, permission-denied when data is role-gated.
