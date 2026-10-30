---
template_id: base-ui-architecture
template_name: Base UI Architecture
category: base
version: 1.0.0
status: stable
extends: ""
description: Shared structural requirements for all Stage 4 UI architecture templates.
suitable_for:
  - all-interface-architecture
unsuitable_for: []
---

# Base UI Architecture

Required rules:

- every page has purpose, primary user, primary goal, entry points, and exit points
- every page declares one page archetype
- every launch-critical page records one selected layout pattern with reasons
- every data region defines loading, empty, error, populated, and permission-denied behavior when applicable
- every navigation destination maps to a real page or external target
- every major component has one clear responsibility
- every primary action is identifiable
- every interactive component defines keyboard, touch, responsive, and accessibility behavior

Base page structure:

```yaml
page:
  id:
  name:
  route:
  archetype:
  purpose:
  primary_user:
  primary_goal:
  entry_points: []
  exit_points: []
navigation:
  parent:
  primary_location:
  breadcrumbs: []
  tabs: []
header:
  title:
  description:
  primary_action:
  secondary_actions: []
layout:
  pattern:
  content_width:
  columns:
  regions: []
components: []
states:
  loading:
  empty:
  error:
  populated:
  permission_denied:
responsive:
  desktop:
  tablet:
  mobile:
accessibility:
  landmarks:
  heading_order:
  keyboard_flow:
  focus_behavior:
```

