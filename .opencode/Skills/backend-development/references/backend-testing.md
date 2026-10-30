# Backend Testing Strategies

Comprehensive testing approaches, frameworks, and quality assurance practices for backend systems.

## Contents

- Use When
- Fast Rules
- Test Pyramid
- Unit Testing
- Integration Testing
- Contract Testing
- Load Testing
- E2E Testing
- Migration Testing
- Security Testing
- Coverage
- CI/CD Testing

## Use When

- Choosing unit, integration, contract, load, E2E, migration, or security test coverage
- Adding verification for backend code changes
- Reviewing CI test gates and coverage expectations

## Fast Rules

- Match tests to risk and existing project tooling before adding new frameworks.
- Keep most tests fast and deterministic; reserve E2E/load/security scans for the paths that justify them.
- Treat coverage percentages as heuristics, not substitutes for meaningful assertions.

## Test Pyramid (70-20-10 Rule)

```text
        /\
       /E2E\     10% - End-to-End Tests
      /------\
     /Integr.\ 20% - Integration Tests
    /----------\
   /   Unit     \ 70% - Unit Tests
  /--------------\
```

## Unit Testing

### Frameworks by Language

- **TypeScript/JavaScript:** Vitest, Jest
- **Python:** Pytest, Unittest
- **Go:** testing, testify

### Best Practices

```typescript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid data', async () => {
      const userData = { email: 'test@example.com', name: 'Test' };
      const user = await userService.createUser(userData);

      expect(user).toMatchObject(userData);
      expect(user.id).toBeDefined();
    });
  });
});
```

### Mocking

```typescript
jest.mock('./emailService');
```

## Integration Testing

### API Integration Tests

```typescript
import request from 'supertest';
import { app } from '../app';
```

### Database Testing with TestContainers

```typescript
import { GenericContainer } from 'testcontainers';
```

## Contract Testing (Microservices)

### Pact

```typescript
import { Pact } from '@pact-foundation/pact';
```

## Load Testing

### k6

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';
```

### Performance Thresholds

- Response time: p95 < 500ms
- Response time: p99 < 1s
- Error rate: < 1%
- Test at 2x expected peak

## E2E Testing

### Playwright

```typescript
import { test, expect } from '@playwright/test';
```

## Database Migration Testing

Critical for schema evolution and rollback confidence.

## Security Testing

### SAST

```bash
sonar-scanner
semgrep --config auto src/
```

### DAST

```bash
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://api.example.com \
  -r zap-report.html
```

### Dependency Scanning

```bash
npm audit
snyk test
```

Review dependency findings first, then make intentional upgrades. Avoid automatic fix commands unless dependency churn and lockfile changes are acceptable for the task.

## Code Coverage

### Target Metrics

- Overall coverage: 80%+
- Critical paths: 100%
- New code: 90%+

## CI/CD Testing Pipeline

```yaml
name: Test Pipeline

on: [push, pull_request]
```

## Testing Best Practices

1. Arrange-Act-Assert
2. Descriptive test names
3. Test edge cases
4. Clean test data
5. Fast tests
6. Deterministic tests
7. Independent tests

## Testing Checklist

- [ ] Unit tests cover core logic
- [ ] Integration tests for API endpoints
- [ ] Contract tests for microservices
- [ ] Load tests configured
- [ ] E2E tests for critical flows
- [ ] Migration tests
- [ ] Security scanning in CI/CD
- [ ] Coverage reports automated
- [ ] Tests run on every PR
- [ ] Flaky tests eliminated

## Resources

- **Vitest:** https://vitest.dev/
- **Playwright:** https://playwright.dev/
- **k6:** https://k6.io/docs/
- **Pact:** https://docs.pact.io/
- **TestContainers:** https://testcontainers.com/
