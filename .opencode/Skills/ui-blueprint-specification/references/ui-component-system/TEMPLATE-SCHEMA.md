# UI Architecture Template Schema

Every UI architecture template must define:

- template identity
- product characteristics
- suitable and unsuitable product conditions
- structural defaults
- information architecture
- navigation architecture
- application shell
- required and conditional page archetypes
- layout rules
- component families
- interaction patterns
- responsive strategy
- system states
- accessibility requirements
- adaptation rules
- output guidance for Stage 4 UI blueprints

Template frontmatter:

```yaml
---
template_id: ""
template_name: ""
category: ""
version: "1.0.0"
status: stable
extends: base-ui-architecture
description: ""
suitable_for: []
unsuitable_for: []
---
```

Rule levels:

- `required`: normally necessary for this archetype
- `recommended`: default unless the project provides a reason to change it
- `conditional`: apply only when product conditions exist
- `prohibited`: normally incompatible with the archetype

Templates provide defaults. Stage 4 must still preserve upstream product, workflow, role, architecture, accessibility, and MVP constraints.

