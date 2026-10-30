# Jev Workflow Integration Plan

## Document Status

| Field | Value |
| --- | --- |
| Status | Proposed implementation plan |
| Scope | Additive Jev decision support for the Genesis harness |
| Primary pilot | Scoped-change intake and stage routing |
| Workflow authority | Existing Genesis contracts, deterministic checks, and human approvals |
| Credential source | External secrets manager accessed through runtime identity |
| Last researched | 2026-10-29 |

This document is a plan only. It does not change any current stage command,
schema, readiness rule, approval boundary, router result, or build-state file.

---

## Executive Summary

Jev is a bounded decision model. It receives a `state`, evaluates one or more
typed questions, and returns structured `Choice`, `Score`, or `Noul` answers.
It does not generate plans, explanations, source code, or stage artifacts.

That behavior makes Jev a good fit for the small, repeated judgments inside
Genesis, including:

- routing a scoped change to the earliest affected stage
- identifying ambiguous or cross-cutting change requests
- suggesting failure and revision ownership
- scoring evidence, operational urgency, or review priority
- selecting from an approved set of agents, skills, or validation paths

The recommended first implementation is a read-only, advisory integration with
`change-intake-router`. The existing keyword router remains authoritative. Jev
runs beside it, and its result is used to measure decision quality, expose
uncertainty, and focus human review. It cannot create a `CHANGE-` record,
approve a stage, accept risk, mark readiness, or execute a tool.

The integration should progress through three operating modes:

```text
shadow -> advisory -> narrowly approved automation
```

Only the first two modes are part of the recommended implementation. Automated
workflow authority requires a separate policy decision after evaluation and is
outside this plan's initial rollout.

The TypeSafe API key will be stored in a secrets manager. A workload identity
will retrieve it at runtime and pass it directly to the Jev client in memory.
The key must never be committed, written to `Build-Plans/`, included in a model
state, placed in an artifact, or emitted in logs.

---

## Goals

- Improve the consistency of bounded routing and classification decisions.
- Surface uncertainty before a change enters the wrong stage.
- Reduce the need to use a large reasoning model for routine classification.
- Produce structured, reviewable decision signals with probabilities and
  confidence.
- Preserve every existing workflow contract and approval boundary.
- Continue operating when Jev or the secrets manager is unavailable.
- Keep the Jev provider and secrets-manager provider replaceable.
- Create enough evaluation evidence to decide whether future automation is
  safe.

## Non-Goals

- Replacing Stage 1–8 orchestrators or their subskills.
- Generating product plans, research, architecture, UX, tickets, code, or
  launch plans.
- Replacing JSON Schema validation or the global readiness audit.
- Giving Jev authority to approve decision briefs or changes.
- Allowing Jev to accept high or critical risks.
- Allowing Jev to authorize tools, deployments, merges, or destructive work.
- Sending entire stage directories or unrestricted repository content to an
  external model.
- Selecting a specific secrets-manager vendor in the core integration.
- Fine-tuning Jev or treating confidence as proof that an answer is correct.

---

## Current Workflow Baseline

The existing workflow remains the source of truth:

```text
Stage 1 -> Stage 2 -> Stage 3 -> Stage 4
     -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8
```

The relevant existing controls are:

- `change-intake-router` previews a requested change, selects the earliest
  affected stage, and creates a compact record only after approval.
- `global-stage-readiness-audit` validates files, schemas, references,
  handoffs, evidence, risk acceptance, and revision ownership.
- Stages 1–4 cannot advance without the required decision-brief approval.
- High and critical risk acceptance requires the existing approval and ledger
  rules.
- Stable IDs and affected-ID locks prevent silent replacement and concurrent
  change conflicts.
- A failed readiness check creates a revision loop owned by the stage capable
  of resolving the issue.

