---
template_id: mobile-content-platform
template_name: Mobile Content Platform
category: mobile
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Mobile-first content consumption architecture for feeds, media, search, profiles, saved items, and lightweight engagement.
suitable_for:
  - mobile-content-products
  - media-apps
  - learning-content-apps
  - creator-content-apps
unsuitable_for:
  - dense-admin-tools
  - desktop-record-management
  - procurement-commerce
---

# Mobile Content Platform

Structural defaults:

- navigation: `bottom-navigation`
- secondary navigation: `navigation-drawer`
- common layouts: `content-list`, `card-grid`, `single-column`
- density: readable to balanced

Required page archetypes:

- `mobile-home`
- `collection`
- `detail`
- `search-results`
- `profile`

Conditional page archetypes:

- `onboarding`
- `settings`
- `authentication`

Common component families:

- navigation
- actions
- data-display
- search-and-filtering
- feedback

Layout rules:

- use `content-list` for feeds and recency-driven content
- use `card-grid` for visual browsing and saved collections
- use `single-column` for reading, watching, listening, or lesson detail
- prioritize offline, loading, and interrupted-session behavior on mobile

