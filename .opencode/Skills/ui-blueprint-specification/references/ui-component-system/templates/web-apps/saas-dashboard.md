---
template_id: saas-dashboard
template_name: SaaS Dashboard
category: web-app
version: 1.0.0
status: stable
extends: base-ui-architecture
description: Workspace-oriented interface architecture for recurring business workflows, record management, monitoring, and account administration.
suitable_for:
  - business-saas
  - customer-portals
  - subscription-platforms
  - internal-tools
unsuitable_for:
  - simple-landing-pages
  - editorial-websites
  - single-screen-mobile-tools
---

# SaaS Dashboard

Structural defaults:

- navigation: `sidebar-navigation`
- utility navigation: top bar
- common layouts: `dashboard-grid`, `data-table`, `master-detail`, `form-layout`, `settings-layout`
- density: balanced to data-dense

Required page archetypes:

- `dashboard`
- `collection`
- `detail`
- `create-edit`
- `settings`

Conditional page archetypes:

- `analytics`
- `onboarding`
- `profile`
- `messaging`

Common component families:

- navigation
- actions
- forms
- data-display
- feedback
- overlays
- search-and-filtering

Layout rules:

- use `data-table` for dense comparable records, sorting, filtering, and bulk actions
- use `master-detail` when users repeatedly inspect records while browsing
- use `dashboard-grid` for cross-surface summaries and operational metrics
- use `form-layout` for create/edit flows
- use `settings-layout` for grouped preferences, permissions, or account configuration