The current change router uses deterministic phrase matching. It is predictable
and inexpensive, but it can miss synonyms, indirect descriptions, requests
that span several domains, and cases where the earliest affected stage is not
named explicitly. Jev should initially measure and explain these gaps through
structured signals without replacing the deterministic result.

---

## Design Principles

### Advisory before authoritative

- Start in shadow mode.
- Show Jev output only after the deterministic route has been calculated.
- Never silently substitute the Jev route for the existing route.
- Require an explicit future policy change before Jev can control a workflow
  branch.

### Policy remains deterministic

- Code owns thresholds, permissions, allowed choices, and fallbacks.
- The model supplies a judgment; it does not supply authority.
- Existing schemas, audits, ledgers, and approval records remain authoritative.

### Use bounded answer spaces

- Every `Choice` option must map to a valid Genesis value.
- Every `Score` rubric must define ordered levels in plain language.
- Every `Noul` question must contain one testable proposition.
- Include an `unclear_or_cross_cutting` choice when a single stage may not be a
  complete answer.

### Minimize shared state

- Send only the information needed for the question.
- Prefer IDs and compact summaries over complete files.
- Apply allowlist construction and redaction before the request leaves the
  process.
- Do not send credentials, source code, private keys, customer records, or
  unrelated conversation history.

### Fail safely

- An unavailable advisory model must not block the normal workflow.
- An invalid response is treated as no advisory result.
- A sensitive request that cannot be safely minimized is not sent.
- A low-confidence result is routed to review, not guessed.

### Preserve reproducibility

- Pin an evaluated Jev model version in non-experimental operation.
- Record the returned model version and question-contract version.
- Re-run the evaluation suite before changing model versions, questions,
  criteria, or thresholds.

---

## Proposed Architecture

```text
User change request
        |
        v
Existing deterministic router ------------------------------+
        |                                                    |
        | authoritative route                                |
        v                                                    |
Existing preview and approval flow                           |
                                                             |
Sanitized advisory state                                     |
        |                                                    |
        v                                                    |
Jev decision-support adapter                                 |
        |                                                    |
        +--> secrets boundary --> secrets manager            |
        |         runtime identity retrieves API key         |
        |                                                    |
        +--> TypeSafe System One API                         |
        |                                                    |
        v                                                    |
Typed answer + probabilities + confidence                    |
        |                                                    |
        v                                                    |
Local threshold and policy evaluator                         |
        |                                                    |
        +--> agree: annotate preview                          |
        +--> disagree/uncertain: request review               |
        +--> unavailable: continue without advisory result ---+
```

### Component boundaries

| Component | Responsibility | Must not do |
| --- | --- | --- |
| State builder | Construct the minimum allowed Jev state | Read or transmit unrestricted repository content |
| Redactor | Remove or reject sensitive values | Claim that arbitrary text is safe without checks |
| Secret resolver | Retrieve the API key through runtime identity | Persist, print, hash, or return the key in diagnostics |
| Jev client | Send typed questions and validate typed responses | Decide workflow policy |
| Policy evaluator | Apply locally configured thresholds and escalation rules | Treat confidence as approval |
| Evidence recorder | Record non-secret metadata and evaluation outcomes | Store raw secrets or unnecessary input text |
| Existing router | Produce the authoritative route | Depend on Jev availability during the pilot |

### Proposed additive package

Implementation should add a general-purpose skill package without editing the
Stage 1–8 skills:

```text
.opencode/Skills/jev-decision-support/
  skill.md
  references/
    decision-contract.md
    data-handling.md
    operations.md
  scripts/
    jev_client.py
    jev_policy.py
    evaluate_change_routes.py
  tests/
    fixtures/
    test_jev_client.py
    test_jev_policy.py
    test_evaluate_change_routes.py
```

The skill should be callable independently. During shadow mode, the existing
router is not edited; the evaluation runner calls both implementations and
compares their results. Advisory integration into the router should occur only
after the shadow acceptance gate passes.

### Dependency approach

