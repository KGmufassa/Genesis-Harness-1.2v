# Responsive Implementation

Use this file when applying responsive behavior in code, not just deciding layout strategy.

## Mobile-First Rule

Design and implement mobile first, then expand.

```tsx
<div className="
  grid grid-cols-1
  sm:grid-cols-2
  lg:grid-cols-3
  gap-4
">
```

## Breakpoint Checks

At minimum, verify behavior at:
- 320px
- 768px
- 1024px
- 1440px

## Implementation Rules

- keep the minimum viable mobile workflow intact
- make priority order visible in the DOM and layout
- do not rely on desktop-only assumptions
- use overflow menus or drawers intentionally
- preserve interaction targets on small screens

## Verification Checklist

- [ ] works at 320px, 768px, 1024px, 1440px
- [ ] no critical overflow or clipping
- [ ] primary actions remain obvious
- [ ] dense content remains usable
- [ ] interactions stay accessible on touch devices

## Output Expectation

When using this reference, specify:
- implementation breakpoint behavior
- mobile-first layout choices
- responsive risks to test
