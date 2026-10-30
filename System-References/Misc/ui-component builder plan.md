# UI-COMPONENT.md System Build Plan

## 1. System Goal

Build a reusable system that generates a project-specific `UI-COMPONENTS.md` file from a selected UI architecture template.

The system should help define:

* Application navigation
* Application shell
* Page hierarchy
* Page layouts
* Grid, table, list, and card usage
* Component families
* Interaction patterns
* Responsive behavior
* Loading, empty, error, and permission states
* Accessibility expectations

The system should work independently from visual design styles.

Example:

```yaml
ui_architecture_template: saas-dashboard
visual_design_template: neobrutalism
```

The UI architecture template determines structure and behavior.

The design template determines colors, typography, borders, shadows, and visual styling.

---

# 2. Final System Shape

The completed system should contain five major parts:

```text
UI-COMPONENT.md System
├── Template schema
├── UI architecture templates
├── Template selector
├── Project file generator
└── Validation system
```

Recommended directory structure:

```text
ui-component-system/
├── README.md
├── TEMPLATE-SCHEMA.md
├── TEMPLATE-SELECTOR.md
├── GENERATION-WORKFLOW.md
├── OUTPUT-SCHEMA.md
├── NORMALIZED-VALUES.md
│
├── templates/
│   ├── base/
│   │   └── base-ui-architecture.md
│   ├── websites/
│   ├── web-apps/
│   ├── commerce/
│   └── mobile/
│
├── patterns/
│   ├── navigation/
│   ├── layouts/
│   ├── pages/
│   ├── components/
│   ├── interactions/
│   └── states/
│
├── extensions/
│   ├── analytics.md
│   ├── collaboration.md
│   ├── role-based-access.md
│   └── onboarding.md
│
├── assets/
│   └── UI-COMPONENTS.template.md
│
├── validation/
│   ├── TEMPLATE-CHECKLIST.md
│   ├── OUTPUT-CHECKLIST.md
│   └── CONTRADICTION-RULES.md
│
└── tests/
    ├── test-projects/
    ├── expected-outputs/
    └── TEST-RESULTS.md
```

---

# Phase 1 — Define the System Boundaries

## Step 1. Define what `UI-COMPONENTS.md` controls

Create a document that explicitly defines the file’s responsibilities.

The file should control:

```yaml
ui_components_responsibilities:
  - information-architecture
  - application-navigation
  - application-shell
  - page-inventory
  - page-archetypes
  - page-layouts
  - component-selection
  - responsive-behavior
  - interaction-patterns
  - system-states
  - accessibility-structure
```

The file should not control:

```yaml
excluded_responsibilities:
  - final-color-palette
  - typography-branding
  - logo-treatment
  - illustration-style
  - backend-architecture
  - database-schema
  - API-design
  - feature-requirements
```

## Step 2. Define the relationship with other project files

Create a clear document ownership map.

```yaml
project_files:
  PRD.md:
    defines: product-requirements

  USER-FLOWS.md:
    defines: user-task-sequences

  UI-COMPONENTS.md:
    defines: interface-structure-and-behavior

  DESIGN.md:
    defines: visual-design-language

  TECH-STACK.md:
    defines: implementation-technology
```

## Step 3. Define the system terminology

Standardize terms early.

Use:

```yaml
terminology:
  ui_template: A reusable structural architecture
  page_archetype: A reusable page type
  layout_pattern: A method of arranging page content
  component_family: A group of related reusable components
  extension: An optional capability added to a base template
  project_output: The generated UI-COMPONENTS.md file
  override: A project-specific replacement for a template default
```

## Phase 1 deliverables

```text
README.md
DOCUMENT-BOUNDARIES.md
TERMINOLOGY.md
```

---

# Phase 2 — Build the Universal Template Schema

## Step 4. Create `TEMPLATE-SCHEMA.md`

Every UI architecture template must use the same structure.

Required template sections:

```text
1. Template identity
2. Product characteristics
3. Structural defaults
4. Information architecture
5. Navigation architecture
6. Application shell
7. Page archetypes
8. Page composition patterns
9. Layout rules
10. Component families
11. Interaction patterns
12. Responsive strategy
13. System states
14. Accessibility requirements
15. Adaptation rules
16. Output instructions
```

## Step 5. Define template metadata

Use a standard frontmatter block.