The core implementation should begin with Python 3.10 standard-library HTTP
support because the repository currently favors dependency-free utilities.
Use a small transport interface so the official `typesafe-sdk` can be adopted
later without changing decision or policy code.

The HTTP transport should call:

```text
POST https://api.typesafe.ai/v1/systemone
```

The transport must support:

- HTTPS only
- bearer authentication
- explicit connection and total timeouts
- JSON request and response validation
- provider request IDs in diagnostics
- bounded retries with jitter for retryable responses
- no retries for invalid authentication or invalid requests
- dependency injection of a fake transport for tests

---

## Secrets-Manager Design

### Required security properties

- The TypeSafe API key is created and stored in the selected secrets manager.
- Developers, agents, CI jobs, and runtime processes use workload identity or
  an equivalent short-lived identity to retrieve it.
- The runtime identity receives read access only to the Jev credential needed
  for its environment.
- Production, staging, CI, and local development use separate secret entries
  and, where supported, separate TypeSafe keys.
- The plaintext key exists only in process memory for the shortest practical
  time.
- The key is never placed in `.env`, shell history, command arguments, Git,
  build artifacts, test fixtures, screenshots, or logs.
- Secret values are excluded from exceptions and structured diagnostics.

### Provider-neutral secret contract

The core Jev adapter should depend on a minimal protocol rather than a
vendor-specific SDK:

```python
from typing import Protocol


class SecretResolver(Protocol):
    def resolve(self, logical_name: str) -> str:
        """Return a secret value in memory or raise SecretResolutionError."""
```

Recommended logical names:

```text
genesis/jev/development/api-key
genesis/jev/ci/api-key
genesis/jev/staging/api-key
genesis/jev/production/api-key
```

The provider mapping belongs to deployment or operator configuration, not to
stage outputs. If the chosen secrets manager injects an environment variable
directly, the process may read `TYPESAFE_API_KEY` once at startup. If it offers
an API or sidecar, a provider-specific resolver may supply the value directly
to the client constructor.

Direct in-memory injection is preferred over a long-lived environment variable
when both options are available. Environment injection remains supported for
compatibility with the official SDK.

### Authentication flow

```text
Jev process starts
    -> obtains workload identity
    -> requests the environment-specific secret
    -> receives the key in memory
    -> creates the Jev client
    -> sends the key only in the HTTPS Authorization header
    -> clears client references when the process ends
```

### Rotation flow

- Rotate the key in the TypeSafe console and secrets manager according to the
  organization's normal rotation policy.
- Prefer overlapping validity during rollout when the provider permits it.
- Start new processes with the new secret version.
- If a request receives an authentication failure, invalidate the cached value,
  resolve the secret once more, and retry authentication once.
- Do not loop on authentication failures.
- Record only the secret version identifier supplied by the secrets manager,
  never the value or a derived fingerprint.
- Revoke the old key after new processes have demonstrated successful calls.

### Secrets-manager outage behavior

Because Jev is advisory in the initial rollout:

```text
secret available   -> run advisory request
secret unavailable -> record `advisory_unavailable` and use existing workflow
```

A secrets-manager outage must not change the deterministic route, block a
stage, prevent an audit, or create a revision loop. Alerting may report the
integration degradation without exposing the logical secret value if that
name is considered sensitive by the operator.

### Local development and testing

- Use a development-only secret entry and a developer workload identity.
- Do not create a committed `.env` file.
- Unit tests use a fake resolver returning a synthetic value and a fake HTTP
  transport; they never call the secrets manager or TypeSafe.
- Optional integration tests run only when an explicit flag is present and the
  runtime identity can access the CI-specific secret.
- CI should prefer OIDC or an equivalent federated identity over stored static
  credentials.

---

## Data Handling and Privacy

### Allowed pilot state

The Stage-routing pilot may send only:

