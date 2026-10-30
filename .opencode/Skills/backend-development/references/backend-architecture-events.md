# Event-Driven Architecture Patterns

## Event Sourcing

Store events instead of only current state.

Benefits:
- audit trail
- replay capability
- temporal inspection
- flexible projections

```typescript
const balance = events
  .filter(e => e.userId === '123')
  .reduce((acc, event) => {
    if (event.type === 'MoneyDeposited') return acc + event.amount;
    if (event.type === 'MoneyWithdrawn') return acc - event.amount;
    return acc;
  }, 0);
```

## Message Broker Patterns

### Kafka

Use for:
- event streaming
- replayable event logs
- high-throughput analytics

```typescript
import { Kafka } from 'kafkajs';
```

### RabbitMQ

Use for:
- task queues
- request/reply style messaging
- work dispatch with acknowledgements

```typescript
import amqp from 'amqplib';
```

## CQRS

Separate read and write models when:
- read patterns differ from write patterns
- read scaling needs are much higher
- denormalized read models improve latency

```typescript
class CreateOrderCommand {}
class GetOrderQuery {}
```
