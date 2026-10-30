---
template_id: marketplace-platform
template_name: Marketplace Platform
category: commerce
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Multi-sided commerce architecture for buyers, sellers, listings, discovery, trust, messaging, transactions, and account areas.
suitable_for:
  - marketplaces
  - buyer-seller-platforms
  - service-marketplaces
  - creator-or-provider-platforms
unsuitable_for:
  - single-seller-storefronts
  - internal-only-admin-tools
  - pure-content-sites
---

# Marketplace Platform

Structural defaults:

- navigation: `top-navigation`
- authenticated workspace navigation: `sidebar-navigation` where seller/provider tools exist
- common layouts: `card-grid`, `content-list`, `data-table`, `form-layout`, `dashboard-grid`
- density: balanced

Required page archetypes:

- `landing-page`
- `collection`
- `detail`
- `search-results`
- `profile`
- `checkout`

Conditional page archetypes:

- `dashboard`
- `messaging`
- `settings`
- `create-edit`

Common component families:

- navigation
- commerce
- actions
- forms
- data-display
- search-and-filtering
- messaging
- feedback

Layout rules:

- use `card-grid` for buyer-side listing discovery
- use `detail` pages for trust, seller/provider identity, availability, and conversion
- use `data-table` for seller/provider management, orders, payouts, or listing administration
- require role-specific navigation for buyer, seller, provider, and admin surfaces

