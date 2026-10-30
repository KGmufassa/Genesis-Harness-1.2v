# UI Architecture Contradiction Rules

Fail or flag Stage 4 UI blueprint validation when:

- mobile-first product uses desktop-only navigation without a mobile transformation
- comparison-heavy page uses `card-grid` without an explicit rationale
- long workflow is placed inside a small modal
- required action is hidden only in an overflow menu
- table layout lacks mobile behavior
- bulk-action page lacks selection behavior
- page has multiple primary actions without hierarchy
- navigation item has no destination
- page has no entry point
- data-dense page lacks sorting, filtering, loading, empty, and error states
- permission-sensitive page lacks permission-denied behavior
- component family duplicates another component family responsibility without a reason

