# Backend Architecture Patterns

Use this file as the entry point for architecture work. Load only the detailed reference that matches the architecture question.

## Read This First For

- choosing monolith vs microservices
- deciding between service, event, and scaling patterns
- routing architecture work to the right detailed reference

## Reference Routing

- service decomposition, gateway, discovery, circuit breaker, saga:
  `references/backend-architecture-services.md`
- event sourcing, brokers, CQRS:
  `references/backend-architecture-events.md`
- horizontal scaling, sharding, caching layers:
  `references/backend-architecture-scaling.md`

## Decision Matrix

| Pattern | When to Use | Complexity | Benefits |
|---------|-------------|------------|----------|
| **Monolith** | Small team, MVP, unclear boundaries | Low | Simple, fast development |
| **Microservices** | Large team, clear domains, need scaling | High | Independent deployment, fault isolation |
| **Event-Driven** | Async workflows, audit trail needed | Moderate | Decoupling, scalability |
| **CQRS** | Different read/write patterns | High | Optimized queries, scalability |
| **Serverless** | Spiky traffic, event-driven | Low | Auto-scaling, pay-per-use |

## Anti-Patterns To Avoid

1. Distributed monolith
2. Chatty services
3. Shared database across services
4. Over-engineering with microservices
5. No circuit breakers in distributed systems

## Architecture Checklist

- [ ] Clear service boundaries
- [ ] Database ownership is explicit
- [ ] API gateway strategy defined if needed
- [ ] Service discovery handled where relevant
- [ ] Resilience patterns included
- [ ] Eventing strategy defined where needed
- [ ] Health checks and tracing planned

## Resources

- **Microservices Patterns:** https://microservices.io/patterns/
- **Martin Fowler - Microservices:** https://martinfowler.com/articles/microservices.html
- **Event-Driven Architecture:** https://aws.amazon.com/event-driven-architecture/
- **CQRS Pattern:** https://martinfowler.com/bliki/CQRS.html
