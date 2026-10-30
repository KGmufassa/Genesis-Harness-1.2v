# Stage 4 UI Component System

This reference library helps `ui-blueprint-specification` select structural UI architecture before page blueprints are finalized.

It controls:

- information architecture
- application navigation
- application shell
- page inventory
- page archetypes
- page layout patterns
- component families
- interaction patterns
- responsive behavior
- loading, empty, error, success, offline, and permission-denied states
- accessibility structure

It does not control:

- product scope
- backend architecture
- database schema
- API design
- final colors, typography, logo treatment, or illustration style
- frontend code generation
- implementation tickets

Normal Stage 4 runs must treat this library as read-only. If a run discovers a missing pattern or poor recommendation, record a template gap or deviation in Stage 4 outputs; update this library only through explicit maintenance work.

Canonical Stage 4 outputs remain `07-ui-blueprint-specification.json`, `08-design-system-foundation.json`, and `09-complete-app-blueprint.md`.

# Efficient Use

For normal Stage 4 runs, read the smallest reference set that can justify the decision:

1. `ROUTING-INDEX.md`
2. `TEMPLATE-SELECTOR.md`
3. `NORMALIZED-VALUES.md`
4. the selected primary template
5. selected extensions only
6. directly relevant navigation, layout, page, interaction, and state patterns
7. `OUTPUT-CHECKLIST.md`
8. `CONTRADICTION-RULES.md`

Do not load every pattern file by default. Use `LAYOUT-DECISION-MATRIX.md` when the page’s placement model is unclear, such as choosing between `data-table`, `card-grid`, `content-list`, or `master-detail`.
