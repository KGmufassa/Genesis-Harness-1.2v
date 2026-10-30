---
template_id: b2b-commerce-portal
template_name: B2B Commerce Portal
category: commerce
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Account-based commerce architecture for negotiated pricing, quotes, approvals, bulk ordering, procurement, invoices, and reorder workflows.
suitable_for:
  - b2b-commerce
  - wholesale-portals
  - procurement-products
  - account-based-ordering
unsuitable_for:
  - consumer-only-storefronts
  - pure-marketplaces
  - content-only-sites
---

# B2B Commerce Portal

Structural defaults:

- navigation: `sidebar-navigation` or authenticated `top-navigation`
- common layouts: `data-table`, `card-grid`, `form-layout`, `settings-layout`, `dashboard-grid`
- density: balanced to data-dense

Required page archetypes:

- `dashboard`
- `collection`
- `detail`
- `checkout`
- `settings`

Conditional page archetypes:

- `analytics`
- `search-results`
- `profile`

Common component families:

- navigation
- commerce
- actions
- forms
- data-display
- search-and-filtering
- feedback

Layout rules:

- use `data-table` for bulk ordering, reorder lists, invoices, quotes, and account product catalogs
- use `form-layout` for quote requests, approvals, billing, and procurement setup
- use `settings-layout` for account users, roles, payment terms, and delivery preferences
- require approval, permission, and account-specific pricing states