```json
{
  "requested_outcome": "A concise change request supplied by the user",
  "current_stage": "stage_3",
  "current_stage_status": "ready_for_stage_4",
  "affected_id_prefixes": ["API-", "SCREEN-"],
  "explicit_domains": ["authentication", "accessibility"]
}
```

Use ID prefixes unless exact IDs are required for a measured use case. Do not
send full stage artifacts to improve a routing answer.

### Prohibited state

- API keys, tokens, passwords, certificates, or secret-manager responses
- private customer or employee data not required for routing
- raw production telemetry containing personal data
- full source files or repository archives
- unredacted incident payloads
- complete conversation histories
- approval identities when a role or boolean is sufficient

### Sanitization sequence

1. Build state from an allowlist of fields.
1. Normalize length and reject unexpectedly large inputs.
1. Detect common credential patterns and sensitive field names.
1. Redact incidental personal data when it is not necessary for the decision.
1. Reject the external call if safe minimization is uncertain.
1. Log only the sanitization outcome, not the removed values.

### Retention

- Do not log the raw request body or raw response body by default.
- Retain the question-contract version, model version, request ID, typed
  answers, probabilities, confidence, policy outcome, latency, and error class.
- Store a one-way digest of the sanitized state only if deduplication is
  required and approved by project policy.
- Apply the organization's retention and deletion policy to evaluation
  artifacts.
- Confirm the provider's data-processing and retention terms before production
  use, especially when project data may be confidential.

---

## Pilot Decision Contract

### State-routing question

The first `Choice` question should select the earliest stage whose owned
decision must change:

```json
{
  "owning_stage": {
    "type": "choice",
    "instructions": "Select the earliest Genesis stage whose approved output must change to satisfy the requested outcome. Select unclear_or_cross_cutting when the state is insufficient or no single earliest stage can be selected safely.",
    "criteria": {
      "stage_1": "Product identity, users, roles, workflows, capabilities, permissions, boundaries, or MVP scope",
      "stage_2": "Invalid, contradicted, or unsupported product, market, user, business, technical, operational, or scalability assumptions",
      "stage_3": "System topology, services, data, APIs, integrations, security, infrastructure, authentication, migrations, or scalability",
      "stage_4": "Journeys, screens, behavior, state, accessibility, navigation, UI architecture, visual specifications, or design systems",
      "stage_5": "Development sequence, tickets, agent assignments, testing strategy, dependencies, parallel execution, or release planning",
      "stage_6": "Implementation, validation, regression, repair, runtime behavior, responsive validation, or visual QA",
      "stage_7": "Deployment, monitoring, analytics, support, rollback, operational tooling, or launch readiness",
      "stage_8": "Live telemetry, optimization, roadmap evolution, AI improvement, operational learning, or scale evolution",
      "unclear_or_cross_cutting": "The request lacks enough context or spans ownership boundaries in a way that needs review"
    }
  }
}
```

### Parallel pilot questions

Evaluate independent questions in the same request:

```json
{
  "is_material": {
    "type": "noul",
    "instructions": "The requested outcome materially changes approved product, architecture, UX, security, migration, or release direction"
  },
  "requires_human_review": {
    "type": "noul",
    "instructions": "The request is ambiguous, cross-cutting, high-impact, sensitive, or unsafe to route without human review"
  },
  "impact_level": {
    "type": "score",
    "instructions": "Score the likely workflow impact of this request",
    "criteria": [
      "Local and reversible",
      "Bounded to one workflow domain",
      "System-wide or cross-cutting",
      "Critical security, privacy, data-loss, or operational impact"
    ]
  }
}
```

Question IDs are local response keys. Every instruction must be complete
because the identifier itself should not be assumed to provide semantic
context to the model.

### Contract versioning

Use an explicit version such as:

```text
genesis-change-routing/1.0.0
```

Increment:

- patch when wording changes without changing meanings or choices
- minor when optional questions or compatible metadata are added
- major when choices, rubrics, or policy semantics change

