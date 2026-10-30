# Stage 2 Command Skill Build Task List

# Objective

Build the `stage-2-research-and-validation` command skill for Stage 2 so it can orchestrate validation skills, maintain shared validation state, produce evidence-backed outputs, and determine whether a product is ready for Stage 3 architecture.

---

# Completion Definition

The Stage 2 command skill is complete when it can:

* load Stage 1 outputs
* extract and prioritize product assumptions
* coordinate all Stage 2 validation skills
* maintain a centralized assumption registry
* update confidence scores across validation domains
* detect contradictions and critical unknowns
* generate the six Stage 2 final output files
* determine whether architecture progression is safe

---

# Task List

## 1. Define Command Skill Folder

- [x] Create `Skills/stage-2-research-and-validation/`
- [x] Create `Skills/stage-2-research-and-validation/skill.md`
- [x] Define the command purpose, trigger conditions, inputs, outputs, and orchestration responsibilities
- [x] Make clear that this is the Stage 2 command skill, not a single validation subskill

## 2. Define Stage 2 Input Contract

- [x] Specify required Stage 1 inputs:
  - [x] `01-product-foundation.json`
  - [x] `02-user-system-map.json`
  - [x] `03-workflow-architecture.json`
  - [x] `04-product-capabilities.json`
  - [x] `05-feature-structure.json`
  - [x] `06-product-boundaries.json`
  - [x] `07-dependency-map.json`
  - [x] `08-mvp-operational-model.json`
  - [x] `09-risk-and-constraints.json`
  - [x] `10-success-framework.json`
- [x] Define behavior when some Stage 1 files are missing
- [x] Define minimum viable input set for Stage 2 to proceed
- [x] Add a preflight validation step before assumption extraction

## 3. Define Shared Validation State

- [x] Create the canonical shared state schema
- [x] Include these required top-level fields:
  - [x] `assumptions`
  - [x] `validation_targets`
  - [x] `assumption_registry`
  - [x] `confidence_scores`
  - [x] `market_validation`
  - [x] `competitive_landscape`
  - [x] `user_validation`
  - [x] `technical_validation`
  - [x] `operational_validation`
  - [x] `business_validation`
  - [x] `scalability_analysis`
  - [x] `critical_unknowns`
  - [x] `contradictions`
  - [x] `risk_registry`
  - [x] `recommendations`
  - [x] `architecture_readiness`
  - [x] `completion_status`
- [x] Define how each subskill reads and updates shared state
- [x] Define confidence score merge behavior

## 4. Define Assumption Registry Contract

- [x] Require every assumption to include:
  - [x] `id`
  - [x] `assumption`
  - [x] `domain`
  - [x] `source_stage_1_file`
  - [x] `explicit_or_implicit`
  - [x] `risk_if_false`
  - [x] `architecture_critical`
  - [x] `status`
  - [x] `confidence`
  - [x] `evidence`
  - [x] `evidence_quality`
  - [x] `contradictions`
  - [x] `next_action`
- [x] Define allowed statuses:
  - [x] `unvalidated`
  - [x] `validated`
  - [x] `weakened`
  - [x] `contradicted`
  - [x] `unknown`
- [x] Define allowed evidence quality values:
  - [x] `none`
  - [x] `low`
  - [x] `medium`
  - [x] `high`

## 5. Define Orchestration Sequence

- [x] Add the required execution order:
  - [x] load Stage 1 outputs
  - [x] initialize shared validation state
  - [x] run `assumption-analysis`
  - [x] prioritize validation targets
  - [x] run `market-and-competitive-validation`
  - [x] run `technical-and-operational-validation`
  - [x] run `business-and-scalability-validation`
  - [x] run `validation-synthesis`
  - [x] produce final Stage 2 outputs
  - [x] determine completion status
- [x] Define when a validation skill may be skipped
- [x] Define when the command must stop and report blockers

## 6. Define Subskill Output Contract

- [x] Require every validation subskill to return:
  - [x] `validated_assumptions`
  - [x] `weakened_assumptions`
  - [x] `contradicted_assumptions`
  - [x] `unknown_assumptions`
  - [x] `critical_unknowns`
  - [x] `contradictions`
  - [x] `confidence_delta`
  - [x] `evidence`
  - [x] `evidence_quality`
  - [x] `risks`
  - [x] `recommendation`
- [x] Define allowed recommendations:
  - [x] `continue`
  - [x] `revise`
  - [x] `block`
- [x] Require every subskill to update the assumption registry instead of producing isolated findings

## 7. Build `assumption-analysis` Skill

- [x] Create `Skills/assumption-analysis/skill.md`
- [x] Extract explicit assumptions from Stage 1 outputs
- [x] Infer implicit assumptions from workflows, capabilities, dependencies, MVP scope, and success criteria
- [x] Classify assumptions by domain:
  - [x] user
  - [x] market
  - [x] technical
  - [x] business
  - [x] operational
  - [x] scalability
  - [x] compliance
- [x] Mark architecture-critical assumptions
- [x] Prioritize validation targets by risk and uncertainty
- [x] Populate the initial assumption registry

## 8. Build `market-and-competitive-validation` Skill

- [x] Create `Skills/market-and-competitive-validation/skill.md`
- [x] Validate demand strength
- [x] Validate target audience viability
- [x] Analyze direct and indirect competitors
- [x] Identify saturation risk
- [x] Validate user pain and workflow realism
- [x] Assess adoption and habit-change difficulty
- [x] Identify positioning opportunities
- [x] Update market confidence and competitive landscape state

