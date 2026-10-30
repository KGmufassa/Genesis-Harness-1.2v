# Backend Technologies

Core technologies, frameworks, databases, and message queues for backend development.

## Contents

- Use When
- Fast Rules
- Programming Languages
- Databases
- ORMs And Database Tools
- Message Queues And Event Streaming
- Framework Comparisons
- Technology Selection Flowchart
- Situational Defaults
- Common Pitfalls

## Use When

- Choosing or comparing backend languages, frameworks, databases, queues, caches, or ORMs
- Reviewing whether a proposed technology fits the team's constraints
- Planning a stack change or new backend service

## Fast Rules

- Start with the repository's existing stack and team familiarity.
- Prefer boring, well-supported tools unless scale, latency, compliance, or product constraints require more complexity.
- Avoid adding distributed infrastructure before the app has clear operational need and ownership.
- Verify current framework and provider docs before committing to version-specific guidance.

## Programming Languages

### Node.js/TypeScript

**Best For:**
- Full-stack JavaScript teams
- Real-time applications
- Rapid prototyping
- Event-driven architectures

**Popular Frameworks:**
- **NestJS**
- **Express**
- **Fastify**
- **tRPC**

### Python

**Best For:**
- Data-heavy applications
- ML/AI integration
- Scientific computing
- Scripting and automation

**Popular Frameworks:**
- **FastAPI**
- **Django**
- **Flask**

### Go

**Best For:**
- High-concurrency systems
- Microservices
- CLI and DevOps tooling
- Simple deployment

### Rust

**Best For:**
- Performance-critical systems
- Memory-safe system programming
- High-reliability requirements
- Low-level control

## Databases

### PostgreSQL

**Strengths:**
- ACID compliance
- JSONB support
- Advanced indexing
- Full-text search

### MongoDB

**Strengths:**
- Flexible schemas
- Sharding
- Aggregation pipeline

### Redis

**Capabilities:**
- In-memory key-value store
- Pub/sub
- Sorted sets
- Streams

## ORMs And Database Tools

- **Drizzle ORM**
- **Prisma**
- **TypeORM**
- **SQLAlchemy**

## Message Queues & Event Streaming

### RabbitMQ

Best for task queues and request/reply patterns.

### Apache Kafka

Best for durable event streaming, replay, and high-throughput systems when the team can operate it.

## Framework Comparisons

### Node.js Frameworks

| Framework | Performance | Learning Curve | Use Case |
|-----------|------------|----------------|----------|
| Express | Moderate | Easy | Simple APIs |
| NestJS | Moderate | Steep | Enterprise apps |
| Fastify | High | Moderate | Performance-critical |
| tRPC | High | Moderate | Full-stack TypeScript |

### Python Frameworks

| Framework | Performance | Features | Use Case |
|-----------|------------|----------|----------|
| FastAPI | High | Modern, async | New APIs |
| Django | Moderate | Batteries-included | Full-featured apps |
| Flask | Moderate | Minimal | Simple services |

## Technology Selection Flowchart

```text
Start -> Existing repo stack fits?
       -> Yes -> extend existing stack
       -> No -> Need ML/data-heavy workflow?
              -> Yes -> Python ecosystem
              -> No -> Need very high concurrency/simple deploys?
                     -> Yes -> Go
                     -> No -> Need memory safety/performance-critical code?
                            -> Yes -> Rust
                            -> No -> TypeScript or Python based on team fit
```

## Situational Defaults

- REST: simple public APIs, CRUD-heavy services, broad client compatibility
- GraphQL: many client-specific read shapes, mature schema governance, strong resolver performance discipline
- gRPC: internal service-to-service APIs with typed contracts and low-latency needs
- Redis pub/sub or streams: simple realtime, caching, lightweight queues
- RabbitMQ, SQS, Pub/Sub: work queues and business events without Kafka-level stream requirements
- Kafka: durable high-throughput streams, replay, event logs, and teams prepared to operate it

## Common Pitfalls

1. Choosing NoSQL for relational data
2. Not using connection pooling
3. Ignoring indexes
4. Over-engineering with microservices
5. Not caching

## Resources

- **NestJS:** https://nestjs.com
- **FastAPI:** https://fastapi.tiangolo.com
- **PostgreSQL:** https://www.postgresql.org/docs/
- **MongoDB:** https://www.mongodb.com/docs/
- **Redis:** https://redis.io/docs/
- **Kafka:** https://kafka.apache.org/documentation/