Every evaluation and advisory record must include this version.

---

## Local Policy and Thresholds

### Shadow mode

- Jev never affects the route.
- Record whether the Jev answer agrees with the deterministic route and the
  human-reviewed gold route.
- Record uncertainty and disagreement categories.
- Do not expose raw probabilities as proof of correctness.

### Advisory mode

Use conservative initial policy:

- `Choice` is high confidence only when confidence is at least `0.90` and the
  selected option probability is at least `0.90`.
- `Noul` values from `0.30` through `0.70` are treated as uncertain.
- `requires_human_review >= 0.70` always recommends review.
- `unclear_or_cross_cutting` always recommends review.
- A disagreement with the deterministic route recommends review.
- Security, privacy, authentication, payment, destructive migration, data
  loss, or emergency keywords always recommend review regardless of confidence.
- No threshold bypasses an existing approval.

These are safe starting values, not permanent truth. Adjust them only from a
versioned evaluation report using representative Genesis cases.

### Future automation gate

Narrow automation may be proposed later only when all of the following are
true:

- the user approves a separate workflow-policy change
- the target decision is low impact and reversible
- the choice set is complete and versioned
- the evaluated model version is pinned
- the confidence threshold is calibrated on representative data
- the deterministic fallback remains available
- the action does not approve, accept risk, deploy, merge, or modify stable IDs
- production monitoring and a kill switch are active

Until then, Jev output remains advisory.

---

## Evidence and Observability

### Decision record

Use a supplemental record shaped like the following. It is evidence, not a new
workflow contract:

```json
{
  "decision_id": "JEV-DECISION-0001",
  "mode": "shadow",
  "use_case": "change_stage_routing",
  "question_contract_version": "genesis-change-routing/1.0.0",
  "model_requested": "jev-1.14.0",
  "model_returned": "jev-1.14.0",
  "provider_request_id": "",
  "answers": {
    "owning_stage": {
      "choice": "stage_3",
      "probabilities": {},
      "confidence": 0.0
    }
  },
  "policy_result": "agree | review | unavailable | invalid",
  "deterministic_route": "stage_3",
  "human_gold_route": "",
  "latency_ms": 0,
  "secret_version_id": "",
  "state_retained": false,
  "created_at": ""
}
```

Do not add `JEV-DECISION-` to the global stable-ID standard during the pilot.
Treat it as an integration-local identifier until the evaluation demonstrates
a durable need.

### Artifact registry use

When a decision record must be retained for an approved `CHANGE-` record:

- write it under that change's evidence directory
- register it as the existing `validation_report` artifact type
- reference its `ARTIFACT-` ID from the change record when useful
- keep it supplemental rather than required for readiness
- omit raw state unless policy explicitly permits retention

No artifact-evidence schema change is required for the pilot because the
existing artifact shape allows additional properties and already supports
validation reports.

### Metrics

Collect:

- exact agreement with the human gold route
- agreement with the deterministic route
- confusion matrix across Stage 1–8 and `unclear_or_cross_cutting`
- earliest-stage under-routing rate
- high-impact false-negative rate
- review recommendation precision and recall
- confidence coverage at each candidate threshold
- timeout, authentication, rate-limit, validation, and provider error counts
- median and 95th-percentile latency
- secrets-resolution failure count
- fallback success rate
- estimated cost per evaluated change

### Logging rules

- Use structured logs.
- Never log authorization headers or secret values.
- Do not log the raw state by default.
- Sanitize exception messages before emission.
- Record the provider request ID for support correlation.
- Record the returned model version because aliases can move.
- Keep operational logs separate from durable stage artifacts.

---

## Implementation Phases

### Foundation and threat review

Deliverables:

- approve this integration plan
- select the secrets-manager provider and runtime identity mechanism
- confirm TypeSafe organizational, privacy, retention, and network policies
- create development and CI API keys
- define data classification and allowed pilot inputs
- document incident ownership and credential rotation responsibility
- create a small threat review covering secret leakage, prompt/state leakage,
  route manipulation, provider outage, and incorrect high-confidence results

Exit criteria:

- no unresolved critical credential or data-handling risk
- runtime identity can retrieve only the environment-specific Jev secret
- operators can rotate and revoke the key without a repository change

### Add the isolated client and policy package

Deliverables:

- create the additive `jev-decision-support` skill
- implement the provider-neutral secret resolver
- implement the standard-library HTTPS transport
- implement typed request and response validation
- implement timeout, retry, error-classification, and sanitization behavior
- implement a local policy evaluator independent of network transport
- document operator configuration without including secret values

Exit criteria:

- unit tests pass without network or real credentials
- invalid and unavailable responses cannot influence workflow output
- secret values cannot appear in normal logs or exceptions
- the existing router test suite remains unchanged and passing

### Build the evaluation corpus

Create a sanitized, version-controlled corpus containing:

- at least 100 representative change requests
- at least 10 clear examples for each Stage 1–8 where the current workflow can
  route that stage
- ambiguous and cross-cutting requests
- synonyms not covered by current keyword rules
- active-stage refinements
- emergencies and high-impact security, privacy, authentication, payment,
  migration, and data-loss cases
- intentionally underspecified requests
- adversarial text that attempts to override routing criteria

Each case must include:

```json
{
  "case_id": "JEV-EVAL-001",
  "request": "",
  "current_workflow_state": {},
  "expected_mode": "change_cycle",
  "expected_entry_stage": "stage_3",
  "expected_review": true,
  "impact_tags": [],
  "rationale": "",
  "reviewed_by": ""
}
```

Two reviewers should resolve disputed gold labels for security-sensitive or
cross-cutting cases.

Exit criteria:

- all cases are sanitized
- every gold label is justified against the global workflow contract
- the corpus includes both easy and difficult cases rather than only examples
  copied from the decision criteria

### Run shadow evaluation

For every corpus case:

1. Run the existing deterministic classifier.
1. Run Jev with the pinned model and question-contract version.
1. Apply the local policy without changing the route.
1. Compare both results with the human gold route.
1. Generate aggregate metrics and a disagreement report.
1. Review all high-confidence errors and all earliest-stage under-routes.

Minimum acceptance criteria for advisory rollout:

- `100%` of responses conform to the expected local response shape or are
  rejected safely
- `100%` of unavailable or rejected responses fall back successfully
- `0` secrets appear in logs, fixtures, artifacts, or captured HTTP bodies
- `0` known critical cases are silently recommended for automatic handling
- Jev gold-route accuracy is no worse than the deterministic baseline
- the reviewed threshold has no earliest-stage under-routing on critical cases
- every disagreement is visible and reviewable

Accuracy alone is not sufficient. If the model improves average accuracy but
under-routes high-impact cases, remain in shadow mode.

### Enable advisory previews

After shadow acceptance, add an opt-in flag to the change preview path. The
preview may display:

```text
Authoritative route: Stage 3 (existing router)
Jev advisory route: Stage 3
Advisory confidence: high
Review recommendation: no additional review signal
```

For disagreement or uncertainty:

```text
Authoritative route: Stage 4 (existing router)
Jev advisory route: unclear_or_cross_cutting
Advisory confidence: low
Review recommendation: confirm the earliest affected stage before approval
```

Rules:

- the authoritative route remains unchanged
- the existing approval step remains mandatory
- disabling the flag restores the exact prior behavior
- network or secret failure produces a short non-blocking advisory-unavailable
  message
- raw probability details are available in diagnostic output, not presented as
  a guarantee to ordinary users

Exit criteria:

- opt-in operation is stable for an agreed observation period
- users understand which result is authoritative
- disagreement review catches useful cases without excessive noise
- the kill switch has been exercised successfully

