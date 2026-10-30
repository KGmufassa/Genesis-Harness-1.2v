# Stage Command And Skill Diagnostic Report

# Purpose

This report scans the Stage 1-8 command skills, stage-associated subskills, and supporting workflow references for underlying issues.

The goal is to identify:

* broken or risky skill structure
* command-to-subskill orchestration gaps
* readiness-control coverage
* registry drift
* naming and file-entrypoint inconsistencies
* critiques of the current Stage 1-8 workflow

---

# Diagnostic Scope

Scanned:

```text
.opencode/Skills/stage-1-product-initialization/skill.md
.opencode/Skills/stage-2-research-and-validation/skill.md
.opencode/Skills/stage-3-system-architecture/skill.md
.opencode/Skills/stage-4-ux-interaction-architecture/skill.md
.opencode/Skills/stage-5-development-orchestration/skill.md
.opencode/Skills/stage-6-implementation-validation/skill.md
.opencode/Skills/stage-7-launch-operationalization/skill.md
.opencode/Skills/stage-8-post-launch-evolution/skill.md
.opencode/Skills/global-stage-readiness-audit/skill.md
.opencode/Skills/*/skill.md
System-References/Docs/Stage-1-product-initialization-draft.md
System-References/Docs/Stage-2-architect.md
System-References/Docs/Stage-3-system-architecture-draft.md
System-References/Docs/Stage-4-ux-interaction-architecture-draft.md
System-References/Docs/Stage-5-development-orchestration-draft.md
System-References/Docs/Stage-6-implementation-validation-draft.md
System-References/Docs/Stage-7-launch-operationalization-draft.md
System-References/Docs/Stage-8-post-launch-evolution-draft.md
System-References/skill-regisry/skill-registry.json
```

---

# Executive Summary

Overall status:

```text
A-grade workflow with several repository hygiene and automation gaps.
```

The stage command skills are structurally sound. All eight stage command skills exist, each has an orchestration order, and all include the current readiness controls:

```text
schema_validation
reference_integrity
risk_acceptance_ledger
revision_loops
```

All expected Stage 1-8 subskill folders contain a `skill.md` entrypoint.

The main issues are not missing stage logic. They are:

* path casing drift around Stage 1
* nonstandard skill entrypoints in a few non-stage skills
* stale skill registry metadata
* Stage 7 and Stage 8 command skills are materially thinner than Stages 1-6
* readiness controls are documented but not backed by automated validators
* stage execution may become heavy without stricter profile-based depth enforcement

---

# High-Confidence Findings

## Finding 1 — Stage 1 Command Path Casing Is Inconsistent

Severity:

```text
Medium
```

Evidence:

```text
Tracked path:
.opencode/Skills/Stage-1-product-initialization/skill.md

Filesystem/usage path:
.opencode/Skills/stage-1-product-initialization/skill.md
```

Related references:

```text
System-References/skill-regisry/skill-registry.json
System-References/Docs/Stage-1-8-A-Grade-Improvement-Patch-Plan.md
Build-Plans/Build-status/Planning-state.json
Stage 1 review docs and command text
```

Risk:

On a case-insensitive filesystem, this may appear to work. On a case-sensitive filesystem or in CI, `Stage-1-product-initialization` and `stage-1-product-initialization` can behave as different paths.

Recommended fix:

Standardize the folder and command references to lowercase:

```text
.opencode/Skills/stage-1-product-initialization/
stage-1-product-initialization
```

Then update references in:

```text
System-References/skill-regisry/skill-registry.json
System-References/Docs/Stage-1-8-A-Grade-Improvement-Patch-Plan.md
Build-Plans/Build-status/Planning-state.json
Stage 1 review docs if command casing should change
```

---

## Finding 2 — Some Skill Folders Use Nonstandard Entrypoint Filenames

Severity:

```text
Medium
```

Evidence:

Nonstandard files:

```text
.opencode/Skills/backend-development/SKILL.md
.opencode/Skills/document-to-skill-package/SKILL.md
.opencode/Skills/using-git-worktrees/using-git-worktrees.md
```

The stage-associated skill folders are fine, but these non-stage skills may not be discovered by tooling that expects:

```text
skill.md
```

Risk:

Agent-task-builder or future skill scanners may skip these skills unless they support alternate entrypoint names.

Recommended fix:

Either:

* normalize each folder to include `skill.md`, or
* update the skill registry builder to explicitly support `SKILL.md` and documented alternate entrypoints.

Preferred approach:

```text
Add skill.md compatibility wrappers for nonstandard skills.
```

---

## Finding 3 — Skill Registry Metadata Is Stale Or Incomplete

Severity:

```text
High
```

Evidence:

Current registry states:

```json
{
  "skills_scanned": 76,
  "skills_included": 17,
  "stage_associated_skills_excluded": 59
}
```

