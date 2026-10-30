# Dynamic Security Review Agent Skill

# Purpose

The `security-review` skill should operate as a general dynamic agent skill for reviewing and hardening code security.

It should not be integrated as a Stage 1-8 command or stage subskill.

It is intended to be used by implementation, review, or validation agents when code changes touch security-sensitive areas.

---

# Core Role

The skill transforms:

* changed code
* implementation tasks
* API routes
* authentication logic
* database access
* user input handling
* file uploads
* external integrations
* AI endpoints
* payment or webhook flows

into:

* security surface maps
* selected context-aware checks
* severity-ranked findings
* suggested or applied fixes
* verification steps
* residual risk reports

---

# Dynamic Operating Model

The skill should follow this workflow:

```text
Scan changed files
↓
Detect project stack and security surfaces
↓
Classify risk level
↓
Select relevant security checks
↓
Review prioritized files and nearby boundaries
↓
Patch issues if the agent has permission
↓
Recommend or run verification
↓
Report residual risk
```

---

# Activation Triggers

Use this skill when a task touches:

* authentication
* authorization
* sessions
* cookies
* API routes
* server actions
* database reads or writes
* user input
* file uploads
* admin features
* payments
* webhooks
* secrets
* environment variables
* third-party APIs
* AI endpoints
* sensitive user data
* logging or error handling
* deployment configuration

---

# Non-Goals

This skill should not:

* orchestrate a product stage
* generate build tickets
* replace Stage 6 validation
* perform broad refactors unrelated to security
* invent missing business rules
* weaken security to satisfy convenience
* mark stage completion

Stage 6 controls execution.

`security-review` controls security judgment.

---

# Review Modes

The skill should support these modes:

```text
review_mode
fix_mode
pre_completion_check
pre_deploy_check
```

## review_mode

Report findings only.

Use when the agent does not have edit permission or the user requested review only.

## fix_mode

Patch high-confidence security issues and verify the fix.

Use only when the agent has edit permission.

## pre_completion_check

Run before an implementation agent marks security-sensitive work complete.

## pre_deploy_check

Perform a broader production-readiness security review.

---

# Permission-Aware Behavior

The skill must adapt to agent permissions:

```text
edit denied -> report findings only
edit allowed -> patch safe and well-scoped issues
bash denied -> list verification commands
bash allowed -> run focused security checks when appropriate
```

Do not attempt invasive changes when operating in review-only mode.

---

# Dynamic Context Detection

Before reviewing, detect:

```json
{
  "framework": "",
  "runtime": "",
  "package_manager": "",
  "auth_system": "",
  "database_layer": "",
  "deployment_target": "",
  "api_surface": [],
  "auth_surface": [],
  "data_access_surface": [],
  "sensitive_operations": [],
  "security_relevant_files": []
}
```

Examples:

* Next.js route handlers
* Express routes and middleware
* Supabase clients and RLS assumptions
* Prisma, Drizzle, or raw SQL queries
* Clerk, Auth.js, Supabase Auth, JWT, or custom auth
* Stripe, GitHub, Clerk, Supabase, or custom webhooks
* OpenAI or other AI provider endpoints

---

# Changed-Files-First Review

Prioritize review in this order:

```text
1. changed files
2. imported auth, database, config, validation, and secret helpers
3. route handlers, controllers, server actions, and middleware
4. permission checks and ownership checks
5. tests covering the changed behavior
6. deployment and environment configuration if affected
```

Only expand beyond this scope when the changed files cross a security boundary or expose a likely vulnerability.

---

# Security Surface Classification

Classify touched code into one or more surfaces:

```text
public_surface
authenticated_surface
privileged_surface
data_read_surface
data_write_surface
secret_handling_surface
external_integration_surface
file_upload_surface
payment_surface
webhook_surface
ai_abuse_surface
logging_surface
deployment_surface
```

Each surface should determine which checks are selected.

---

# Context-Based Check Selection

## API Route Or Server Action

Check:

* authentication
* authorization
* input validation
* rate limiting
* safe error handling
* sensitive logging
* response data exposure

## Database Read Or Write

Check:

* parameterized queries
* row ownership
* role permissions
* mass assignment
* RLS assumptions
* transaction safety

## Auth Or Session Code

Check:

* secure cookie flags
* token storage
* session expiration
* refresh behavior
* CSRF exposure
* privilege escalation paths

## File Upload

Check:

* file size limit
* MIME type allowlist
* extension allowlist
* storage permissions
* virus or content scanning needs
* path traversal risk

## Webhook

Check:

* signature verification
* raw body handling
* timestamp tolerance
* replay protection
* idempotency
* event allowlist
* retry behavior

## Payment

Check:

* webhook verification
* idempotency
* amount and currency validation
* metadata trust boundaries
* sensitive logging
* authorization around billing actions

