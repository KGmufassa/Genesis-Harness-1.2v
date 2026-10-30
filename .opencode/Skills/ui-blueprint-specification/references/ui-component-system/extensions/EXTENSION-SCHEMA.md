# Extension Schema

Extensions add product-specific UI architecture to a primary template without creating a new template.

```yaml
extension:
  id:
  name:
  version:
  compatible_with: []
  description:

adds:
  pages: []
  components: []
  interactions: []
  states: []

modifies:
  navigation: []
  layouts: []
  responsive_behavior: []

requires:
  product_conditions: []
```

Extensions must be additive or modifying. They must not redefine product scope, backend architecture, API design, visual design language, implementation technology, or final frontend code.

