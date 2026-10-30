# Project State Synthesis Instructions

You are maintaining `Memory/project-state.md` from distilled conversation reports.

## Source Material

There are {source_count} distilled reports. Treat the following material as evidence:

{distilled_context}

## Rules

- Reconcile reports chronologically; newer explicit decisions supersede older state.
- Distinguish current state from historical changes.
- Do not infer facts that are not supported by the reports.
- Preserve uncertainty in `Unresolved Questions`.
- Keep the output concise and operationally useful for a new agent.
- Retain source filenames when a conclusion depends on a specific report.
- Label each conclusion with confidence: `[high]`, `[medium]`, or `[low]`.
- Include an `Active Risks` section for repeated failures or unresolved operational threats.

## Required Output

Write `Memory/project-state.md` using the project-state template with these sections:

- Current Architecture
- Current Stack
- Active Features
- Deprecated Features
- Current Priorities
- Known Constraints
- Active Risks
- Unresolved Questions
- Next Recommended Steps