### Consider additional use cases

Add one use case at a time, repeating corpus creation, shadow evaluation, and
advisory rollout.

Recommended order:

1. revision-loop ownership suggestion
1. Stage 6 failure classification
1. Stage 8 feedback and telemetry classification
1. Stage 5 agent or skill recommendation from an approved allowlist
1. evidence-quality and operational-priority scoring

Do not reuse Stage-routing thresholds for another use case. Each question
contract needs its own evaluation, thresholds, and failure policy.

---

## Detailed Test Plan

### Secret handling tests

- Resolver returns a secret only to the client boundary.
- Missing identity produces `advisory_unavailable`.
- Access denial produces `advisory_unavailable` without leaking provider text.
- Secret value is absent from stdout, stderr, logs, tracebacks, and artifacts.
- Authentication failure triggers at most one secret refresh.
- Rotation replaces the secret without a source-code or configuration commit.
- Tests and fixtures contain synthetic values only.

### Client tests

- Request includes the pinned model, sanitized state, and versioned questions.
- Authorization is sent only over the configured HTTPS endpoint.
- Choice, Score, and Noul responses are parsed and range checked.
- Unknown answer types, missing choices, out-of-range probabilities, malformed
  JSON, and model mismatch are rejected.
- Connection timeout and total timeout are enforced.
- Retryable rate-limit and provider failures use bounded backoff.
- Authentication and validation errors are not repeatedly retried.
- Provider request ID and returned model version are retained.

### Policy tests

- High-confidence agreement produces `agree`.
- Low confidence produces `review`.
- `unclear_or_cross_cutting` produces `review`.
- Deterministic/Jev disagreement produces `review`.
- Sensitive and high-impact tags produce `review` regardless of confidence.
- No policy result can create approval, readiness, or risk acceptance.
- Model unavailability leaves the deterministic route unchanged.

### Data-minimization tests

- Only allowlisted fields enter the serialized state.
- Full stage files cannot be passed accidentally.
- Credential-like values cause redaction or request rejection.
- Oversized input is rejected before secret retrieval and network access.
- Logs contain metadata but not raw state.

### Evaluation tests

- Every corpus case has a valid expected route and reviewer rationale.
- Metrics are reproducible for a pinned model and question contract.
- Confusion matrices include every allowed choice.
- Critical under-routes are reported separately from ordinary errors.
- A model or question-contract change invalidates the previous acceptance
  result until re-evaluation completes.

### Regression commands

The implementation should keep the existing checks green:

```sh
python -m unittest discover .opencode/Skills/change-intake-router/tests
python -m unittest discover .opencode/Skills/global-stage-readiness-audit/tests
python -m unittest discover .opencode/Skills/skill-registry-builder/tests
```

Add the new isolated suite:

```sh
python -m unittest discover .opencode/Skills/jev-decision-support/tests
```

---

## Failure Modes and Required Behavior

| Failure | Required behavior |
| --- | --- |
| Secret cannot be resolved | Skip Jev and continue with the existing route |
| API key rejected | Refresh the secret once, then skip and alert |
| TypeSafe rate limit | Retry within the bounded policy, then skip |
| Provider timeout or outage | Skip without blocking the workflow |
| Malformed response | Reject the advisory result and record an invalid-response metric |
| Model returns unexpected choice | Reject the result; never coerce it into a stage |
| Low confidence | Recommend human review |
| Jev disagrees with deterministic routing | Keep the deterministic route and recommend review |
| Sensitive state detected | Do not send the request |
| Model alias changes target version | Detect returned-version mismatch and remain in shadow/review mode |
| Evaluation regression | Disable advisory display and return to shadow mode |
| Logging leak suspected | Disable integration, rotate the key, preserve incident evidence safely, and investigate |

---

## Rollout and Rollback

### Feature controls

Provide separate controls for:

