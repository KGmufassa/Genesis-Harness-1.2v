---
name: creating-dynamic-wireframes
description: Reads product documentation or PRD files and generates structured, low-fidelity wireframes with deterministic page architecture, state definitions, trigger mapping, and annotated ASCII layouts. Supports dynamic workflow detection and safe update mode.
Default file: docs/Frontend/ui-ux-design/ux-flows/overview.md
compatibility: opencode
---

# Creating Dynamic Wireframes

## Purpose

This skill interprets structured or semi-structured documentation (PRDs, markdown files, feature specs, notes) and produces deterministic, low-fidelity wireframes.

It focuses on:

- Structural hierarchy
- Page architecture
- Navigation logic
- Trigger mapping
- User flow
- State definitions
- Annotated ASCII diagrams

It never guesses.  
It asks one clarifying question at a time when required.

---

# Core Principles

1. Structure over visuals.
2. Never assume missing UX decisions.
3. Always define entry and exit conditions.
4. Every interactive element must map to a defined action.
5. Every page must include all possible states.
6. Validate completeness before output.

---

# Mode Detection

## Automatic Modes

If a file is provided → `interpret-file` mode  
If no file is provided → `interpret default file` mode  
If updating an existing wireframe file → `update` mode  

---

# Step 1 — File Ingestion (Interpret-File Mode)

If a file path is provided:

1. Read file fully.
2. Extract:
   - Product type
   - Core features
   - User roles
   - Navigation references
   - States mentioned
   - Explicit pages
   - Device assumptions
   - Entry points
   - Success outcomes

3. Detect missing critical UX data.

If unclear:
Ask one question.

Do not proceed to layout until clarified.

---

# Step 2 — Workflow Detection

Auto-detect workflow type:

- Marketing site → Website workflow
- Product app → App workflow
- Admin panel → Dashboard workflow
- Multi-step journey → Flow workflow

If ambiguous:
Ask:
“Is this a marketing site, product app, dashboard, or flow-based system?”

---

# Step 3 — Page Architecture Engine

Determine:

- Required pages
- Required states per page
- Feature clustering
- Logical separation of responsibilities

Output:

## MVP Page Map

1. Page Name
   - Purpose
   - Entry
   - Exit

Do not create wireframes yet.

---

# Step 4 — Structural Validation Pass

Before wireframing, confirm:

- Device priority (mobile-first, desktop-first)
- Navigation type (sidebar, top nav, tabs, contextual)
- Auth required?
- Role-based variations?
- Persistent layout or per-page layout?

Ask one missing item at a time.

---

# Step 5 — Wireframe Construction

For each page:

## WIREFRAME SPECIFICATION

**Project:**  
**Page:**  
**Device Priority:**  

---

## USER FLOW

Entry → Action → Result → Next Step

---

## ASCII WIREFRAME

Use structured low-fidelity layout.

Example:

```
+----------------------------------+
| HEADER                          |
| [Logo] [Nav] [Nav] [CTA]        |
+----------------------------------+

+----------------------------------+
| MAIN CONTENT                    |
|                                  |
| [Primary Action]                 |
|                                  |
+----------------------------------+

+----------------------------------+
| FOOTER                          |
+----------------------------------+
```
All components must be labeled.

---

## COMPONENT MAP

| Component | Type | Purpose | Interaction |
|----------|------|----------|-------------|

No unlabeled components allowed.

---

## TRIGGER MAP

| Trigger | Location | Action | State Change | Navigation |
|---------|----------|--------|--------------|------------|

Every clickable item must be listed.

---

## STATES (Mandatory)

Each page must define:

- Default
- Loading
- Error
- Empty
- Success

No page may omit states.

---

## EDGE CASES

- Invalid input
- Network failure
- Permission issues
- Unexpected system error

---

## RESPONSIVE NOTES

- Mobile behavior
- Tablet behavior
- Desktop behavior
- Layout shifts

---

# Step 6 — Flow Connections

Define transitions between pages:

Page A → Trigger → Page B

Indicate arrows:

A → B  
A ? Decision → B or C  

All paths must terminate.

---

# Step 7 — Output Structure

Write files to:

/frontend/reference/wireframes/

Create:

/frontend/ui-ux-design/wireframes/overview.md  
/frontend/ui-ux-design/wireframes/[page-name].md  

If updating:
- Append new pages
- Preserve existing structure
- Add revision section

Never overwrite unless explicitly instructed.

---

# Integrity Validation Rules

Before writing files, verify:

- Every feature is mapped to a page.
- No orphan CTA exists.
- No page without entry and exit.
- No trigger without defined outcome.
- All states are documented.
- Navigation paths are closed loops.

If violations exist:
Ask clarification.

---

# Prohibited Actions

NEVER:

- Guess page count
- Skip state definitions
- Create ambiguous navigation
- Generate incomplete flows
- Merge unrelated features
- Assume device priority
- Assume authentication logic

---

# Required Output Confirmation

After generation return:

1. Workflow detected
2. Pages created
3. Files written
4. Missing clarifications (if any)
5. Structural validation status

---

# Fidelity Level

Default: Low-fidelity ASCII  
If user specifies mid or high fidelity → adjust structure only, not visuals.

---

# Design Philosophy

This skill creates structural contracts, not visual design.

It locks:

- Information architecture
- Interaction behavior
- Navigation logic
- State handling
- UX determinism

Before high-fidelity design or implementation.
