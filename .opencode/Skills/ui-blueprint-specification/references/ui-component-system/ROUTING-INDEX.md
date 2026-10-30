# UI Component System Routing Index

Use this file first. Load only the references needed for the current Stage 4 decision.

| Decision need | Required references |
| --- | --- |
| Understand library boundaries | `README.md` |
| Select primary UI architecture template | `TEMPLATE-SELECTOR.md`, `TEMPLATE-REGISTRY.md`, selected template |
| Normalize user language to canonical values | `NORMALIZED-VALUES.md` |
| Apply rule precedence | `PRECEDENCE-RULES.md` |
| Compose extensions | `extensions/EXTENSION-COMPATIBILITY.md`, `extensions/TEMPLATE-COMPOSITION.md`, selected extensions |
| Choose page layout pattern | `LAYOUT-DECISION-MATRIX.md`, directly relevant `patterns/layouts/*.md` |
| Choose page archetype | `NORMALIZED-VALUES.md`, directly relevant `patterns/pages/*.md` |
| Choose component families | `NORMALIZED-VALUES.md`, selected template, selected extensions |
| Validate output completeness | `OUTPUT-CHECKLIST.md` |
| Detect contradictions | `CONTRADICTION-RULES.md` |
| Record recurring gaps | `MAINTENANCE.md` |
| See expected output shape | `examples/*.json` |

Minimum normal Stage 4 read set:

1. `ROUTING-INDEX.md`
2. `TEMPLATE-SELECTOR.md`
3. `NORMALIZED-VALUES.md`
4. selected template
5. selected extensions
6. directly relevant layout/page/interaction/state patterns
7. `OUTPUT-CHECKLIST.md`
8. `CONTRADICTION-RULES.md`

Do not load every pattern file by default.

Template routing shortcuts:

| Product shape | Candidate template |
| --- | --- |
| public conversion, positioning, pricing, lead capture | `templates/websites/marketing-website.md` |
| articles, authors, categories, archives, recurring publication | `templates/websites/editorial-content-site.md` |
| guides, API/product docs, reference content, changelog, help center | `templates/websites/documentation-site.md` |
| project gallery, creative portfolio, case studies, services | `templates/websites/portfolio-showcase.md` |
| customer-facing SaaS dashboard or business workflow app | `templates/web-apps/saas-dashboard.md` |
| internal CRUD/admin/inventory/operations tool | `templates/web-apps/internal-admin-tool.md` |
| metrics, reports, dashboards, drilldowns, saved views | `templates/web-apps/analytics-platform.md` |
| shared workspace, team coordination, comments, messaging, presence | `templates/web-apps/collaboration-workspace.md` |
| single-seller storefront and checkout | `templates/commerce/ecommerce-storefront.md` |
| multi-sided buyer/seller or provider/customer platform | `templates/commerce/marketplace-platform.md` |
| account-based B2B purchasing, quotes, bulk orders, approvals | `templates/commerce/b2b-commerce-portal.md` |
| mobile repeated task utility | `templates/mobile/mobile-utility.md` |
| mobile content feed/media/learning consumption | `templates/mobile/mobile-content-platform.md` |
| mobile social/community participation | `templates/mobile/mobile-social-community.md` |
