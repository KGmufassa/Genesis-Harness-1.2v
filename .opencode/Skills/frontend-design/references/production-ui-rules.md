# Production UI Rules

Use this file for implementation-quality guidance and to avoid low-grade generated UI.

## Core Standard

The UI should look like it was built by a design-aware engineer at a strong product company, not assembled from generic generated patterns.

## Avoid The AI Aesthetic

| AI Default | Why It Fails | Better Direction |
|---|---|---|
| Purple/indigo everything | safe but generic | use the actual product palette |
| Excessive gradients | decorative noise | flat or restrained gradients only when justified |
| Rounded everything | ignores real radius hierarchy | use a consistent radius system |
| Generic hero sections | template-driven, weak content fit | content-first layout |
| Placeholder copy everywhere | hides real layout stress | realistic placeholder content |
| Oversized padding everywhere | destroys hierarchy | use a real spacing scale |
| Stock card grids | ignores information priority | purpose-driven layout |
| Shadow-heavy design | competes with content | use subtle elevation only when needed |

## Spacing And Layout

Use a consistent spacing scale. Do not invent values.

```css
padding: 1rem;
gap: 0.75rem;
```

Avoid arbitrary values that are not on the system scale.

## Typography

Respect hierarchy:

```text
h1 → page title
h2 → section title
h3 → subsection title
body → default text
small → helper text
```

Do not skip heading levels or use heading styling for non-heading content.

## Color

- use semantic tokens, not raw hex values
- maintain sufficient contrast
- do not rely only on color to communicate state

## Red Flags

- components over 200 lines without a good reason
- inline styles or arbitrary pixel values
- missing loading, error, or empty states
- no keyboard testing
- color as the sole state indicator
- generic “AI look”

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| Accessibility is a nice-to-have | It is a quality and often legal requirement |
| We’ll make it responsive later | Retrofitting responsiveness is much harder |
| It’s just a prototype | Prototypes often become production code |
| The AI aesthetic is fine for now | It signals low quality immediately |

## Output Expectation

When using this reference, specify:
- which production-quality risks are present
- which AI-aesthetic defaults to remove
- what to change in spacing, type, hierarchy, and states
