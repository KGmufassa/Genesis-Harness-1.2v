# Responsive Behavior

Use this file when the UI must adapt across mobile, tablet, and desktop.

## Core Rules

- decide what collapses first
- decide what remains persistent
- move lower-priority actions into menus or drawers
- preserve the minimum viable workflow on smaller screens

Default to adaptive design rather than assuming one mobile layout stretched everywhere.

Source note:
- Android recommends adaptive design as the default and suggests determining layout changes by width class first, then adjusting for height.

## Mobile Rules

- keep the primary action obvious
- reduce simultaneous visible complexity
- stack content in priority order
- avoid tiny hit targets

## Tablet Rules

- preserve context better than mobile
- avoid awkward shrunk-desktop layouts

## Desktop Rules

- use width for orientation and parallel context
- keep persistent panels only when they materially help
- do not add density without structure

## Responsive Techniques

Use these intentionally:
- reflow content to fit larger widths
- show or hide secondary metadata based on screen size
- re-architect the layout when preserving focus matters more than preserving structure
- resize regions and margins to improve balance and reduce unnecessary scrolling

## Output Expectation

The final UI should make clear:
- what changes by breakpoint
- what stays pinned
- which actions move into overflow
- which surfaces need separate composition
