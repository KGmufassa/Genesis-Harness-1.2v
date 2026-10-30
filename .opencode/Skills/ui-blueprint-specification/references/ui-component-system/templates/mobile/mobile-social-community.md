---
template_id: mobile-social-community
template_name: Mobile Social Community
category: mobile
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Mobile-first community architecture for feeds, profiles, posting, messaging, groups, notifications, moderation, and social discovery.
suitable_for:
  - social-apps
  - community-products
  - creator-communities
  - group-based-mobile-products
unsuitable_for:
  - private-admin-tools
  - static-content-sites
  - pure-utility-task-apps
---

# Mobile Social Community

Structural defaults:

- navigation: `bottom-navigation`
- secondary navigation: `navigation-drawer`
- common layouts: `content-list`, `card-grid`, `single-column`, `form-layout`
- density: balanced

Required page archetypes:

- `mobile-home`
- `collection`
- `detail`
- `profile`
- `messaging`

Conditional page archetypes:

- `onboarding`
- `search-results`
- `settings`
- `authentication`

Common component families:

- navigation
- actions
- forms
- data-display
- feedback
- messaging
- collaboration

Layout rules:

- use `content-list` for feeds, comments, messages, notifications, and activity
- use `form-layout` for posting, reporting, profile editing, and moderation flows
- require moderation, notification, permission, blocked-user, and offline states when applicable

