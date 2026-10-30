---
template_id: editorial-content-site
template_name: Editorial Content Site
category: website
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Content publishing architecture for articles, categories, authors, archives, search, and recurring editorial discovery.
suitable_for:
  - publications
  - blogs
  - magazines
  - knowledge-content-sites
unsuitable_for:
  - dense-record-management
  - transactional-commerce
  - authenticated-workspace-products
---

# Editorial Content Site

Structural defaults:

- navigation: `top-navigation`
- secondary navigation: `breadcrumbs` and category navigation
- common layouts: `single-column`, `responsive-grid`, `card-grid`, `content-list`
- density: readable to balanced

Required page archetypes:

- `landing-page`
- `collection`
- `detail`
- `search-results`

Conditional page archetypes:

- `profile`
- `authentication`
- `settings`

Common component families:

- navigation
- actions
- data-display
- search-and-filtering
- feedback

Layout rules:

- use `content-list` for chronological article feeds, archives, and category pages
- use `single-column` for article/detail reading
- use `card-grid` for featured stories, topic collections, and visual editorial browsing
- use `search-results` when full-site content search exists

