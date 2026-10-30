---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with a clear aesthetic direction and high design quality. Routes layout, token systems, responsive behavior, motion, anti-pattern avoidance, and stack-specific implementation across a wide range of app surface types.
compatibility: opencode
---

# Frontend Design

Use this skill to design and implement frontend interfaces that are visually intentional, structurally coherent, and production-ready.

This skill is the entry point for frontend design execution, not a generic design manifesto. It should route to the minimum reference set required by the requested surface, stack, and design problem.

## When To Use

Use this skill when:

- building UI components, pages, or full interfaces
- improving or redesigning an existing frontend
- creating landing pages, dashboards, app shells, workspaces, or settings surfaces
- applying or correcting a design system
- making responsive layout decisions
- adding interaction polish or motion

Do not use this skill as the primary tool for:

- full user-flow mapping
- wireframing before the product surface is known
- PRD-to-page architecture planning

Those are adjacent planning tasks. This skill assumes the product surface is known enough to design.

## Reference Navigation

Start with the minimum reference set.

**Surface Types**
- `references/surface-types.md` - choose the right posture for landing pages, dashboards, workspaces, settings, consumer surfaces, admin interfaces, and hybrids

**Core Systems**
- `references/design-tokens.md` - colors, typography, spacing, radius, elevation, token discipline
- `references/layout-composition.md` - hierarchy, zoning, density, composition modes, rhythm
- `references/layout-patterns.md` - shell patterns, list-detail, split-pane, dashboard, settings, and dense-data layouts
- `references/component-patterns.md` - action bars, tables, filters, empty states, settings grouping, and navigation behavior
- `references/responsive-behavior.md` - mobile/tablet/desktop adaptation rules
- `references/responsive-surface-patterns.md` - surface-specific responsive collapse, reflow, overflow, and re-architecture rules

**Polish And Interaction**
- `references/motion-guidelines.md` - motion intensity, transition usage, restraint
- `references/frontend-anti-patterns.md` - generic AI aesthetics, weak hierarchy, clutter, system inconsistency
- `references/visual-directions.md` - aesthetic directions, best-fit surfaces, risks, and token/composition implications

**Implementation**
- `references/implementation-modes.md` - React, Next.js, Tailwind, and vanilla adaptation rules
- `references/component-architecture.md` - component structure, composition patterns, container/presentation separation
- `references/state-management.md` - choosing the right state model and avoiding prop-drilling misuse
- `references/production-ui-rules.md` - production-quality frontend engineering rules and anti-AI-aesthetic guidance
- `references/accessibility-checklist.md` - keyboard access, labels, focus, states, and verification
- `references/responsive-implementation.md` - mobile-first implementation rules, breakpoint checks, and responsive QA
- `references/loading-and-transitions.md` - skeletons, optimistic updates, and transition behavior

## Reference Selection Rules

Read only what the task needs.

- If the task is about picking the right interface type for a product surface, start with `references/surface-types.md`.
- If the task is about defining or correcting the visual system, start with `references/design-tokens.md`.
- If the task is about hierarchy, composition, structure, or density, start with `references/layout-composition.md`.
- If the task is about choosing a shell or page-level pattern, start with `references/layout-patterns.md`.
- If the task is about repeated interactive structures, start with `references/component-patterns.md`.
- If the task is about mobile and desktop behavior, start with `references/responsive-behavior.md`.
- If the task is about how a specific surface should collapse or expand across breakpoints, start with `references/responsive-surface-patterns.md`.
- If the task is about animation or interaction feel, start with `references/motion-guidelines.md`.
- If the task is about weak existing output or “why does this UI feel generic,” start with `references/frontend-anti-patterns.md`.
- If the task is about selecting a strong aesthetic direction, start with `references/visual-directions.md`.
- If a specific stack is provided, also read `references/implementation-modes.md`.
- If the task is about component structure or reusability, read `references/component-architecture.md`.
- If the task is about choosing where state should live, read `references/state-management.md`.
- If the task is about implementation quality and avoiding low-grade generated UI, read `references/production-ui-rules.md`.
- If the task is about accessibility requirements or verification, read `references/accessibility-checklist.md`.
- If the task is about responsive execution details, read `references/responsive-implementation.md`.
- If the task is about loading states, optimistic updates, or transition behavior, read `references/loading-and-transitions.md`.

## Combined Routing Rules

For overlapping work, use these pairings in order:

- landing page + visual polish -> `references/surface-types.md`, `references/visual-directions.md`, `references/layout-composition.md`, `references/motion-guidelines.md`
- dashboard + dense data -> `references/surface-types.md`, `references/layout-patterns.md`, `references/component-patterns.md`, `references/responsive-surface-patterns.md`
- workspace or app shell -> `references/surface-types.md`, `references/layout-patterns.md`, `references/layout-composition.md`, `references/design-tokens.md`
- settings or configuration UI -> `references/surface-types.md`, `references/layout-patterns.md`, `references/component-patterns.md`, `references/responsive-surface-patterns.md`
- redesign weak UI -> `references/frontend-anti-patterns.md`, `references/design-tokens.md`, `references/layout-composition.md`, `references/visual-directions.md`
- stack-specific implementation -> `references/implementation-modes.md`, `references/component-architecture.md`, and the most relevant surface and design references
- frontend implementation quality pass -> `references/production-ui-rules.md`, `references/accessibility-checklist.md`, `references/responsive-implementation.md`

