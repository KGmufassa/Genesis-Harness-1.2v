---
template_id: portfolio-showcase
template_name: Portfolio Showcase
category: website
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Showcase architecture for creative work, case studies, projects, services, testimonials, and lightweight contact conversion.
suitable_for:
  - portfolios
  - agencies
  - creators
  - case-study-sites
unsuitable_for:
  - dense-documentation
  - record-management
  - multi-vendor-commerce
---

# Portfolio Showcase

Structural defaults:

- navigation: `top-navigation`
- common layouts: `single-column`, `responsive-grid`, `card-grid`
- density: low to readable

Required page archetypes:

- `landing-page`
- `collection`
- `detail`

Conditional page archetypes:

- `search-results`
- `authentication`

Common component families:

- navigation
- actions
- data-display
- feedback

Layout rules:

- use `card-grid` for project galleries and case-study indexes
- use `single-column` for project narratives, service details, and contact pages
- keep page inventory shallow unless content discovery is a core requirement

