# Backend Performance & Scalability

Performance optimization strategies, caching patterns, and scalability practices.

## Contents

- Use When
- Fast Rules
- Database Performance
- Caching Strategies
- Load Balancing
- Asynchronous Processing
- CDN
- Scaling
- Database Scaling Patterns
- Performance Monitoring
- Optimization Checklist
- Common Pitfalls

## Use When

- Investigating slow queries, latency, throughput, resource saturation, caching, pooling, or scaling
- Reviewing performance-sensitive backend changes
- Choosing where to measure and optimize

## Fast Rules

- Measure before optimizing unless the bug is obvious.
- Fix query shape, indexes, pooling, and unbounded work before adding distributed systems.
- Add caching only with an invalidation strategy and observability for hit rate and stale data.
- Treat numeric impact claims as workload-dependent; benchmark in the target environment.

## Database Performance

### Query Optimization

#### Indexing Strategies

Indexes can remove table scans and dramatically improve query latency when they match real query patterns.

```sql
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);
CREATE INDEX idx_active_users ON users(email) WHERE active = true;
```

**Index Types:**
- **B-tree**
- **Hash**
- **GIN**
- **GiST**

### Connection Pooling

Connection pooling reduces connection overhead and protects the database from unbounded client concurrency.

```typescript
import { Pool } from 'pg';

const pool = new Pool({
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});
```

### N+1 Query Problem

```typescript
const posts = await Post.findAll({
  include: [{ model: User, as: 'author' }],
});
```

## Caching Strategies

### Redis Caching

#### Cache-Aside Pattern

```typescript
async function getUser(userId: string) {
  const cached = await redis.get(`user:${userId}`);
  if (cached) return JSON.parse(cached);

  const user = await db.users.findById(userId);
  await redis.setex(`user:${userId}`, 3600, JSON.stringify(user));
  return user;
}
```

#### Write-Through Pattern

```typescript
async function updateUser(userId: string, data: UpdateUserDto) {
  const user = await db.users.update(userId, data);
  await redis.setex(`user:${userId}`, 3600, JSON.stringify(user));
  return user;
}
```

#### Cache Invalidation

```typescript
async function deleteUser(userId: string) {
  await db.users.delete(userId);
  await redis.del(`user:${userId}`);
  await redis.del(`user:${userId}:posts`);
}
```

### Cache Best Practices

1. Cache frequently accessed data
2. Set appropriate TTL
3. Invalidate on write
4. Use predictable cache key patterns
5. Monitor hit rates

## Load Balancing

### Algorithms

```nginx
upstream backend {
    least_conn;
    server backend1.example.com;
    server backend2.example.com;
}
```

### Health Checks

```typescript
app.get('/health', async (req, res) => {
  const checks = {
    uptime: process.uptime(),
    timestamp: Date.now(),
    database: await checkDatabase(),
    redis: await checkRedis(),
    memory: process.memoryUsage(),
  };

  const isHealthy = checks.database && checks.redis;
  res.status(isHealthy ? 200 : 503).json(checks);
});
```

## Asynchronous Processing

### Message Queues for Long-Running Tasks

```typescript
import Queue from 'bull';

const emailQueue = new Queue('email', {
  redis: { host: 'localhost', port: 6379 },
});

await emailQueue.add('send-welcome', {
  userId: user.id,
  email: user.email,
});
```

## CDN (Content Delivery Network)

```typescript
res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
res.setHeader('Cache-Control', 'public, max-age=3600');
res.setHeader('Cache-Control', 'private, no-cache');
```

## Horizontal vs Vertical Scaling

### Horizontal Scaling (Scale Out)

Use for high traffic, redundancy, and stateless applications.

### Vertical Scaling (Scale Up)

Use for simpler architectures where consistency is critical.

## Database Scaling Patterns

### Read Replicas

```typescript
await primaryDb.users.create(userData);
const users = await replicaDb.users.findAll();
```

### Database Sharding

```typescript
function getShardId(userId: string): number {
  return hashCode(userId) % SHARD_COUNT;
}
```

## Performance Monitoring

### Key Metrics

**Application:**
- Response time
- Throughput
- Error rate
- CPU and memory usage

**Database:**
- Query execution time
- Connection saturation
- Cache hit rate
- Slow query log

## Performance Optimization Checklist

- [ ] Indexes on frequently queried columns
- [ ] Connection pooling configured
- [ ] N+1 queries eliminated
- [ ] Slow query log monitored
- [ ] Redis cache for hot data
- [ ] Cache invalidation on writes
- [ ] CDN for static assets
- [ ] Async processing for long tasks
- [ ] Load balancing configured
- [ ] APM and dashboards configured

## Common Performance Pitfalls

1. No caching
2. Missing indexes
3. N+1 queries
4. Synchronous long tasks
5. No connection pooling
6. Unbounded queries
7. No CDN

## Resources

- **PostgreSQL Performance:** https://www.postgresql.org/docs/current/performance-tips.html
- **Redis Best Practices:** https://redis.io/docs/management/optimization/
- **Web Performance:** https://web.dev/performance/
- **Database Indexing:** https://use-the-index-luke.com/
