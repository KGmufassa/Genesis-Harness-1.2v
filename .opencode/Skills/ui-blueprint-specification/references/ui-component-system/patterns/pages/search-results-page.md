---
pattern_id: search-results-page
pattern_type: page
aliases: [results, global-search]
use_when: [query-driven discovery, cross-entity search]
avoid_when: [known collection browsing only]
requires: [query state, result grouping, no-results state]
---

# Page Pattern — search-results-page

Use for global or scoped search.

Preferred layouts: `content-list`, `card-grid`, `data-table`.

Requires query state, empty query behavior, no-results behavior, result grouping, filters, and keyboard-accessible result opening.