Issue:

The registry includes an entry for:

```text
using-git-worktrees
```

but that folder does not contain `skill.md`; it contains:

```text
using-git-worktrees.md
```

Risk:

Agent-task-builder may select a skill that cannot be loaded through the expected `skill.md` convention.

Recommended fix:

Regenerate the skill registry after entrypoint normalization.

Also fix the typo in the folder path:

```text
System-References/skill-regisry/
```

Recommended canonical spelling:

```text
System-References/skill-registry/
```

---

## Finding 4 — Stage 7 And Stage 8 Command Skills Are Much Thinner Than Earlier Commands

Severity:

```text
Medium
```

Evidence:

The Stage 7 and Stage 8 command files exist and include orchestration plus readiness controls, but they are shorter and less operationally detailed than Stages 1-6.

Risk:

This is not a current blocker, but Stage 7 and Stage 8 may rely more heavily on their review docs and subskills than the command skill itself.

Implication:

When executing Stage 7 or Stage 8, an agent may need to infer more from the review docs unless the command skill is expanded.

Recommended fix:

Strengthen Stage 7 and Stage 8 command skills with:

* explicit preflight input validation
* shared state schema details
* subskill output merge rules
* artifact and risk-ledger update behavior
* completion-blocking examples
* readiness audit failure handling examples

---

## Finding 5 — Readiness Controls Are Specified But Not Fully Automated

Severity:

```text
Medium
```

Evidence:

Every stage command includes:

```text
schema_validation
reference_integrity
risk_acceptance_ledger
revision_loops
```

But there is no dedicated automated resolver or validator skill for:

```text
schema validation
cross-stage reference integrity
risk ledger ownership validation
revision-loop lifecycle validation
```

Risk:

The workflow can still be executed manually by agents, but quality depends on agent discipline rather than deterministic checks.

Recommended fix:

Create or extend these utility skills:

```text
schema-validation-runner
reference-integrity-audit
risk-acceptance-ledger-audit
revision-loop-manager
```

These could be called by `global-stage-readiness-audit`.

---

# Stage Command Coverage

## Stage 1

Command:

```text
.opencode/Skills/stage-1-product-initialization/skill.md
```

Status:

```text
Healthy with casing cleanup needed.
```

Observed orchestration:

```text
product-intelligence
workflow-and-capability-synthesis
dependency-and-risk-analysis
mvp-and-optimization
product-synthesis
global-stage-readiness-audit
```

Critique:

Stage 1 is strong and appropriately interactive. The biggest issue is repository-level path casing drift, not Stage 1 logic.

---

## Stage 2

Command:

```text
.opencode/Skills/stage-2-research-and-validation/skill.md
```

Status:

```text
Healthy.
```

Observed orchestration:

```text
assumption-analysis
market-and-competitive-validation
technical-and-operational-validation
business-and-scalability-validation
validation-synthesis
global-stage-readiness-audit
```

Critique:

Stage 2 is detailed and has the strongest evidence model. The next improvement is operational: make external evidence gathering and freshness validation executable instead of purely procedural.

---

## Stage 3

Command:

```text
.opencode/Skills/stage-3-system-architecture/skill.md
```

Status:

```text
Healthy.
```

Observed orchestration:

```text
system-topology-design
service-boundary-architecture
data-and-api-architecture
integration-and-infrastructure-architecture
security-and-scalability-architecture
architecture-synthesis
global-stage-readiness-audit
```

Critique:

Stage 3 cleanly separates architecture from implementation. It could benefit from stronger example outputs for reference integrity across service, entity, API, security, and scale IDs.

---

## Stage 4

Command:

```text
.opencode/Skills/stage-4-ux-interaction-architecture/skill.md
```

Status:

```text
Healthy and mature.
```

Observed orchestration:

```text
user-journey-design
interaction-architecture-design
screen-system-design
feature-behavior-specification
state-transition-and-accessibility-design
ui-blueprint-specification
design-system-foundation
ux-interaction-synthesis
global-stage-readiness-audit
```

Critique:

Stage 4 is powerful and frontend-ready. The risk is weight: UI blueprint, visual spec, design system, accessibility, responsive, and state planning can become too heavy for simple apps unless `stage_contract_profile` actively reduces required depth.

---

## Stage 5

Command:

```text
.opencode/Skills/stage-5-development-orchestration/skill.md
```

Status:

```text
Healthy and execution-ready.
```

Observed orchestration:

```text
development-roadmap-planning
implementation-sequence-planning
engineering-dependency-planning
testing-strategy-planning
build-ticket-generation
agent-assignment-planning
parallel-execution-planning
release-plan-orchestration
development-orchestration-synthesis
global-stage-readiness-audit
```

Critique:

Stage 5 is strong, but it is the most complex planning stage. It should enforce ticket profile templates so simple backend tickets do not inherit every frontend, visual, preview, and agent field unnecessarily.