```yaml
---
template_id: saas-dashboard
template_name: SaaS Dashboard
category: web-app
version: 1.0.0
status: stable
extends: base-ui-architecture
description: >
  Workspace-oriented interface architecture for recurring business
  workflows, data management, monitoring, and account administration.
suitable_for:
  - business-saas
  - customer-portals
  - subscription-platforms
unsuitable_for:
  - editorial-websites
  - simple-landing-pages
  - single-screen-mobile-tools
---
```

## Step 6. Define rule priority levels

Each recommendation should be labeled as one of the following:

```yaml
rule_levels:
  required:
    meaning: Normally necessary for this archetype

  recommended:
    meaning: Default unless the project provides a reason to change it

  conditional:
    meaning: Only apply when a specific product condition exists

  prohibited:
    meaning: Normally incompatible with the archetype
```

## Step 7. Define normalized values

Create `NORMALIZED-VALUES.md`.

This prevents templates from using different names for the same pattern.

### Navigation values

```yaml
navigation_patterns:
  - top-navigation
  - sidebar-navigation
  - bottom-navigation
  - navigation-drawer
  - split-navigation
  - contextual-navigation
  - tab-navigation
```

### Layout values

```yaml
layout_patterns:
  - single-column
  - two-column
  - responsive-grid
  - dashboard-grid
  - card-grid
  - data-table
  - content-list
  - master-detail
  - split-pane
  - form-layout
  - settings-layout
```

### Page archetypes

```yaml
page_archetypes:
  - dashboard
  - collection
  - detail
  - create-edit
  - settings
  - search-results
  - authentication
  - onboarding
  - profile
  - checkout
  - messaging
  - analytics
```

## Phase 2 deliverables

```text
TEMPLATE-SCHEMA.md
NORMALIZED-VALUES.md
templates/base/base-ui-architecture.md
```

---

# Phase 3 — Build the Base UI Architecture Template

## Step 8. Create the universal base template

The base template should contain rules shared by all interface types.

It should define:

* Every page must have a purpose.
* Every page must have a primary user goal.
* Every page must declare a page archetype.
* Every data region must define system states.
* Every page must define responsive behavior.
* Every navigation destination must map to a real page.
* Every major component must have a clear responsibility.
* Every primary action must be identifiable.
* Every interactive component must define keyboard and touch behavior.

## Step 9. Create the base page specification

Use a common page schema.

```yaml
page:
  id:
  name:
  route:
  archetype:
  purpose:
  primary_user:
  primary_goal:
  entry_points: []
  exit_points: []

navigation:
  parent:
  primary_location:
  breadcrumbs: []
  tabs: []

header:
  title:
  description:
  primary_action:
  secondary_actions: []

layout:
  pattern:
  content_width:
  columns:
  regions: []

components: []

states:
  loading:
  empty:
  error:
  populated:
  permission_denied:

responsive:
  desktop:
  tablet:
  mobile:

accessibility:
  landmarks:
  heading_order:
  keyboard_flow:
  focus_behavior:
```

## Step 10. Create the base component specification

```yaml
component:
  id:
  name:
  category:
  purpose:
  reuse_level:
  used_on: []

anatomy: []

variants: []

states:
  - default
  - hover
  - focus
  - active
  - disabled
  - loading
  - error

behavior:
  click:
  keyboard:
  touch:
  responsive:

accessibility:
  semantic_role:
  keyboard_support:
  screen_reader_label:
  focus_management:
```

## Phase 3 deliverables

```text
templates/base/base-ui-architecture.md
assets/UI-COMPONENTS.template.md
```

---

# Phase 4 — Build the First Template Set

Start with four templates that are structurally different.

## Step 11. Build `marketing-website.md`

Primary focus:

* Top navigation
* Hero section
* Conversion paths
* Feature sections
* Social proof
* Pricing
* FAQ
* Footer
* Responsive content sections

Required page archetypes:

```yaml
required:
  - landing-page
  - product-or-service-page
  - contact-or-conversion-page

conditional:
  - pricing
  - case-studies
  - blog
  - documentation
```

## Step 12. Build `saas-dashboard.md`

Primary focus:

* Persistent sidebar
* Utility top bar
* Dashboard
* Record collections
* Detail pages
* Forms
* Settings
* Search and filtering
* Tables and operational data

Required page archetypes:

```yaml
required:
  - dashboard
  - collection
  - detail
  - create-edit
  - settings

conditional:
  - analytics
  - billing
  - team-management
  - integrations
```

## Step 13. Build `ecommerce-storefront.md`

Primary focus:

* Product discovery
* Category navigation
* Product grids
* Product detail
* Search
* Cart
* Checkout
* Account
* Order history

Required page archetypes:

```yaml
required:
  - storefront-home
  - category-listing
  - search-results
  - product-detail
  - cart
  - checkout
  - order-confirmation
```

## Step 14. Build `mobile-utility.md`

Primary focus:

* Short repeated workflows
* Bottom navigation
* One-handed interaction
* Bottom sheets
* Device permissions
* Offline handling
* Interrupted-session recovery
* Large touch targets

Required page archetypes:

```yaml
required:
  - mobile-home
  - primary-task
  - history-or-saved-items
  - settings

conditional:
  - onboarding
  - permissions
  - account
```

## Phase 4 deliverables

```text
templates/websites/marketing-website.md
templates/web-apps/saas-dashboard.md
templates/commerce/ecommerce-storefront.md
templates/mobile/mobile-utility.md
```

---

# Phase 5 — Build the Pattern Library

Templates should reference shared patterns instead of repeating large blocks.

## Step 15. Create navigation patterns

```text
patterns/navigation/
├── top-navigation.md
├── sidebar-navigation.md
├── bottom-navigation.md
├── navigation-drawer.md
├── tabs.md
└── breadcrumbs.md
```

Each navigation pattern should define:

```yaml
pattern:
  purpose:
  use_when: []
  avoid_when: []
  anatomy: []
  desktop_behavior:
  tablet_behavior:
  mobile_behavior:
  accessibility:
```

## Step 16. Create layout patterns

```text
patterns/layouts/
├── dashboard-grid.md
├── card-grid.md
├── data-table.md
├── content-list.md
├── master-detail.md
├── split-pane.md
├── form-layout.md
└── settings-layout.md
```

## Step 17. Create page patterns

```text
patterns/pages/
├── dashboard-page.md
├── collection-page.md
├── detail-page.md
├── form-page.md
├── settings-page.md
├── search-results-page.md
├── authentication-page.md
└── onboarding-page.md
```

## Step 18. Create interaction patterns

```text
patterns/interactions/
├── search.md
├── filtering.md
├── sorting.md
├── bulk-actions.md
├── creation.md
├── editing.md
├── deletion.md
├── notifications.md
└── permissions.md
```

## Step 19. Create state patterns

```text
patterns/states/
├── loading.md
├── empty.md
├── error.md
├── success.md
├── offline.md
└── permission-denied.md
```

## Phase 5 deliverables

A complete reusable pattern library referenced by all templates.

---

# Phase 6 — Build the Template Selector

## Step 20. Create the selector inputs

The selector should evaluate:

```yaml
selection_inputs:
  product_category:
  primary_platform:
  primary_user_behavior:
  dominant_workflow:
  content_type:
  information_density:
  comparison_needs:
  collaboration_level:
  transaction_model:
  session_frequency:
```

## Step 21. Create the selection questions

Use a short structured questionnaire.

```text
1. What is the product’s primary purpose?
2. What action do users perform most often?
3. What type of content or records do users manage?
4. Do users compare many items or values?
5. Is the experience task-first or content-first?
6. Is collaboration central to the product?
7. Is the primary experience desktop or mobile?
8. Does the system include purchasing or transactions?
```

## Step 22. Build the selection matrix

```yaml
selection_rules:
  - condition:
      purpose: promotion
      experience: content-first
    template: marketing-website

  - condition:
      purpose: recurring-business-workflows
      platform: desktop-web
    template: saas-dashboard

  - condition:
      purpose: direct-product-purchasing
      transaction_model: seller-to-customer
    template: ecommerce-storefront

  - condition:
      purpose: focused-repeated-task
      platform: mobile
    template: mobile-utility
```

## Step 23. Define the selector output

```yaml
template_selection:
  primary_template: saas-dashboard
  confidence: high

  alternative_templates:
    - internal-admin-tool

  recommended_extensions:
    - analytics
    - role-based-access

  reasons:
    - recurring-workflows
    - desktop-first
    - structured-record-management

  unresolved_questions: []
```

