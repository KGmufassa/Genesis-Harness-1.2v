# UI Components Generation Workflow

`ui-blueprint-specification` should use this workflow:

1. Read `ROUTING-INDEX.md` to identify the minimum relevant reference set.
2. Read Stage 1 product, workflow, feature, boundary, and MVP inputs.
3. Read Stage 3 architecture, API, data, and permission constraints.
4. Read Stage 4 journeys, interactions, screen system, feature behaviors, states, accessibility, design system, and visual references.
5. Select or confirm the primary UI architecture template.
6. Select relevant extensions and check `extensions/EXTENSION-COMPATIBILITY.md`.
7. Apply precedence rules.
8. Remove irrelevant template defaults.
9. Define application shell and navigation architecture.
10. Generate page inventory.
11. Assign a page archetype to every launch-critical page.
12. Select a layout pattern for every launch-critical page, using `LAYOUT-DECISION-MATRIX.md` when placement is not obvious.
13. Select component families and shared components.
14. Define responsive transformations.
15. Define system states.
16. Define accessibility structure.
17. Record layout decisions, component-family decisions, overrides, deviations, and template gaps.
18. Generate Stage 4-native UI blueprints.
19. Optionally derive `Build-Plans/Stage-4/UI-COMPONENTS.md`.

Stage 4 outputs must preserve stable `UI-BLUEPRINT-`, `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` references.
