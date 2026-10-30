---
template_id: marketing-website
template_name: Marketing Website
category: website
version: 1.0.0
status: stable
extends: base-ui-architecture
description: Content-first website architecture for promotion, conversion, education, and public discovery.
suitable_for:
  - public-websites
  - launch-sites
  - content-first-products
unsuitable_for:
  - dense-record-management
  - internal-admin-workflows
  - mobile-only-task-tools
---

# Marketing Website

Structural defaults:

- navigation: `top-navigation`
- common layouts: `single-column`, `responsive-grid`, `card-grid`
- density: low to balanced

Required page archetypes:

- `landing-page`
- `detail`
- `search-results` when content discovery exists

Conditional page archetypes:

- `pricing`
- `authentication`
- `onboarding`
- `settings`

Common component families:

- navigation
- actions
- data-display
- feedback

Avoid:

- persistent data tables as the primary public browsing model
- deeply nested sidebar navigation unless authenticated product surfaces are in scope

