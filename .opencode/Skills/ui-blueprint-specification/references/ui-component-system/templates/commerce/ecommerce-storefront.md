---
template_id: ecommerce-storefront
template_name: Ecommerce Storefront
category: commerce
version: 1.0.0
status: stable
extends: base-ui-architecture
description: Product discovery, cart, checkout, account, and order-management architecture.
suitable_for:
  - product-catalogs
  - marketplaces
  - storefronts
unsuitable_for:
  - pure-content-sites
  - internal-only-admin-tools
---

# Ecommerce Storefront

Structural defaults:

- navigation: `top-navigation`
- mobile navigation: `navigation-drawer` or `bottom-navigation`
- common layouts: `card-grid`, `data-table`, `form-layout`, `single-column`

Required page archetypes:

- `landing-page`
- `collection`
- `detail`
- `search-results`
- `checkout`
- `profile`

Common component families:

- navigation
- commerce
- actions
- forms
- search-and-filtering
- feedback

Layout rules:

- use `card-grid` for product/category browsing when image recognition matters
- use `data-table` for order history, admin inventory, or comparable operational rows
- use `form-layout` for checkout, shipping, billing, and account forms

