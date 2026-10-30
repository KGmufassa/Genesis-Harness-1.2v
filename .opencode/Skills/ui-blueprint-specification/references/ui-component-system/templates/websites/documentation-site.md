---
template_id: documentation-site
template_name: Documentation Site
category: website
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Structured documentation architecture for docs navigation, versioned content, search, guides, references, and changelog-style discovery.
suitable_for:
  - product-documentation
  - developer-docs
  - knowledge-bases
  - help-centers
unsuitable_for:
  - promotional-only-sites
  - transactional-commerce
  - social-community-products
---

# Documentation Site

Structural defaults:

- navigation: `sidebar-navigation` or `top-navigation` with docs sidebar
- secondary navigation: `breadcrumbs`, section tabs, table-of-contents
- common layouts: `single-column`, `two-column`, `content-list`
- density: readable with high information clarity

Required page archetypes:

- `landing-page`
- `collection`
- `detail`
- `search-results`

Conditional page archetypes:

- `onboarding`
- `profile`
- `settings`

Common component families:

- navigation
- actions
- data-display
- search-and-filtering
- feedback

Layout rules:

- use `two-column` for docs pages with local table-of-contents
- use `content-list` for guide lists, reference indexes, and changelogs
- use `search-results` for docs search and filtered help discovery
- avoid commerce, account administration, and dashboard widgets unless a product console is also in scope