---

## Stage 6

Command:

```text
.opencode/Skills/stage-6-implementation-validation/skill.md
```

Status:

```text
Healthy and controlled.
```

Observed orchestration:

```text
implementation-execution
validation-execution
regression-analysis
repair-workflow
system-health-synthesis
global-stage-readiness-audit
```

Critique:

Stage 6 has strong control rules. The main remaining gap is automation around artifact proof and validation command discovery. The command says what must happen, but it does not yet provide deterministic tooling for all checks.

---

## Stage 7

Command:

```text
.opencode/Skills/stage-7-launch-operationalization/skill.md
```

Status:

```text
Structurally healthy but thinner than Stages 1-6.
```

Observed orchestration:

```text
launch-readiness-validation
deployment-framework-planning
monitoring-systems-planning
analytics-framework-planning
operational-tooling-planning
launch-operationalization-synthesis
global-stage-readiness-audit
```

Critique:

Stage 7 now has deployment proof requirements, but the command skill should be expanded with more explicit state merge rules, artifact consumption rules, accepted launch risk behavior, and launch-blocker examples.

---

## Stage 8

Command:

```text
.opencode/Skills/stage-8-post-launch-evolution/skill.md
```

Status:

```text
Structurally healthy but thinner than Stages 1-6.
```

Observed orchestration:

```text
telemetry-analysis
operational-optimization
ai-improvement-planning
roadmap-evolution-planning
scalability-evolution-planning
post-launch-evolution-synthesis
global-stage-readiness-audit
```

Critique:

Stage 8 has the right feedback-routing model. It should define stronger lifecycle behavior for routed feedback, such as whether a finding opens a new stage cycle, a build ticket, a roadmap item, or a risk ledger entry.

---

# Subskill Coverage

All expected Stage 1-8 subskills have a `skill.md` entrypoint.

No missing stage-associated subskill entrypoints were found.

---

# Repository Hygiene Issues

## Nonstandard Skill Entrypoints

These folders should be normalized or explicitly supported by the registry builder:

```text
.opencode/Skills/backend-development/SKILL.md
.opencode/Skills/document-to-skill-package/SKILL.md
.opencode/Skills/using-git-worktrees/using-git-worktrees.md
```

## Skill Registry Folder Typo

Current path:

```text
System-References/skill-regisry/skill-registry.json
```

Recommended path:

```text
System-References/skill-registry/skill-registry.json
```

This is not breaking current references, but it is a source of long-term confusion.

## Stale Registry Metadata

The registry still references:

```text
using-git-worktrees
```

as a usable skill even though it does not contain standard `skill.md`.

Recommended fix:

Normalize entrypoints first, then regenerate:

```text
System-References/skill-registry/skill-registry.json
```

---

# Workflow Critique

## Strengths

* The eight-stage model has clear cognitive boundaries.
* Stage commands now include readiness controls consistently.
* Stage 4 through Stage 6 form a strong frontend-to-ticket-to-validation pipeline.
* Stage 5 is agent-aware and skill-aware.
* Stage 6 has mature terminal status, validation, regression, and repair logic.
* Stage 7 and Stage 8 now complete the lifecycle with launch proof and feedback routing.

## Weaknesses

* The workflow is documentation-rich but still light on executable validators.
* Stage 5 can become dense because tickets carry many possible fields.
* Stage 4 can become heavy for simple products if profile-depth rules are not enforced.
* Stage 7 and Stage 8 command skills are thinner than the earlier stage commands.
* Registry drift can weaken dynamic agent creation if not refreshed after skill changes.

## Core critique

The workflow is now strong enough to run a real app build, but its reliability still depends on agents following written rules. The next quality jump should come from automation around the rules:

```text
schema validation
reference integrity
artifact evidence matching
risk acceptance ownership
revision-loop lifecycle tracking
skill registry regeneration
```

---

# Recommended Fix Order

1. Normalize Stage 1 command casing to lowercase everywhere.
2. Add `skill.md` wrappers or registry support for nonstandard skill entrypoints.
3. Regenerate the skill registry and fix the `skill-regisry` folder typo.
4. Add executable schema validation and reference integrity utilities.
5. Expand Stage 7 and Stage 8 command skills to match the operational detail level of Stages 1-6.
6. Add ticket profile templates for Stage 5 to reduce ticket verbosity.
7. Add profile-depth enforcement examples for Stage 4 and Stage 5.

---

# Final Assessment

Current stage command and skill health:

```text
92 / 100
```

The stage commands and subskills are complete enough to operate, but the surrounding skill ecosystem needs cleanup before it is fully robust for dynamic agent selection and cross-environment execution.

The highest-priority technical risk is path and entrypoint consistency. The highest-priority workflow risk is relying on documented readiness controls without dedicated executable validators.