## AI Endpoint

Check:

* prompt size limits
* rate limits
* abuse controls
* prompt injection exposure
* unsafe tool invocation
* system prompt leakage
* sensitive data in prompts or logs
* output validation

## Frontend Rendering

Check:

* unsafe HTML rendering
* `dangerouslySetInnerHTML`
* DOM injection
* token storage in browser
* sensitive data exposure

## Secrets And Config

Check:

* hardcoded secrets
* exposed service roles
* env var validation
* `.env` git safety
* accidental logging

---

# Recommended Search Patterns

Use focused searches such as:

```bash
rg "process.env|localStorage|sessionStorage|dangerouslySetInnerHTML|innerHTML|eval\\(|Function\\("
rg "password|secret|token|apiKey|privateKey|service_role|Authorization|Bearer"
rg "SELECT .*\\$\\{|query\\(|raw\\(|execute\\(|from\\(|insert\\(|update\\(|delete\\("
rg "NextResponse|route.ts|route.js|server action|app/api|pages/api"
rg "webhook|signature|stripe|clerk|github|supabase"
rg "upload|File|FormData|multipart|blob|bucket|storage"
```

Searches should be adapted to the actual stack.

---

# Risk Escalation Rules

Use this severity model:

## Critical

Examples:

* exposed secrets
* auth bypass
* service role leakage
* payment or webhook spoofing
* arbitrary code execution
* unrestricted admin action

## High

Examples:

* missing authorization
* cross-user data access
* unsafe file upload
* SQL injection risk
* sensitive data exposure
* missing webhook signature verification

## Medium

Examples:

* missing rate limits
* weak input validation
* verbose user-facing errors
* incomplete CSRF protection
* missing security tests

## Low

Examples:

* missing security headers
* incomplete logging redaction
* dependency update recommendations
* minor hardening opportunities

---

# Abuse-Case Prompts

For every risky change, ask:

```text
How could an unauthenticated user abuse this?
How could an authenticated user access another user's data?
How could a normal user perform an admin action?
How could this be spammed or overloaded?
Could this leak secrets, tokens, PII, prompts, or internal errors?
Could this trust client-provided data that must be server-verified?
Could this endpoint be replayed, forged, or called out of order?
```

---

# Safe Logging Rules

Never log:

* passwords
* API keys
* access tokens
* refresh tokens
* session cookies
* authorization headers
* full request bodies containing sensitive data
* payment details
* private user data
* service role keys
* private prompts or system prompts
* sensitive AI inputs or outputs

Prefer structured, redacted logs:

```json
{
  "event": "payment_webhook_failed",
  "user_id": "usr_123",
  "provider_event_id": "evt_123",
  "reason": "signature_invalid"
}
```

---

# Security Test Recommendations

Recommend or create tests for:

* unauthenticated request returns `401`
* unauthorized cross-user access returns `403`
* invalid input returns `400`
* dangerous payload is rejected
* rate limit returns `429`
* webhook rejects invalid signature
* webhook replay is rejected
* file upload rejects invalid type and oversized files
* protected action requires correct role
* user-facing errors do not expose internals

---

# Finding Output Format

Use this format for findings:

```json
{
  "finding_id": "SEC-001",
  "severity": "critical | high | medium | low",
  "category": "",
  "surface": "",
  "file": "",
  "issue": "",
  "risk": "",
  "recommended_fix": "",
  "verification_step": "",
  "status": "open | fixed | accepted_risk | not_applicable"
}
```

---

# Review Report Output

Return:

```json
{
  "security_review_status": "passed | fixed | findings_remaining | blocked",
  "review_mode": "",
  "detected_context": {},
  "surfaces_reviewed": [],
  "selected_checks": [],
  "skipped_checks": [],
  "findings": [],
  "fixes_applied": [],
  "verification": [],
  "residual_risks": []
}
```

---

# Fix Behavior

When edits are allowed:

* patch only security issues with clear evidence
* keep fixes scoped to the affected surface
* preserve existing application behavior unless behavior is unsafe
* add or update focused tests when possible
* run relevant validation commands when allowed
* document any remaining risk

When edits are not allowed:

* report findings
* include exact file references
* include recommended fixes
* include verification steps

---

# Completion Rule

Do not mark security-sensitive work complete until:

* relevant surfaces were reviewed
* critical and high findings are fixed or explicitly reported
* verification steps were run or listed
* residual risks are documented
* security-sensitive assumptions are stated clearly

---

# Efficiency Principle

The skill should be broad enough to catch serious security problems, but narrow enough to avoid slowing every implementation task.

Default behavior:

```text
Review changed security-relevant files first.
Expand only when imports, permissions, data flow, or execution paths require it.
```

