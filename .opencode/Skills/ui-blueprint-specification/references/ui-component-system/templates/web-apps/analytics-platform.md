---
template_id: analytics-platform
template_name: Analytics Platform
category: web-app
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Reporting and analytics architecture for dashboards, charts, filters, saved views, drilldowns, exports, and metric investigation.
suitable_for:
  - analytics-products
  - reporting-tools
  - business-intelligence
  - monitoring-dashboards
unsuitable_for:
  - simple-crud-admin
  - public-content-sites
  - checkout-heavy-commerce
---

# Analytics Platform

Structural defaults:

- navigation: `sidebar-navigation`
- utility navigation: top bar with date range, account, and saved view controls
- common layouts: `dashboard-grid`, `data-table`, `master-detail`, `split-pane`
- density: data-dense

Required page archetypes:

- `dashboard`
- `analytics`
- `detail`
- `search-results`

Conditional page archetypes:

- `collection`
- `settings`
- `create-edit`

Common component families:

- navigation
- actions
- data-display
- search-and-filtering
- feedback
- overlays
- analytics

Layout rules:

- use `dashboard-grid` for metric overviews, KPI panels, and chart compositions
- use `data-table` for underlying records, reports, exports, and drilldown result sets
- use `master-detail` or `split-pane` for metric investigation with persistent context
- require loading, partial-data, empty, stale-data, and error states for every data panel

