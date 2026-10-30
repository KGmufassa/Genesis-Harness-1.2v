---
name: mapping-user-flow-progression
description: Maps detailed user experience progression and trigger-level interaction flows for an application. Use when defining page-by-page UX behavior, click triggers, state transitions, and navigation progression before implementation.
compatibility: opencode
---

Reference documents: 
- /frontend/reference/ui-ux-draft.md
- or user defined 

---
# Mapping Ux Flows

## Purpose

This skill designs a deterministic play-by-play breakdown of:

- User experience progression
- Page transitions
- Trigger-level interactions
- State changes
- Navigation logic
- Backend hooks (if applicable)

It outputs:

- A master flow overview file
- Individual markdown files per page
- Detailed trigger progression chains

---

# Core Rules

1. Never assume UX behavior.
2. Ask meaningful UX/system questions first.
3. Ask one clarifying question at a time.
4. Do not generate page files until core flow is defined.
5. Every trigger must define:
   - Source
   - Action
   - State change
   - Navigation result
   - Backend event (if applicable)

---

# Workflow

Copy and track:

Flow Mapping Progress:
- [ ] Step 1: Define app entry point
- [ ] Step 2: Define primary user goal
- [ ] Step 3: Define core navigation structure
- [ ] Step 4: Identify all pages
- [ ] Step 5: Map page progression order
- [ ] Step 6: Map trigger-level behavior
- [ ] Step 7: Define system reactions
- [ ] Step 8: Generate markdown files

---

# Step 1 — Clarifying Experience Questions

Ask one at a time:

Examples:

- What is the very first screen a user sees?
- Is onboarding required?
- Is the app account-based or session-based?
- Is the navigation persistent or contextual?
- Is it mobile-first or desktop-first?
- Are actions optimistic (instant UI change) or confirmed by backend response?
- Should interactions feel fast and minimal or guided and explanatory?

Continue until flow clarity is achieved.

Do not proceed without clear answers.

---

# Step 2 — Define Core Flow Structure

Output:

## Primary Flow

Entry → Action → Result → Next State

Example:

Landing → Sign Up → Dashboard → Create Item → Review → Submit → Confirmation

---

# Step 3 — Page Inventory

List:

1. Page Name
2. Purpose
3. Entry Points
4. Exit Routes

Do not design triggers yet.

---

# Step 4 — Trigger-Level Mapping

For each page define:

## Page: [Page Name]

### Entry Conditions
How user arrives.

### Layout Zones
- Header
- Navigation
- Main content
- Secondary panels
- Modals

---

### Trigger Table

| Trigger | Location | Action | State Change | Navigation | Backend Hook |
|---------|----------|--------|--------------|------------|--------------|

Every clickable element must appear here.

---

### System Reactions

Define:

- Loading state
- Error state
- Success state
- Empty state

---

### Edge Case Handling

- Network failure
- Invalid input
- Permission issues

---

# Step 5 — Progression Chains

Define click-level chains:

Example:

User clicks "Create" →
Modal opens →
User inputs data →
Clicks Save →
Loading state →
Backend validation →
Success →
Redirect to Detail Page →
Toast confirmation

Every multi-step interaction must be defined as a linear chain.

---

# Step 6 — Output Structure

Create:

docs/Frontend/ui-ux-design/ux-flows/overview.md  
docs/Frontend/ui-ux-design/ux-flows/pages/[page-name].md  

If folder does not exist:
Create it.

---

# Overview File Format

# Application Flow Overview

## Primary User Journey
## Secondary Flows
## Trigger Dependency Graph
## State Transition Summary

---

# Individual Page File Format

# Page: [Page Name]

## Purpose
## Entry Conditions
## Exit Conditions
## Layout Structure
## Trigger Map
## Interaction Chains
## State Management
## Edge Cases
## Backend Events

---

# Constraints

NEVER:
- Skip defining state transitions
- Leave trigger undefined
- Merge flows ambiguously
- Assume backend confirmation timing
- Create page without entry/exit definition

ALWAYS:
- Force deterministic UX behavior
- Map progression sequentially
- Ensure reproducible navigation logic
- Keep documentation implementation-ready

---

# Output Confirmation

After generation:

Return:

1. Number of pages created
2. Files written
3. Missing behavioral definitions
4. Any unresolved UX ambiguity
