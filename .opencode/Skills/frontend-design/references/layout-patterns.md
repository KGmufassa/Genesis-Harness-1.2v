# Layout Patterns

Use this file to choose a concrete shell or page-level pattern after the surface type is known.

## Selection Rule

Choose the simplest pattern that supports the task without hiding essential context.

## Narrative Landing

Best for:
- launches
- consumer landing pages
- brand-forward marketing pages

Use when:
- sequencing and persuasion matter more than dense operation

Strengths:
- strong pacing
- memorable sections
- flexible visual storytelling

Breaks down when:
- the page needs heavy ongoing interaction or repeated dense tasks

## Dashboard Shell

Best for:
- operational SaaS
- analytics
- admin summaries

Use when:
- the user needs orientation first, then action

Strengths:
- predictable sections
- fast scanning
- repeatable widgets and panels

Breaks down when:
- the work requires deep object editing or many simultaneous supporting panels

## List-Detail

Best for:
- messaging
- file browsers
- contact managers
- any collection where item detail is the main secondary context

Use when:
- users choose from a list, then inspect or act on one item

Strengths:
- strong selection flow
- easy large-screen adaptation
- supports compact-to-expanded progression well

Breaks down when:
- there is no meaningful detail pane or the list is not the dominant organizer

Source note:
- Android canonical layouts identifies list-detail as a common pattern for messaging, contact managers, and file browsers.

## Split-Pane Workspace

Best for:
- editors
- tools
- multi-step operations
- inspector-driven applications

Use when:
- users must keep context visible while acting in another pane

Strengths:
- persistent context
- supports creation and inspection together
- good for expert workflows

Breaks down when:
- the app has little contextual dependency between panes

## Settings Hierarchy

Best for:
- account settings
- app configuration
- setup-heavy SaaS

Use when:
- preferences need grouping across categories or screens

Strengths:
- predictable navigation
- progressive disclosure
- low-friction scanning

Breaks down when:
- frequent actions are misplaced into settings instead of staying contextual

Source note:
- Android settings guidance recommends grouping settings meaningfully and leaving frequent actions in the context where they matter.

## Dense Data Workspace

Best for:
- tables with filters
- operations consoles
- audit/review queues

Use when:
- users need to compare rows, scan status, and act repeatedly

Strengths:
- efficient repeated action handling
- supports toolbars, filters, sorting, and pagination

Breaks down when:
- the interface is mostly narrative or driven by one primary action

## Output Expectation

When using a layout pattern, specify:
- chosen pattern
- why it fits the surface
- main zones
- navigation model
- primary and secondary action placement
- likely breakpoint adaptation