## Common Workflows

### Design A New Interface

1. Identify the surface type in `references/surface-types.md`.
2. Read `references/visual-directions.md`.
3. Read `references/design-tokens.md`.
4. Read `references/layout-composition.md`.
5. Add `references/layout-patterns.md` and `references/responsive-behavior.md` when structure and breakpoints matter.
6. Produce:
   - aesthetic direction
   - token system
   - layout concept
   - implementation-ready UI code

### Redesign An Existing Interface

1. Read `references/frontend-anti-patterns.md`.
2. Read `references/design-tokens.md`.
3. Read `references/layout-composition.md`.
4. Read `references/visual-directions.md`.
5. If motion changes are requested, read `references/motion-guidelines.md`.
6. Produce:
   - diagnosed issues
   - replacement design direction
   - revised implementation

### Build A Dashboard Or App Workspace

1. Read `references/surface-types.md`.
2. Read `references/layout-patterns.md`.
3. Read `references/component-patterns.md`.
4. Read `references/responsive-surface-patterns.md`.
5. Read `references/design-tokens.md`.
6. Produce:
   - shell structure
   - hierarchy and zoning
   - density handling
   - reusable system rules

### Implement In A Specific Stack

1. Read `references/implementation-modes.md`.
2. Read `references/component-architecture.md`.
3. Read the most relevant surface and design references.
4. If accessibility or responsiveness is important, read `references/accessibility-checklist.md` and `references/responsive-implementation.md`.
5. Produce:
   - stack-aligned implementation
   - token usage strategy
   - readable component and styling structure

### Frontend Engineering Quality Pass

1. Read `references/production-ui-rules.md`.
2. Read `references/component-architecture.md`.
3. Read `references/state-management.md` if interactivity or shared state matters.
4. Read `references/accessibility-checklist.md`.
5. Read `references/responsive-implementation.md`.
6. Produce:
   - implementation quality corrections
   - accessibility and responsive fixes
   - component and state structure improvements

## Execution Pipeline

### 1. Context Intake

- identify purpose, audience, and use case
- identify surface type before selecting a direction
- detect platform and device expectations
- extract framework, accessibility, and performance constraints

### 2. Aesthetic Direction Selection

Choose one clear direction.

Define:
- visual style
- tone
- density
- motion philosophy

Do not blend conflicting styles without a strong reason.

### 3. Design System Definition

Define and use:
- color system
- typography hierarchy
- spacing scale
- radius and elevation rules
- CSS variables or equivalent tokens

### 4. Layout And Composition Planning

Before coding:
- define the structure
- establish hierarchy
- choose the composition mode
- decide how density should behave
- adapt composition to the actual surface type

### 5. Implementation

Generate:
- production-ready code
- modular structure
- reusable components
- responsive layout

Follow:
- separation of concerns
- accessibility standards
- clean structure

### 6. Refinement Pass

Improve:
- spacing consistency
- alignment precision
- visual rhythm
- interaction polish

Remove:
- unnecessary elements
- inconsistent styling
- decorative clutter without purpose

## Design Token Rules

All outputs must:

- use a consistent token system
- define typography hierarchy
- use a consistent spacing scale
- avoid repeated hardcoded values

## Anti-Generic Design Rules

Reject outputs that include:

- generic hero + cards defaults
- overused decorative gradients without structural purpose
- default/system font dependence without intent
- repetitive AI-like styling
- one-size-fits-all composition across different app types

Each design should include at least one meaningful differentiator:

- distinctive typography
- surface-specific composition
- unusual but usable spatial rhythm
- intentional motion behavior

## Code Quality Requirements

- modular, reusable components
- no excessive inline styles
- semantic HTML
- accessible structure
- responsive by default
- clear separation of structure and styling logic
- meaningful loading, error, and empty states

## Output Modes

- Full build mode
- Enhancement mode
- Design system mode
- Rapid prototype mode

Match the requested complexity. Do not overbuild.

## Surface Adaptation Rules

Match the design approach to the surface instead of forcing one frontend style everywhere.

- Landing page:
  prioritize narrative, conversion hierarchy, and pacing
- Dashboard:
  prioritize orientation, structure, and scanability
- Workspace / tool UI:
  prioritize shell clarity, panel relationships, and visible state
- Settings UI:
  prioritize categorization and low-friction editing
- Consumer app surface:
  prioritize approachability and strong primary actions
- Admin interface:
  prioritize control, auditability, and density management
- Marketing + app hybrid:
  keep expressive marketing surfaces distinct from disciplined product surfaces

## Component Behavior Rule

For surfaces with repeated interactions, define:

- where global actions live
- where local actions live
- whether filtering is instant or batch
- how empty states replace missing content
- how tables, cards, tabs, drawers, and settings sections behave

## Output Expectations

When using this skill:

- state a clear design intent
- choose a surface-appropriate composition model
- define tokens before styling heavily
- keep implementation aligned to the provided stack
- avoid loading unrelated references
- favor distinctive but usable output over novelty for its own sake
- meet production-quality frontend engineering expectations, not just visual ambition

## Final Rule

Every output should feel:

- intentional
- distinctive
- production-ready
- appropriate to the app type

No two outputs should feel identical just because they came from the same skill.
