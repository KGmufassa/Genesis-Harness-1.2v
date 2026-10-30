# Component Patterns

Use this file for repeated interaction structures and component-level decision rules.

## Global Vs Local Actions

- global actions belong in page or table toolbars
- local actions belong close to the object they affect
- destructive actions should not compete visually with primary actions

## Table Toolbar Pattern

Best for:
- data tables
- admin lists
- audit queues

Rules:
- reserve the toolbar for global actions such as settings, complex filters, export, or batch editing
- keep high-priority actions visible
- move overflow actions into menus after the visible set becomes too large

Source note:
- Carbon data table guidance reserves the toolbar for global actions and limits the visible action set before overflow.

## Filtering Pattern

### Instant Filtering

Use when:
- one selection is common
- results are expected immediately
- retrieval is fast enough to keep pace with interaction

### Batch Filtering

Use when:
- users make several choices across categories
- result retrieval is slower
- the user benefits from confirming changes together

Placement rules:
- multi-category filtering should live vertically on the left or horizontally above the dataset
- do not hide multi-category filtering inside a simple dropdown

Source note:
- Carbon filtering guidance distinguishes instant and batch filtering and recommends side/top placement for multi-category controls.

## Search Pattern

- collapsed search is appropriate when search is secondary to the page title or toolbar
- keep search discoverable when it is a frequent action

## Table Row Interaction Pattern

- row hover can help scanning even when rows are not clickable
- selection, expansion, and row-level actions must have distinct click targets
- pagination belongs below the table

## Empty State Pattern

Rules:
- empty states should replace the element that would otherwise show
- avoid leaving the old structure visible behind the empty message
- for repeated dashboard failures, prefer simpler text-based empty states over repeated illustrations
- include the next best action when the user can recover or populate the space

Source note:
- Carbon empty-state guidance recommends replacing the underlying element and simplifying repeated dashboard empty states.

## Settings Group Pattern

- group preferences by user meaning, not implementation detail
- frequent actions should remain contextual, not buried in settings
- use clear labels and safe defaults

## Output Expectation

When using component patterns, specify:
- component family
- global vs local action placement
- state variants
- default interaction behavior
- overflow behavior if needed
- accessibility-sensitive behavior
