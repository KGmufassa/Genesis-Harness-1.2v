---
name: backend-development
description: Backend engineering guidance for designing, implementing, reviewing, debugging, securing, scaling, testing, or operating server-side systems. Use for backend API contracts, service architecture, authentication and authorization, security hardening, performance, technology selection, test strategy, deployment, observability, production debugging, and maintainability work.
compatibility: opencode
---

# Backend Development

Use this skill to produce production-minded backend recommendations while staying anchored to the repository in front of you.

## Default Protocol

1. Inspect the project stack, framework, database, deployment model, dependency policy, and existing patterns before recommending changes.
2. Prefer existing repository conventions over generic backend defaults.
3. Load the smallest relevant reference file first; add a second reference only when the task crosses domains.
4. Treat security, authentication, compliance, cloud-provider, and fast-moving ecosystem guidance as freshness-sensitive; verify current primary documentation when the exact standard, rule, or version matters.
5. State tradeoffs when multiple backend choices are valid.

## Reference Routing

- API style choice or cross-API concerns -> `references/backend-api-design.md`
- REST routes, payloads, errors, pagination, filtering, versioning, OpenAPI -> `references/backend-api-rest.md`
- GraphQL schema, resolvers, query shape, DataLoader -> `references/backend-api-graphql.md`
- gRPC contracts, protobuf, internal service APIs -> `references/backend-api-grpc.md`
- Architecture entry point, boundaries, anti-patterns -> `references/backend-architecture.md`
- Monoliths, microservices, gateways, discovery, sagas -> `references/backend-architecture-services.md`
- Event sourcing, brokers, CQRS, streaming -> `references/backend-architecture-events.md`
- Scaling topology, sharding, caching layers -> `references/backend-architecture-scaling.md`
- Login, sessions, RBAC, MFA, JWT, OAuth, API keys -> `references/backend-authentication.md`
- Vulnerabilities, validation, rate limiting, headers, secrets -> `references/backend-security.md`
- Slow queries, caching, load balancing, pooling, throughput -> `references/backend-performance.md`
- Deployment, CI/CD, Docker, Kubernetes, monitoring, health checks -> `references/backend-devops.md`
- Failing behavior, traces, logs, profiling, incident triage -> `references/backend-debugging.md`
- Maintainability entry point -> `references/backend-code-quality.md`
- SOLID or dependency boundaries -> `references/backend-code-principles.md`
- Design patterns -> `references/backend-code-patterns.md`
- Code organization, error handling, refactoring -> `references/backend-code-practices.md`
- Language, framework, database, queue, cache, ORM choice -> `references/backend-technologies.md`
- Test coverage, unit/integration/E2E, load, contract, security testing -> `references/backend-testing.md`
- Tradeoffs, decomposition, resilience, review posture -> `references/backend-mindset.md` as secondary context unless the user explicitly asks for architectural reasoning.
- Skill maintenance and reference freshness checks -> `references/backend-maintenance.md`

## Combined Routing

For overlapping work, read references in this order:

- API + auth -> relevant API reference, then `references/backend-authentication.md`
- API + security -> relevant API reference, then `references/backend-security.md`
- architecture + performance -> relevant architecture reference, then `references/backend-performance.md`
- architecture + operations -> relevant architecture reference, then `references/backend-devops.md`
- auth + security -> `references/backend-authentication.md`, then `references/backend-security.md`
- debugging + performance -> `references/backend-debugging.md`, then `references/backend-performance.md`
- debugging + production operations -> `references/backend-debugging.md`, then `references/backend-devops.md`
- implementation + testing -> relevant code-quality reference, then `references/backend-testing.md`
- stack choice + architecture -> `references/backend-technologies.md`, then relevant architecture reference

## Output Contract

When using this skill:

- cite the reference file or files used
- give concrete recommendations tied to the current stack and repository patterns
- prefer production-safe defaults without forcing unnecessary infrastructure
- identify risk, rollout, and verification steps when behavior changes
- avoid loading unrelated references
- avoid presenting draft, dated, or context-dependent guidance as universal fact

## Maintenance

When updating this skill, keep `SKILL.md` as a router and put details in one-level references. For freshness and consistency checks, use `references/backend-maintenance.md`.
