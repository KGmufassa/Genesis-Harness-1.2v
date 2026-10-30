---
template_id: collaboration-workspace
template_name: Collaboration Workspace
category: web-app
version: 0.1.0
status: draft
extends: base-ui-architecture
description: Multi-user workspace architecture for shared objects, comments, assignments, activity, messaging, presence, and team coordination.
suitable_for:
  - team-workspaces
  - project-collaboration
  - shared-document-products
  - task-coordination-tools
unsuitable_for:
  - public-static-sites
  - single-user-mobile-utilities
  - pure-storefront-commerce
---

# Collaboration Workspace

Structural defaults:

- navigation: `sidebar-navigation`
- secondary navigation: `tabs` and contextual navigation
- common layouts: `content-list`, `master-detail`, `split-pane`, `form-layout`
- density: balanced

Required page archetypes:

- `dashboard`
- `collection`
- `detail`
- `messaging`
- `settings`

Conditional page archetypes:

- `onboarding`
- `profile`
- `analytics`

Common component families:

- navigation
- actions
- forms
- data-display
- feedback
- overlays
- collaboration
- messaging

Layout rules:

- use `master-detail` for task, conversation, or document browsing with selected detail
- use `split-pane` when two work surfaces must stay visible together
- use `content-list` for activity feeds, comments, messages, and updates
- require optimistic, conflict, permission, and notification behavior for shared edits

