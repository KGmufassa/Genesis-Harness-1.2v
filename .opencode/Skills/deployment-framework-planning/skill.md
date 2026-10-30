---
name: deployment-framework-planning
description: The deployment-framework-planning skill defines the deployment model needed to operate the product in production.
compatibility: opencode
---

# Skill — deployment-framework-planning

# Purpose

The `deployment-framework-planning` skill defines the deployment model needed to operate the product in production.

It plans:

* deployment environments
* setup requirements
* deployment checklist
* release process
* rollback process
* deployment risks

---

# Core Responsibilities

## Environment Planning

Define:

* local, staging, and production environment needs
* required services
* required secrets and configuration
* build commands
* deployment commands
* smoke checks

Do not invent secrets or environment values. Missing secrets must become blockers or setup actions.

## Deployment Checklist

Produce an ordered checklist for launch execution, including setup, build, deploy, verify, rollback, and post-deploy checks.

## Rollback Planning

Define rollback triggers, rollback commands, owner expectations, and user/data impact.

---

# Inputs

```json
{
  "launch_readiness": {},
  "implementation_status": {},
  "system_health": {},
  "stage_5_release_plan": {},
  "existing_state": {}
}
```

---

# Deployment Proof Responsibilities

When Stage 7 claims deployment readiness, this skill must define or collect:

```json
{
  "deployment_proof": {
    "production_build_artifact": "",
    "deployment_dry_run_result": {},
    "smoke_test_results": [],
    "rollback_test_result": {},
    "environment_verification": {},
    "monitoring_alert_test": {},
    "release_blockers": [],
    "accepted_launch_risks": []
  }
}
```

Deployment proof artifacts must be recorded or referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

---

# Outputs

Update shared Stage 7 state in:

```text
Build-Plans/Build-status/Operationalization-state.json
```

Return:

```json
{
  "deployment_framework": {},
  "deployment_environments": [],
  "deployment_checklist": [],
  "rollback_plan": {},
  "deployment_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-7/02-deployment-framework.json
```
