# Template Registry

```yaml
templates:
  - id: marketing-website
    category: website
    version: 1.0.0
    status: stable

  - id: editorial-content-site
    category: website
    version: 0.1.0
    status: draft

  - id: documentation-site
    category: website
    version: 0.1.0
    status: draft

  - id: portfolio-showcase
    category: website
    version: 0.1.0
    status: draft

  - id: saas-dashboard
    category: web-app
    version: 1.0.0
    status: stable

  - id: internal-admin-tool
    category: web-app
    version: 0.1.0
    status: draft

  - id: analytics-platform
    category: web-app
    version: 0.1.0
    status: draft

  - id: collaboration-workspace
    category: web-app
    version: 0.1.0
    status: draft

  - id: ecommerce-storefront
    category: commerce
    version: 1.0.0
    status: stable

  - id: marketplace-platform
    category: commerce
    version: 0.1.0
    status: draft

  - id: b2b-commerce-portal
    category: commerce
    version: 0.1.0
    status: draft

  - id: mobile-utility
    category: mobile
    version: 1.0.0
    status: stable

  - id: mobile-content-platform
    category: mobile
    version: 0.1.0
    status: draft

  - id: mobile-social-community
    category: mobile
    version: 0.1.0
    status: draft
```

Version rules:

- major: breaking schema or architectural changes
- minor: new templates, extensions, pages, or capabilities
- patch: corrections and clarification

Draft-to-stable promotion follows `MAINTENANCE.md` and requires three completed Stage 4 uses across two products plus responsive, accessibility, routing, and gap-resolution evidence.
