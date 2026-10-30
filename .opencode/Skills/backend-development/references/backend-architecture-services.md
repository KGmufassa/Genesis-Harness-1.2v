# Service Architecture Patterns

## Monolith vs Microservices

### Monolithic Architecture

**Pros:**
- Simple to develop and deploy
- Easy local testing
- Single codebase
- Strong consistency

**Cons:**
- Tight coupling
- Scaling limitations
- All-or-nothing deployments

**When to Use:** Startups, MVPs, small teams, unclear domain boundaries

### Microservices Architecture

**Pros:**
- Independent deployment
- Technology flexibility
- Fault isolation
- Easier independent scaling

**Cons:**
- Complex deployment
- Network and consistency challenges
- Operational overhead

**When to Use:** Large teams, clear domain boundaries, different scaling needs

## Database per Service Pattern

Each service owns its own database. This improves isolation and autonomy, but removes direct cross-service joins.

## API Gateway Pattern

Responsibilities:
- request routing
- auth
- rate limiting
- transformation
- caching

```yaml
services:
  - name: user-service
    url: http://user-service:3000
plugins:
  - name: rate-limiting
  - name: jwt
```

## Service Discovery

```typescript
import Consul from 'consul';

const consul = new Consul();
```

Use when service instances are dynamic and addresses cannot be hardcoded.

## Circuit Breaker Pattern

Use to stop repeated calls to a failing dependency and prevent cascade failures.

```typescript
import CircuitBreaker from 'opossum';

const breaker = new CircuitBreaker(callExternalService, {
  timeout: 3000,
  errorThresholdPercentage: 50,
  resetTimeout: 30000,
});
```

## Saga Pattern

Use for distributed workflows that cannot rely on a single ACID transaction.

- choreography for looser coupling
- orchestration for stronger central control
