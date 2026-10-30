# Backend Skill Maintenance

Use this reference only when updating the `backend-development` skill.

## Fast Checks

- Keep `SKILL.md` as a compact router; move detailed backend advice into one-level reference files.
- Search for absolute year-based claims such as `2025 standard`, `modern standard`, and `replaces`.
- Verify security, authentication, compliance, cloud-provider, and package-version guidance against primary sources.
- Check references for contradictory advice before adding new rules.
- Replace copy-risky examples: plaintext secrets, automatic dependency mutation, broad credentials, unsafe defaults.
- Keep recommendations conditional when infrastructure has meaningful operating cost, such as Kafka, Kubernetes, service mesh, distributed tracing, or multi-region databases.
- Prefer repo-first language: inspect the existing stack and conventions before introducing new tools.

## Consistency Checks

- Password policy should avoid arbitrary composition rules unless required by a stated policy.
- Authentication guidance should distinguish sessions, OAuth/OIDC flows, JWTs, API keys, and service credentials by client type and risk.
- Testing guidance should prefer project-local tools and risk-based coverage over fixed percentages.
- DevOps guidance should separate local examples from production deployment patterns.

## Freshness Sources

- OWASP Top 10 and Cheat Sheets: https://owasp.org/
- OAuth and OIDC specifications: https://oauth.net/2.1/ and https://openid.net/
- NIST Digital Identity Guidelines: https://pages.nist.gov/800-63-3/
- OpenTelemetry documentation: https://opentelemetry.io/docs/
- Official framework, cloud-provider, and database documentation for version-specific details
