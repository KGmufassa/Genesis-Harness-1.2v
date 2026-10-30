---
pattern_id: collection-page
pattern_type: page
aliases: [inventory, records, catalog, list-page]
use_when: [browse records, manage inventory, compare items]
avoid_when: [single record detail, one-time task flow]
requires: [layout decision, search filtering sorting states]
---

# Page Pattern — collection-page

Use for browsing and managing multiple records or items.

Preferred layouts: `data-table`, `card-grid`, `content-list`, `master-detail`.

Selection depends on density, comparison needs, visual browsing needs, and bulk action needs.

Common components: search, filters, sort controls, pagination/loading, row/card actions, create action.