## 9. Build `technical-and-operational-validation` Skill

- [x] Create `Skills/technical-and-operational-validation/skill.md`
- [x] Validate implementation realism
- [x] Validate AI capability assumptions
- [x] Validate integration feasibility
- [x] Validate infrastructure complexity
- [x] Detect scalability bottlenecks
- [x] Detect operational support burden
- [x] Identify fragile dependencies
- [x] Update technical, operational, and scalability risk state

## 10. Build `business-and-scalability-validation` Skill

- [x] Create `Skills/business-and-scalability-validation/skill.md`
- [x] Validate monetization assumptions
- [x] Assess pricing realism
- [x] Validate customer acquisition assumptions
- [x] Analyze retention feasibility
- [x] Analyze AI and infrastructure cost sustainability
- [x] Identify growth bottlenecks
- [x] Update business validation and scalability analysis state

## 11. Build `validation-synthesis` Skill

- [x] Create `Skills/validation-synthesis/skill.md`
- [x] Combine all validation results
- [x] Normalize confidence scores
- [x] Detect unresolved contradictions
- [x] Identify remaining critical unknowns
- [x] Generate architecture readiness assessment
- [x] Generate strategic recommendations
- [x] Determine completion status
- [x] Produce progression guidance for Stage 3

## 12. Define Confidence Scoring Rules

- [x] Define domain confidence scale from `0.0` to `1.0`
- [x] Define default starting confidence for unvalidated assumptions
- [x] Define how evidence quality affects confidence
- [x] Define how contradictions reduce confidence
- [x] Define how unknown architecture-critical assumptions affect readiness
- [x] Add minimum readiness thresholds:
  - [x] market confidence minimum: `0.70`
  - [x] technical confidence minimum: `0.75`
  - [x] business confidence minimum: `0.65`
  - [x] operational confidence minimum: `0.70`
  - [x] architecture readiness minimum: `0.75`

## 13. Define Completion Gate

- [x] Stage 2 may complete only when:
  - [x] no critical assumptions remain `unknown`
  - [x] no architecture-critical assumptions are below threshold
  - [x] no unresolved contradictions remain
  - [x] all high-risk assumptions have mitigation paths
  - [x] architecture readiness status is `ready`
- [x] Define possible completion statuses:
  - [x] `ready_for_stage_3`
  - [x] `needs_more_validation`
  - [x] `requires_product_revision`
  - [x] `blocked`

## 14. Define Final Output Files

- [x] Generate `01-market-analysis.json`
- [x] Generate `02-competitive-landscape.json`
- [x] Generate `03-technical-feasibility.json`
- [x] Generate `04-business-viability.json`
- [x] Generate `05-risk-validation.json`
- [x] Generate `06-strategic-positioning.json`
- [x] Ensure every output references relevant assumption IDs
- [x] Ensure every output includes confidence and evidence metadata

## 15. Add Evidence Rules

- [x] Require findings to distinguish evidence from inference
- [x] Require unsupported claims to be marked as assumptions
- [x] Require external validation needs to be listed when browsing or market research is unavailable
- [x] Require source links when external research is used
- [x] Require low-evidence recommendations to be marked as provisional

## 16. Add Contradiction Handling

- [x] Define contradiction structure:
  - [x] `id`
  - [x] `assumption_ids`
  - [x] `description`
  - [x] `severity`
  - [x] `impact`
  - [x] `resolution_path`
  - [x] `status`
- [x] Define contradiction statuses:
  - [x] `open`
  - [x] `mitigated`
  - [x] `resolved`
- [x] Block Stage 3 progression when critical contradictions remain open

## 17. Add Risk Registry Rules

- [x] Define risk fields:
  - [x] `id`
  - [x] `risk`
  - [x] `domain`
  - [x] `severity`
  - [x] `likelihood`
  - [x] `affected_assumptions`
  - [x] `mitigation`
  - [x] `owner_stage`
- [x] Require high and critical risks to include mitigation paths
- [x] Carry unresolved architecture risks into Stage 3 guidance

## 18. Add Command Examples

- [x] Add example command input
- [x] Add example shared validation state
- [x] Add example assumption registry entry
- [x] Add example blocked completion result
- [x] Add example ready-for-architecture result

## 19. Add Validation Checklist

- [x] Confirm all Stage 1 assumptions were reviewed
- [x] Confirm every high-risk assumption was assigned a validation status
- [x] Confirm every confidence score has a rationale
- [x] Confirm every critical unknown has a next action
- [x] Confirm every final output file references assumption IDs
- [x] Confirm completion status follows the gate rules

## 20. Review Against Stage Architecture

- [x] Confirm Stage 2 does not perform Stage 1 product structuring
- [x] Confirm Stage 2 does not perform Stage 3 system design
- [x] Confirm Stage 2 only validates architecture readiness
- [x] Confirm the command preserves the cognition boundary:

```text
Stage 2 asks: "Do the assumptions behind this product survive reality?"
```

---

# Recommended Build Order

1. Build `stage-2-research-and-validation`
2. Build `assumption-analysis`
3. Build shared state and assumption registry contracts
4. Build the three validation domain skills
5. Build `validation-synthesis`
6. Add confidence scoring and completion gates
7. Add examples and validation checklist
8. Test against one complete Stage 1 product model and one incomplete model

