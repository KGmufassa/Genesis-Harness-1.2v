# Design Tokens

Use this file when defining or correcting the frontend visual system.

## Required Token Categories

- color tokens
- typography tokens
- spacing tokens
- radius tokens
- elevation tokens if used
- motion tokens if motion matters

## Color Rules

- define semantic roles, not random decorative swatches
- separate background, surface, text, accent, and status colors
- use CSS variables or equivalent tokens
- avoid repeated hardcoded values

Use role-based color selection where possible:
- neutral for default text and secondary UI
- brand for primary actions
- information for in-progress or informational UI
- success, warning, and danger for semantic status
- inverse tokens on bold backgrounds

Source note:
- Atlassian structures color tokens by property, role, emphasis, and interaction state.

## Typography Rules

- define a display voice and body voice
- maintain clear hierarchy from headline to caption
- match typography to product character
- avoid default stacks unless constrained

## Spacing Rules

- use a predictable spacing scale
- avoid arbitrary spacing values
- keep rhythm consistent across sections and components

Use a base-unit scale rather than pixel guessing.

Source note:
- Atlassian spacing guidance uses an 8px base unit with structured spacing tokens.

## Radius And Elevation

- define the geometry character of the interface
- keep radius aligned with visual tone
- use elevation intentionally

## Output Expectation

At minimum, the final UI should expose:
- token definitions
- type hierarchy
- spacing scale
- component-level token consistency
- semantic action and state color roles
