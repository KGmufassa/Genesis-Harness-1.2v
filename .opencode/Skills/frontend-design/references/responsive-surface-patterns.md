# Responsive Surface Patterns

Use this file when adapting a specific interface type across breakpoints.

## Core Responsive Techniques

Use these deliberately:
- reflow
- show and hide
- re-architect
- resize

Source note:
- Fluent identifies reflow, show/hide, re-architect, and resize as core responsive techniques.

## Dashboard

Small screens:
- reduce simultaneous visible modules
- collapse secondary filters and actions
- preserve one clear primary task path

Large screens:
- keep orientation aids persistent
- allow more metadata and side-by-side context

## List-Detail

Compact screens:
- show list or detail, not both

Expanded screens:
- show list and detail together when it materially improves task flow

Source note:
- Android canonical layouts explicitly supports compact-to-expanded list-detail behavior.

## Workspace / Split-Pane

Small screens:
- collapse supporting panes into drawers, sheets, or staged views
- preserve the active object and main action surface

Large screens:
- restore contextual panes only when they reduce switching cost

## Settings

Small screens:
- use grouped stacked lists and separate screens where needed

Large screens:
- allow grouped overview and detail relationships when readable

## Marketing + App Hybrid

Small screens:
- simplify narrative pacing and avoid heavy parallel composition

Large screens:
- allow expressive section width and varied margins in marketing areas
- keep product areas structured and repeatable

## Output Expectation

When defining responsive behavior for a surface, specify:
- what reflows
- what hides
- what moves into overflow
- what gets re-architected
- what remains persistent
