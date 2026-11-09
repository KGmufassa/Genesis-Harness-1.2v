# Stage 1–8 Supervised Application Pilot

## Status

- Patch 20: prepared; live execution pending application selection and access.
- This repository contains the harness, not an application. Do not advance its baseline workflow or invent a pilot product, live deployment, signup counts, or telemetry.
- Required input: the approved product/application and its repository, intended platforms, and access to its actual research, runtime, deployment, and telemetry environments.

---

## Execution

1. Run the existing test suites and stage-specific seed validation before starting; retain the actual results.
1. Stage 1: approve features, MVP boundaries, target platforms, and the feature-content fingerprint.
1. Stage 2: collect real evidence and populate assumptions, evidence quality, confidence, critical unknowns, and authorized risks. Do not substitute a waitlist launch for research.
1. Stage 3: compare current deployment methods, approve a concrete stack and strategy, and retain the reviewed scope/stack/strategy fingerprints.
1. Stage 4: create, review, publish, and verify the waitlist using those decisions. Retain public publication and signup/measurement evidence without personal data; complete app-wide page/design approval afterward. Do not wait for a signup target.
1. Stage 5: construct and audit the normalized context, eight artifacts, and manifest. Validate scopes, waves, references, and completion definitions.
1. Stage 6: implement the approved tickets and collect genuine persistence, end-to-end, responsive, accessibility, and design-system proof.
1. Stage 7: perform the actual production build, deployment rehearsal, smoke tests, rollback, environment verification, and monitoring-alert test. Resolve release blockers and review any expressly allowed accepted risks.
1. Stage 8: use real operational signals to create owned feedback routes with valid target stages, evidence, actions, and cycle decisions.
1. At every finalization attempt, run the readiness CLI in the application workspace and retain both failed and successful audit evidence. Review results manually during the pilot.

```sh
python3 /path/to/harness/.opencode/Skills/global-stage-readiness-audit/scripts/run_readiness_audit.py \
  --workspace-root /path/to/application \
  --stage 4 \
  --proposed-status ready_for_stage_5
```

- The application workspace must have the harness contracts/schemas and its own `Build-Plans` structure. The harness code can run from this repository; resolve all artifact paths in the application workspace.
- Use the existing Stage 1–8 command skills to generate the outputs. Do not copy the synthetic test fixture and label it real evidence.

---

## Evidence Review And Completion

| Area | Required Review |
| --- | --- |
| Product and research | Approved scope/platforms; real sources; justified confidence and risks |
| Pre-code decisions | Approved stack/strategy fingerprints; compatible targets |
| Waitlist | Real published URL and durable signup/measurement proof |
| Design | Complete page approvals, matching hashes, responsive/accessibility evidence |
| Orchestration | Complete normalized package with resolvable handoffs |
| Runtime | Successful critical workflows backed by genuine artifacts |
| Launch | All six actual proof categories, resolved blockers, authorized risks |
| Evolution | Real signal sources and valid owned feedback routes |

- Complete Patch 20 only after all eight stages have genuine reviewable outputs and the supervised review is recorded.
- Retain failures and repairs; do not hide them by replacing history with successful defaults.
- Record the product, run dates, audit locations, observed limitations, and reviewer decision in a new pilot evidence report. Reassess health from that evidence before considering unattended operation or an A+ grade.
