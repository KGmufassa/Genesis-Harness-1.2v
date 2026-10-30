---
pattern_id: master-detail
pattern_type: layout
aliases: [split-detail, list-detail, inbox-detail]
use_when: [select from list then inspect detail, fast record switching]
avoid_when: [standalone detail pages, small single-purpose screens]
requires: [selection state, empty detail state, mobile drill-in behavior]
---

# Layout Pattern — master-detail

Use when:

- users browse a list while repeatedly inspecting or editing one selected item
- context switching between collection and detail would slow the workflow

Avoid when:

- detail views are complex enough to require full-page focus
- mobile is primary and split content would harm comprehension

Requires:

- selected item state
- empty selection state
- mobile transformation to stacked or routed views
- keyboard navigation between master list and detail panel
