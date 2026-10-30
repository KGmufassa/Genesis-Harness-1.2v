# Backend Scaling Patterns

## Horizontal Scaling

Scale out with multiple application instances behind a load balancer.

Use when:
- traffic is high
- redundancy matters
- the app can be made stateless

## Database Sharding

Strategies:
- range-based
- hash-based
- geographic
- entity-based

```typescript
function getShardId(userId: string): number {
  const hash = crypto.createHash('md5').update(userId).digest('hex');
  return parseInt(hash.substring(0, 8), 16) % SHARD_COUNT;
}
```

## Caching Layers

```text
Client
  → CDN
  → API Gateway Cache
  → Application Cache
  → Database Query Cache
  → Database
```

Use layered caching when the same data is repeatedly requested across multiple system levels.