## Phase 6 deliverables

```text
TEMPLATE-SELECTOR.md
SELECTION-MATRIX.md
SELECTION-QUESTIONS.md
```

---

# Phase 7 — Build Template Extensions

Extensions add capabilities without creating a completely new template.

## Step 24. Define the extension schema

```yaml
extension:
  id:
  name:
  version:
  compatible_with: []
  description:

adds:
  pages: []
  components: []
  interactions: []
  states: []

modifies:
  navigation: []
  layouts: []
  responsive_behavior: []

requires:
  product_conditions: []
```

## Step 25. Build initial extensions

Start with:

```text
extensions/
├── analytics.md
├── collaboration.md
├── role-based-access.md
├── onboarding.md
├── billing.md
├── messaging.md
└── file-management.md
```

## Step 26. Define composition rules

Example:

```yaml
ui_architecture:
  primary_template: saas-dashboard

  extensions:
    - analytics
    - role-based-access
    - collaboration
```

## Step 27. Define override precedence

```yaml
precedence:
  1: project-specific-requirements
  2: explicit-project-overrides
  3: selected-extensions
  4: primary-template
  5: base-template
```

## Phase 7 deliverables

```text
EXTENSION-SCHEMA.md
TEMPLATE-COMPOSITION.md
PRECEDENCE-RULES.md
extensions/*.md
```

---

# Phase 8 — Build the Project Generator

## Step 28. Define generator inputs

```yaml
generator_inputs:
  required:
    - product-description-or-PRD
    - selected-template

  recommended:
    - user-roles
    - feature-list
    - user-flows
    - platform-targets

  optional:
    - selected-extensions
    - design-template
    - technical-constraints
    - existing-components
```

## Step 29. Build the generation workflow

The generator should follow this sequence:

```text
1. Read the available product documentation.
2. Extract the product purpose.
3. Identify user roles.
4. Identify primary workflows.
5. Identify major product objects.
6. Identify comparison-heavy tasks.
7. Identify content-heavy tasks.
8. Select or confirm the primary template.
9. Select relevant extensions.
10. Remove irrelevant template defaults.
11. Define the application shell.
12. Define the navigation architecture.
13. Generate the page inventory.
14. Assign a page archetype to every page.
15. Select a layout pattern for every page.
16. Select required component families.
17. Define responsive transformations.
18. Define system states.
19. Define accessibility requirements.
20. Record overrides and deviations.
21. Generate `UI-COMPONENTS.md`.
```

## Step 30. Define the generated file structure

```text
UI-COMPONENTS.md
├── Template metadata
├── Product interface summary
├── User roles
├── Primary workflows
├── Information architecture
├── Navigation architecture
├── Application shell
├── Page inventory
├── Page specifications
├── Layout decisions
├── Component inventory
├── Interaction rules
├── Responsive strategy
├── System states
├── Accessibility requirements
└── Template deviations
```

## Step 31. Add decision traceability

Each important decision should include its reason.

```yaml
layout_decision:
  page: products
  selected_pattern: data-table

  reasons:
    - users-compare-prices
    - rows-share-consistent-fields
    - bulk-actions-are-required

  source:
    - PRD.product-management
    - template.saas-dashboard.collection-page
```

## Step 32. Define deviation tracking

```yaml
template_deviations:
  - subject: primary-navigation
    template_default: sidebar
    project_choice: top-navigation
    reason: application-has-only-three-primary-sections
```

## Phase 8 deliverables

```text
GENERATION-WORKFLOW.md
INPUT-SCHEMA.md
OUTPUT-SCHEMA.md
TRACEABILITY-RULES.md
assets/UI-COMPONENTS.template.md
```

---

# Phase 9 — Build the Validation System

## Step 33. Validate template files

Every template must contain:

```yaml
template_checks:
  - valid-template-id
  - version-defined
  - category-defined
  - suitable-for-defined
  - unsuitable-for-defined
  - structural-defaults-defined
  - navigation-defined
  - page-archetypes-defined
  - layout-rules-defined
  - responsive-strategy-defined
  - states-defined
  - accessibility-defined
```

## Step 34. Validate generated project files

```yaml
output_checks:
  - every-page-has-purpose
  - every-page-has-primary-goal
  - every-page-has-archetype
  - every-page-has-layout
  - every-page-has-responsive-rules
  - every-data-page-has-system-states
  - every-navigation-item-maps-to-page
  - primary-actions-are-defined
  - no-orphan-pages
  - no-duplicate-component-responsibilities
```

