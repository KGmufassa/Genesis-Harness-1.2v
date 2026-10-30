---
pattern_id: data-table
pattern_type: layout
aliases: [table, record-table, inventory-table, admin-table]
use_when: [many comparable records, sorting and filtering, bulk actions]
avoid_when: [image-first browsing, narrative content, simple mobile-only tasks]
requires: [mobile transformation, column priority, loading empty no-results and error states]
---

# Layout Pattern — data-table

Use when:

- users compare many records with consistent fields
- sorting, filtering, pagination, and bulk actions matter
- precision and density matter more than visual browsing

Avoid when:

- items are primarily visual or media-rich
- each item has highly variable structure
- mobile is the only primary surface and comparison is light

Requires:

- mobile transformation
- column priority rules
- loading, empty, no-results, error, and permission-denied states where applicable
- row action behavior
- bulk selection behavior when bulk actions exist
