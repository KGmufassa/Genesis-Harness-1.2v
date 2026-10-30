# Layout Decision Matrix

Use this matrix to choose `layout_pattern_decision.selected_pattern` for each launch-critical page.

| Page/workflow condition | Default pattern | Reject/avoid | Required validation |
| --- | --- | --- | --- |
| Many comparable records, consistent fields, filtering, sorting, pagination, or bulk actions | `data-table` | `card-grid` unless visual browsing dominates | Mobile transformation, column priority, sorting/filtering, loading, empty, no-results, error, bulk selection |
| Visual browsing, media-rich items, uneven item summaries, lightweight comparison | `card-grid` | `data-table` unless dense field comparison dominates | Card anatomy, responsive columns, nested click-target rules |
| Chronological feed, activity, messages, simple repeated records | `content-list` | `data-table` for non-comparable content | Pagination/loading, item action behavior, no-results |
| Browse list while repeatedly inspecting or editing selected item | `master-detail` | full detail route when detail is complex; split UI on mobile without transformation | Selected item state, empty selection state, mobile stacked/routed behavior |
| Metrics, charts, alert panels, operational summary | `dashboard-grid` | `data-table` when one collection dominates | Panel priority, responsive stacking, partial/stale data behavior |
| Create, edit, setup, review, submit structured data | `form-layout` | dashboard/grid layouts | Field grouping, validation, success/failure, unsaved changes |
| Grouped preferences, account, permissions, integrations, billing config | `settings-layout` | generic form layout for many unrelated groups | Group navigation, dirty states, permission-denied behavior |
| Two related work surfaces must remain visible together | `split-pane` | master-detail if one side is only selected detail | Pane priority, collapse behavior, focus order |

Inventory rule:

- Inventory operations with comparable SKU/item rows, quantities, statuses, filters, and bulk updates default to `data-table`.
- Inventory/catalog browsing with image-first product recognition defaults to `card-grid`.
- Inventory management that frequently inspects or edits one selected item while browsing defaults to `master-detail`.

Decision object minimum:

```json
{
  "selected_pattern": "",
  "rejected_patterns": [],
  "decision_factors": {
    "information_density": "",
    "comparison_need": "",
    "scan_behavior": "",
    "primary_user_task": "",
    "record_count": "",
    "bulk_actions_required": false,
    "mobile_behavior_required": true
  },
  "reasons": [],
  "source_refs": [],
  "responsive_transformation": {
    "desktop": "",
    "tablet": "",
    "mobile": ""
  }
}
```