## Step 35. Add contradiction rules

Detect issues such as:

```yaml
contradictions:
  - mobile-first-product-using-desktop-only-navigation
  - comparison-heavy-page-using-non-comparable-card-layout
  - long-workflow-placed-inside-small-modal
  - required-action-hidden-in-overflow-menu
  - table-without-mobile-behavior
  - multiple-primary-actions-on-one-page
  - navigation-item-without-destination
  - page-without-entry-point
```

## Step 36. Add completion scoring

```yaml
completion_score:
  product-context:
  navigation:
  page-inventory:
  page-layouts:
  components:
  interactions:
  responsive:
  states:
  accessibility:
  overall:
```

Example:

```yaml
completion_score:
  product-context: 100
  navigation: 100
  page-inventory: 95
  page-layouts: 90
  components: 85
  interactions: 90
  responsive: 100
  states: 75
  accessibility: 80
  overall: 89
```

## Phase 9 deliverables

```text
validation/TEMPLATE-CHECKLIST.md
validation/OUTPUT-CHECKLIST.md
validation/CONTRADICTION-RULES.md
validation/COMPLETION-SCORING.md
```

---

# Phase 10 — Test the System

## Step 37. Create test product briefs

Use products with different structural needs.

```text
tests/test-projects/
├── marketing-product.md
├── saas-record-manager.md
├── ecommerce-store.md
├── mobile-task-app.md
└── hybrid-marketplace.md
```

## Step 38. Test template selection

For each test project, record:

```yaml
selection_test:
  expected_template:
  selected_template:
  expected_extensions: []
  selected_extensions: []
  confidence:
  result:
```

## Step 39. Test generated outputs

Verify that each output is structurally different.

Expected distinctions:

```text
Marketing website
→ top navigation, content sections, conversion paths

SaaS dashboard
→ sidebar, tables, dashboards, record management

Ecommerce storefront
→ product grids, filters, cart, checkout

Mobile utility
→ bottom navigation, short flows, bottom sheets
```

## Step 40. Record template gaps

```yaml
template_gap:
  test_project:
  template:
  missing_pattern:
  repeated_across_projects:
  recommended_resolution:
```

Only add new templates or extensions when a gap appears repeatedly.

## Phase 10 deliverables

```text
tests/TEST-CASES.md
tests/SELECTION-RESULTS.md
tests/OUTPUT-REVIEWS.md
tests/TEMPLATE-GAPS.md
```

---

# Phase 11 — Package the System as an Agent Skill

## Step 41. Create the skill folder

```text
generating-ui-component-architecture/
├── SKILL.md
├── references/
│   ├── TEMPLATE-SCHEMA.md
│   ├── TEMPLATE-SELECTOR.md
│   ├── NORMALIZED-VALUES.md
│   ├── GENERATION-WORKFLOW.md
│   ├── templates/
│   ├── patterns/
│   └── extensions/
├── assets/
│   └── UI-COMPONENTS.template.md
└── scripts/
    ├── validate_template.py
    └── validate_output.py
```

## Step 42. Define the skill metadata

```yaml
---
name: generating-ui-component-architecture
description: >
  Selects and adapts structural UI architecture templates for websites,
  web applications, commerce systems, and mobile applications. Generates
  a project-specific UI-COMPONENTS.md defining navigation, application
  shells, page layouts, component families, responsive behavior, states,
  and accessibility requirements.
---
```

## Step 43. Define the skill instructions

```text
1. Inspect product documentation.
2. Extract product type and workflows.
3. Select the closest UI architecture template.
4. Load only the relevant template and pattern references.
5. Select necessary extensions.
6. Adapt the template to the project.
7. Generate UI-COMPONENTS.md.
8. Validate the output.
9. Report unresolved decisions and template deviations.
```

## Step 44. Add optional commands later

```text
/ui-template-select
/ui-components-generate
/ui-components-validate
/ui-template-compare
/ui-template-create
```

The first version only needs:

```text
/ui-template-select
/ui-components-generate
```

---

# Phase 12 — Version and Maintain the System

## Step 45. Create a template registry

