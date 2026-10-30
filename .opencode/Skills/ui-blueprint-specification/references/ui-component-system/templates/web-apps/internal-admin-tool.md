---
template_id: internal-admin-tool
template_name: Internal Admin Tool
category: web-app
version: 0.1.0
status: draft
extends: base-ui-architecture
description: CRUD-heavy internal operations architecture for records, inventory, approvals, imports, exports, admin settings, and audit-sensitive workflows.
suitable_for:
  - internal-tools
  - admin-panels
  - inventory-management
  - operational-workflows
unsuitable_for:
  - public-marketing-sites
  - image-first-storefronts
  - mobile-only-utility-products
---

# Internal Admin Tool

Structural defaults:

- navigation: `sidebar-navigation`
- utility navigation: top bar
- common layouts: `data-table`, `master-detail`, `form-layout`, `settings-layout`, `dashboard-grid`
- density: balanced to data-dense

Required page archetypes:

- `dashboard`
- `collection`
- `detail`
- `create-edit`
- `settings`

Conditional page archetypes:

- `analytics`
- `search-results`
- `authentication`

Common component families:

- navigation
- actions
- forms
- data-display
- feedback
- overlays
- search-and-filtering

Layout rules:

- use `data-table` for inventory, users, orders, vendors, logs, and comparable operational records
- use `master-detail` when operators inspect or update many records quickly
- use `form-layout` for create/edit, import mapping, and review flows
- use `settings-layout` for roles, permissions, integrations, and admin configuration
- preserve permission-denied and audit-sensitive states for restricted actions

