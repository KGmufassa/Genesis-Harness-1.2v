# Backend DevOps Practices

CI/CD pipelines, containerization, deployment strategies, and monitoring for backend systems.

## Contents

- Use When
- Fast Rules
- Deployment Strategies
- Containerization With Docker
- Kubernetes Orchestration
- CI/CD Pipelines
- Monitoring And Observability
- Health Checks
- Secrets Management
- Infrastructure As Code
- DevOps Checklist

## Use When

- Designing or reviewing Docker, CI/CD, deployment, Kubernetes, health checks, observability, secrets, or IaC
- Preparing a backend for production operations
- Debugging release, environment, or runtime readiness problems

## Fast Rules

- Match deployment guidance to the repo's current platform and operational maturity.
- Prefer simple deployments until traffic, availability, or compliance needs justify Kubernetes, service mesh, or progressive delivery.
- Keep secrets in managed secret stores or environment-specific secret injection; never put real secrets in examples or committed config.
- Verify current provider and tool documentation before changing production infrastructure.

## Deployment Strategies

### Blue-Green Deployment

**Concept:** Two identical environments (Blue = current, Green = new)

```text
Production Traffic → Blue (v1.0)
                     Green (v2.0) ← Deploy & Test

Switch:
Production Traffic → Green (v2.0)
                     Blue (v1.0) ← Instant rollback available
```

### Canary Deployment

```bash
kubectl set image deployment/api api=myapp:v2
kubectl rollout pause deployment/api
kubectl rollout resume deployment/api
```

### Feature Flags (Progressive Delivery)

```typescript
import { LaunchDarkly } from 'launchdarkly-node-server-sdk';

const client = LaunchDarkly.init(process.env.LD_SDK_KEY);
const showNewCheckout = await client.variation('new-checkout', user, false);
```

## Containerization with Docker

### Multi-Stage Builds (Optimize Image Size)

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm ci --omit=dev
COPY --from=builder /app/dist ./dist
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

### Docker Compose (Local Development)

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=myapp
    volumes:
      - postgres-data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres-data:
```

## Kubernetes Orchestration

### Deployment Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: api
        image: myregistry/api:v1.0.0
        ports:
        - containerPort: 3000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
```

### Horizontal Pod Autoscaling

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-deployment
  minReplicas: 3
  maxReplicas: 10
```

## CI/CD Pipelines

### GitHub Actions

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'
          cache: 'npm'
      - name: Install dependencies
        run: npm ci
      - name: Run linter
        run: npm run lint
      - name: Run tests
        run: npm run test:ci
```

## Monitoring & Observability

### Three Pillars of Observability

**Metrics (Prometheus + Grafana):**
```typescript
import { Counter, Histogram, register } from 'prom-client';
```

**Logs (ELK Stack):**
```typescript
import winston from 'winston';
import { ElasticsearchTransport } from 'winston-elasticsearch';
```

**Traces (Jaeger/OpenTelemetry):**
```typescript
import { NodeSDK } from '@opentelemetry/sdk-node';
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';
```

### Health Checks

```typescript
app.get('/health/liveness', (req, res) => {
  res.status(200).json({ status: 'ok', timestamp: Date.now() });
});

app.get('/health/readiness', async (req, res) => {
  const checks = {
    database: await checkDatabase(),
    redis: await checkRedis(),
    externalAPI: await checkExternalAPI(),
  };

  const isReady = Object.values(checks).every(Boolean);
  res.status(isReady ? 200 : 503).json({
    status: isReady ? 'ready' : 'not ready',
    checks,
  });
});
```

## Secrets Management

### HashiCorp Vault

```bash
vault kv put secret/myapp/db password='<managed-secret-value>'
vault kv get -field=password secret/myapp/db
```

### Kubernetes Secrets

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  url: '<database-url-from-secret-manager>'
```

Use placeholder values only in examples. For real deployments, inject secrets through the platform's secret manager and keep manifests free of plaintext credentials where possible.

## Infrastructure as Code (Terraform)

```hcl
resource "aws_db_instance" "main" {
  identifier        = "myapp-db"
  engine            = "postgres"
  engine_version    = "15.3"
  instance_class    = "db.t3.micro"
}
```

## DevOps Checklist

- [ ] CI/CD pipeline configured
- [ ] Docker multi-stage builds implemented
- [ ] Kubernetes deployment manifests created
- [ ] Blue-green or canary deployment strategy
- [ ] Feature flags configured
- [ ] Health checks implemented
- [ ] Monitoring configured
- [ ] Logging configured
- [ ] Distributed tracing configured
- [ ] Secrets management in place
- [ ] Infrastructure as Code defined
- [ ] Autoscaling configured

## Resources

- **Kubernetes:** https://kubernetes.io/docs/
- **Docker:** https://docs.docker.com/
- **Prometheus:** https://prometheus.io/docs/
- **OpenTelemetry:** https://opentelemetry.io/docs/
- **Terraform:** https://www.terraform.io/docs/