```text
JEV_ENABLED=false
JEV_MODE=shadow
JEV_MODEL=jev-1.14.0
JEV_QUESTION_CONTRACT=genesis-change-routing/1.0.0
JEV_TIMEOUT_SECONDS=<operator-defined>
```

These are non-secret settings. The API key is resolved separately from the
secrets manager.

### Kill switch

- `JEV_ENABLED=false` must prevent secret retrieval and network calls.
- Turning Jev off must restore the exact deterministic behavior.
- The kill switch must not require a code deployment when the runtime platform
  supports dynamic configuration.

### Rollback triggers

- credential or state leakage
- critical under-routing
- unexpected workflow mutation
- repeated provider instability
- material latency added to interactive previews
- question-contract drift without evaluation
- model-version drift without approval
- review burden greater than demonstrated routing benefit

### Rollback procedure

1. Disable Jev with the kill switch.
1. Confirm deterministic routing still works.
1. Revoke or rotate the API key if exposure is suspected.
1. Preserve sanitized diagnostics and provider request IDs.
1. Record the incident and corrective action outside stage readiness state.
1. Re-enter shadow mode only after the relevant test and evaluation gates pass.

---

## Ownership

| Area | Suggested owner |
| --- | --- |
| Question contract and gold labels | Workflow contract maintainer |
| Jev client and local policy | Harness tooling maintainer |
| Secrets-manager configuration | Platform or security owner |
| API key creation and rotation | Named credential custodian |
| Data classification and retention | Security/privacy owner |
| Evaluation review | Workflow maintainer plus domain reviewer |
| Incident response | Platform owner with harness maintainer |
| Future automation approval | User or explicitly delegated policy authority |

No agent should silently assume credential-custodian, risk-acceptance, or
automation-approval authority.

---

## Definition of Done for the Initial Integration

The initial Jev integration is complete when:

- the additive Jev skill and tests exist
- a secrets-manager-backed runtime identity retrieves the key without storing
  it in the repository or local files
- the client uses a pinned model and versioned question contract
- the state builder and redactor enforce the documented allowlist
- shadow evaluation meets all acceptance criteria
- advisory preview is opt-in and clearly identifies the authoritative route
- every Jev failure falls back to unchanged deterministic behavior
- no Jev output can approve, record, merge, deploy, accept risk, or mark stage
  readiness
- the feature can be disabled without changing workflow state
- credential rotation and incident rollback have been tested
- existing router, readiness-audit, and registry-builder tests still pass
- an evaluation report documents benefits, errors, thresholds, and remaining
  risks in language understandable to a human reviewer

---

## Future Decision Point

After the advisory integration has operated long enough to produce
representative evidence, prepare a separate proposal answering:

- Which exact low-risk decision, if any, should Jev be allowed to automate?
- What is the measured error rate at the proposed threshold?
- What is the earliest-stage under-routing rate?
- How much latency and reasoning-model usage does the integration save?
- How often does advisory disagreement lead to a corrected route?
- Are secrets-manager, provider, privacy, and incident controls working?
- Does the benefit justify the new external dependency?

That proposal must be reviewed as a workflow-policy change. Until approved,
the existing Genesis workflow remains authoritative and Jev remains advisory.

---

## Official Jev References

- [TypeSafe introduction](https://docs.typesafe.ai/introduction)
- [TypeSafe quick start and API examples](https://docs.typesafe.ai/introduction/quickstart)
- [TypeSafe confidence guidance](https://docs.typesafe.ai/confidence)
- [TypeSafe models and version aliases](https://docs.typesafe.ai/models)
- [TypeSafe Python SDK usage, retries, errors, and environment variables](https://docs.typesafe.ai/sdk/python/usage/basic)
- [TypeSafe legal and data-handling information](https://docs.typesafe.ai/legal)

Provider documentation can change. Reconfirm API fields, model availability,
pricing, data handling, SDK behavior, and error semantics before implementation
and before each production model upgrade.
