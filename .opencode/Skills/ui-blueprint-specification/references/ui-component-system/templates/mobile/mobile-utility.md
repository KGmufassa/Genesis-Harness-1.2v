---
template_id: mobile-utility
template_name: Mobile Utility
category: mobile
version: 1.0.0
status: stable
extends: base-ui-architecture
description: Mobile-first architecture for short repeated tasks, interrupted sessions, and one-handed interaction.
suitable_for:
  - mobile-first-tools
  - repeated-task-products
  - field-workflows
unsuitable_for:
  - desktop-dense-record-management
  - large-comparison-workflows
---

# Mobile Utility

Structural defaults:

- navigation: `bottom-navigation`
- secondary navigation: `navigation-drawer`
- common layouts: `single-column`, `content-list`, `form-layout`
- touch targets: large

Required page archetypes:

- `mobile-home`
- `primary-task`
- `settings`

Conditional page archetypes:

- `onboarding`
- `profile`
- `collection`

Layout rules:

- avoid desktop-only tables
- prefer focused task surfaces over multi-column dashboards
- use bottom sheets only for short supporting decisions, not long workflows

