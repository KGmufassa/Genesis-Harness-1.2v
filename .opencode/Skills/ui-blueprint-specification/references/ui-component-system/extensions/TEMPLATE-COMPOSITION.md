# Template Composition

Composition shape:

```yaml
ui_architecture:
  primary_template: saas-dashboard
  extensions:
    - analytics
    - role-based-access
    - collaboration
```

Use extensions when product conditions require pages, components, interactions, or states that should not be baked into every primary template.

Record selected extensions in `ui_architecture_template_selection.selected_extensions` and each affected page's `ui_architecture.selected_extensions`.

Before applying extensions, check `EXTENSION-COMPATIBILITY.md` for conflicts, stacking rules, and required composition order.
