---
name: ux-enforcement
description: Validate and enforce that implemented interfaces correctly follow the planned UX. This skill ensures that user flows, interactions, and states are implemented as intended, with no missing steps, hidden actions, or usability regressions.
compatibility: opencode
---

## Purpose

This skill ensures that **planned UX is correctly implemented**.

It does NOT design UX.
It does NOT design UI aesthetics.

It validates:
- user flows
- interaction logic
- usability clarity
- state handling

It identifies gaps and provides corrections.

---

## When to Use

Invoke when:

- verifying a built UI against a defined UX flow
- reviewing frontend implementations
- ensuring no UX steps are missing
- validating interaction logic before deployment
- debugging usability issues
- refining flows after implementation

---

## Required Inputs

- planned UX (flows, steps, or description)
- implemented UI (code, components, or description)

If one is missing, request it.

---

## Execution Pipeline

### 1. Parse Planned UX

Extract:

- primary user goal
- steps in flow
- decisions required
- expected system responses
- expected states
- page interaction contracts
- stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` references
- route types and action outcomes

---

### 2. Parse Implementation

Identify:

- available actions in UI
- navigation paths
- feedback mechanisms
- state handling (loading, error, success)
- implemented labels, accessible names, route targets, action outcomes, permission behavior, and confirmations

---

### 3. Flow Matching

Compare:

- planned steps vs implemented steps
- expected actions vs actual actions
- expected transitions vs actual navigation
- planned stable interaction IDs vs implemented controls and handlers
- planned Mermaid branches vs implemented complex flows

---

### 4. Gap Detection

Identify:

- missing steps
- hidden or unclear actions
- extra/unnecessary steps
- broken or indirect flows
- mismatched system responses

---

### 5. Interaction Validation

Check:

- is the primary action obvious?
- are actions clearly labeled?
- is feedback immediate and clear?
- are decisions minimized?
- do route, action, confirmation, permission, recovery, mobile, and accessibility behaviors match the interaction contract?
- are nested clickable containers and controls unambiguous?

---

### 6. State Validation

Verify presence of:

- loading state
- success state
- error state
- empty state

Ensure each state:
- provides feedback
- offers next action

---

### 7. Friction Analysis

Detect:

- unnecessary clicks or steps
- confusing navigation
- unclear outcomes
- cognitive overload

---

### 8. Correction Output

Provide:

- exact issues
- severity level (low, medium, high, critical)
- clear fix instructions
- optional improved flow if needed

---

## Output Structure

### 1. UX Compliance Summary

- overall alignment: (high / medium / low)
- critical issues:
- major gaps:

---

### 2. Flow Comparison

Planned vs Implemented:

- Step 1:
- Step 2:
- Step 3:

Highlight mismatches.

---

### 3. Issues & Fixes

For each issue:

- issue:
- severity:
- impact:
- fix:

---

### 4. Missing States

List any missing:

- loading
- success
- error
- empty

---

### 5. Friction Points

- unnecessary steps
- unclear interactions
- usability blockers

---

### 6. Recommended Improvements

- simplified flow
- improved interaction clarity
- better feedback handling

---

## Rules

- do NOT redesign UI visually
- do NOT introduce new features unless required to fix UX
- stay aligned with original UX intent
- prioritize correctness over creativity

---

## Anti-Patterns (Strict)

- skipping validation of steps
- assuming flows instead of verifying
- ignoring edge cases
- allowing unclear primary actions
- approving incomplete flows
- approving dropped, renamed, rerouted, or behavior-changed interactions without an approved deviation

---

## Severity Levels

- low → minor clarity issue
- medium → noticeable friction
- high → user confusion likely
- critical → flow is broken or incomplete

---

## Final Rule

Every output must answer:

"Can the user complete the intended goal quickly, clearly, and correctly?"

If not, it must be fixed.
