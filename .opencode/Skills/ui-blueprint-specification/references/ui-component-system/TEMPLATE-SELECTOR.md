# Template Selector

Use the selector after `design-system-foundation` and before `ui-blueprint-specification`.

Required selector inputs:

- product category
- primary platform
- primary user behavior
- dominant workflow
- content type
- information density
- comparison needs
- collaboration level
- transaction model
- session frequency

Selection rules:

| Product condition | Primary template |
| --- | --- |
| Promotion, conversion, content-first experience | `marketing-website` |
| Recurring publishing, articles, authors, categories, archives, editorial search | `editorial-content-site` |
| Product docs, developer docs, guides, references, help center, changelog | `documentation-site` |
| Creative work, case studies, project gallery, services, lightweight contact conversion | `portfolio-showcase` |
| Recurring business workflows, desktop web, structured records | `saas-dashboard` |
| CRUD-heavy internal operations, inventory, imports, exports, admin records, permissions | `internal-admin-tool` |
| Reporting, dashboards, metrics, charts, saved views, drilldowns, exports | `analytics-platform` |
| Shared workspace, comments, assignments, activity, messaging, presence | `collaboration-workspace` |
| Direct purchasing, storefront browsing, seller-to-customer transaction model | `ecommerce-storefront` |
| Multi-sided buyer/seller or provider/customer platform with listings, trust, messaging | `marketplace-platform` |
| Account-based purchasing, quotes, bulk ordering, approvals, negotiated pricing | `b2b-commerce-portal` |
| Focused repeated task, mobile-first platform | `mobile-utility` |
| Mobile-first feed, media, saved content, search, profile, lightweight engagement | `mobile-content-platform` |
| Mobile-first community, posting, social feed, messaging, groups, moderation | `mobile-social-community` |

Tie-breaker rules:

- If a draft template and a stable template both match, select the draft template only when its condition is the dominant product workflow.
- Use `saas-dashboard` instead of `internal-admin-tool` when the product is customer-facing SaaS rather than internal operations.
- Use `internal-admin-tool` for inventory-style pages with dense comparable records, filters, imports, exports, and permissions.
- Use `ecommerce-storefront` for single-seller consumer purchasing; use `marketplace-platform` for multi-sided commerce; use `b2b-commerce-portal` for account-based purchasing.
- Use `mobile-utility` for repeated task completion; use `mobile-content-platform` for consumption; use `mobile-social-community` for social participation.

Selector output:

```json
{
  "primary_template": "",
  "confidence": "high | medium | low",
  "alternative_templates": [],
  "selected_extensions": [],
  "reasons": [],
  "unresolved_questions": [],
  "template_deviations": [],
  "template_gaps": [],
  "source_refs": []
}
```

Ask the user only when template choice materially changes page inventory, navigation, or Stage 5 frontend scope. Otherwise infer from Stage 1 product/workflow inputs and Stage 4 journeys.
