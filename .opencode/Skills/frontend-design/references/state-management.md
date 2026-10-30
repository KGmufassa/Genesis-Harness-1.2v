# State Management

Use this file when deciding where frontend state should live.

## Selection Rule

Choose the simplest state model that correctly represents the problem.

```text
Local state (useState)           → Component-specific UI state
Lifted state                     → Shared between 2-3 sibling components
Context                          → Theme, auth, locale
URL state (searchParams)         → Filters, pagination, shareable UI state
Server state (React Query, SWR)  → Remote data with caching
Global store (Zustand, Redux)    → Complex client state shared app-wide
```

## Rules

- local UI state belongs close to the component that owns it
- lifted state is enough for a small cluster of related children
- use context for read-heavy, write-rare cross-cutting concerns
- use URL state for shareable or navigable interface state
- use server-state tools for remote data, caching, invalidation, and sync
- use a global store only when client state is complex and truly cross-cutting

## Prop Drilling Rule

Avoid prop drilling deeper than 3 levels. If props are passing through components that do not use them:
- introduce context
- restructure the tree
- or change the ownership boundary

## Output Expectation

When using this reference, specify:
- chosen state model
- why it is the simplest correct option
- what should remain local
- what should become shared
- what should be URL or server state