```yaml
templates:
  - id: marketing-website
    category: website
    version: 1.0.0
    status: stable

  - id: saas-dashboard
    category: web-app
    version: 1.0.0
    status: stable

  - id: ecommerce-storefront
    category: commerce
    version: 1.0.0
    status: stable

  - id: mobile-utility
    category: mobile
    version: 1.0.0
    status: stable
```

## Step 46. Define version rules

```yaml
versioning:
  major: Breaking schema or architectural changes
  minor: New patterns, pages, or capabilities
  patch: Corrections and clarification
```

## Step 47. Add change tracking

Create:

```text
TEMPLATE-REGISTRY.md
CHANGELOG.md
```

## Step 48. Establish update rules

Update a template when:

* The same missing pattern appears in several projects.
* A recommendation repeatedly produces poor results.
* Two or more templates duplicate the same guidance.
* A new platform convention becomes common.
* A responsive rule repeatedly fails.
* A recurring contradiction is discovered.

---

# Recommended Implementation Order

## Milestone 1 — Core schema

Build:

```text
README.md
TEMPLATE-SCHEMA.md
NORMALIZED-VALUES.md
base-ui-architecture.md
UI-COMPONENTS.template.md
```

Success condition:

All future templates can use the same structure.

## Milestone 2 — Four starter templates

Build:

```text
marketing-website.md
saas-dashboard.md
ecommerce-storefront.md
mobile-utility.md
```

Success condition:

Each template produces a clearly different interface architecture.

## Milestone 3 — Selector

Build:

```text
TEMPLATE-SELECTOR.md
SELECTION-QUESTIONS.md
SELECTION-MATRIX.md
```

Success condition:

A product brief can be mapped to the correct template with reasons.

## Milestone 4 — Generator

Build:

```text
GENERATION-WORKFLOW.md
INPUT-SCHEMA.md
OUTPUT-SCHEMA.md
TRACEABILITY-RULES.md
```

Success condition:

A product brief and selected template produce a complete `UI-COMPONENTS.md`.

## Milestone 5 — Pattern library

Build the most reused patterns:

```text
sidebar-navigation.md
top-navigation.md
bottom-navigation.md
dashboard-grid.md
data-table.md
card-grid.md
collection-page.md
detail-page.md
form-page.md
loading.md
empty.md
error.md
```

Success condition:

Templates reference shared patterns instead of duplicating instructions.

## Milestone 6 — Validation

Build:

```text
TEMPLATE-CHECKLIST.md
OUTPUT-CHECKLIST.md
CONTRADICTION-RULES.md
COMPLETION-SCORING.md
```

Success condition:

The system identifies missing and contradictory UI architecture decisions.

## Milestone 7 — Extensions

Build:

```text
analytics.md
collaboration.md
role-based-access.md
onboarding.md
billing.md
```

Success condition:

Hybrid products can be modeled without creating excessive templates.

## Milestone 8 — Agent skill

Package the complete system into the reusable skill structure.

---

# Minimum Viable System

The first useful version should contain:

```text
ui-component-system/
├── README.md
├── TEMPLATE-SCHEMA.md
├── TEMPLATE-SELECTOR.md
├── GENERATION-WORKFLOW.md
├── NORMALIZED-VALUES.md
│
├── templates/
│   ├── base/
│   │   └── base-ui-architecture.md
│   ├── websites/
│   │   └── marketing-website.md
│   ├── web-apps/
│   │   └── saas-dashboard.md
│   ├── commerce/
│   │   └── ecommerce-storefront.md
│   └── mobile/
│       └── mobile-utility.md
│
├── assets/
│   └── UI-COMPONENTS.template.md
│
└── validation/
    └── OUTPUT-CHECKLIST.md
```

The MVP must be able to:

```text
1. Read a product brief or PRD.
2. Select one of four templates.
3. Explain the selection.
4. Generate the page inventory.
5. Choose the navigation architecture.
6. Assign layouts to each page.
7. Select component families.
8. Define responsive rules.
9. Define system states.
10. Produce UI-COMPONENTS.md.
```

The MVP should not include:

* Dozens of specialized templates
* React or framework-specific components
* Visual design generation
* Automatic frontend code generation
* A graphical template browser
* A template marketplace
* Complex scoring algorithms
* Product-specific templates

Build the structural decision system first. Expand templates and extensions only after testing reveals repeated architectural needs.
