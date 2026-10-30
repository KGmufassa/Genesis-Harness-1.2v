# Backend Debugging Strategies

Comprehensive debugging techniques, tools, and best practices for backend systems.

## Contents

- Debugging Mindset
- Logging Best Practices
- Debugging Tools By Language
- Database Debugging
- API Debugging
- Performance Debugging
- Production Debugging
- Common Debugging Scenarios
- Debugging Checklist

## Debugging Mindset

### The Scientific Method for Debugging

1. **Observe** - Gather symptoms and data
2. **Hypothesize** - Form theories about the cause
3. **Test** - Verify or disprove theories
4. **Iterate** - Refine understanding
5. **Fix** - Apply solution
6. **Verify** - Confirm fix works

### Golden Rules

1. **Reproduce first**
2. **Simplify the problem**
3. **Read the logs**
4. **Check assumptions**
5. **Use scientific method**
6. **Document findings**

## Logging Best Practices

### Structured Logging

**Node.js (Pino):**
```typescript
import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  transport: {
    target: 'pino-pretty',
    options: { colorize: true }
  }
});

logger.info({ userId: '123', action: 'login' }, 'User logged in');

try {
  await riskyOperation();
} catch (error) {
  logger.error({ err: error, userId: '123' }, 'Operation failed');
}
```

**Python (Structlog):**
```python
import structlog

logger = structlog.get_logger()
logger.info("user_login", user_id="123", ip="192.168.1.1")
```

**Go (Zap):**
```go
logger, _ := zap.NewProduction()
defer logger.Sync()

logger.Info("user logged in",
    zap.String("user_id", "123"),
    zap.String("ip", "192.168.1.1"),
)
```

### Log Levels

| Level | Purpose | Example |
|-------|---------|---------|
| **TRACE** | Very detailed, dev only | Request bodies |
| **DEBUG** | Detailed info for debugging | SQL queries |
| **INFO** | General informational | User login |
| **WARN** | Potential issues | Deprecated API usage |
| **ERROR** | Error conditions | Failed API calls |
| **FATAL** | Critical failures | Database lost |

### What to Log

**Do log:**
- Request and response metadata
- Error messages with context
- Performance metrics
- Security events
- Business events

**Do not log:**
- Passwords or secrets
- Credit card numbers
- PII when avoidable
- Session tokens
- Full request bodies in production

## Debugging Tools by Language

### Node.js / TypeScript

```bash
node --inspect-brk app.js
```

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Server",
      "skipFiles": ["<node_internals>/**"],
      "program": "${workspaceFolder}/src/index.ts",
      "preLaunchTask": "npm: build",
      "outFiles": ["${workspaceFolder}/dist/**/*.js"]
    }
  ]
}
```

```typescript
import debug from 'debug';

const log = debug('app:server');
const error = debug('app:error');
```

### Python

```python
import pdb

def problematic_function(data):
    pdb.set_trace()
    result = process(data)
    return result
```

### Go

```bash
go install github.com/go-delve/delve/cmd/dlv@latest
dlv debug main.go
```

### Rust

```bash
cargo build
rust-lldb ./target/debug/myapp
```

## Database Debugging

### SQL Query Debugging (PostgreSQL)

```sql
EXPLAIN ANALYZE
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.name
ORDER BY order_count DESC
LIMIT 10;
```

```sql
ALTER DATABASE mydb SET log_min_duration_statement = 1000;

SELECT query, calls, total_exec_time, mean_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

### MongoDB Debugging

```javascript
db.users.find({ email: 'test@example.com' }).explain('executionStats')
db.setProfilingLevel(1, { slowms: 100 })
db.system.profile.find().limit(5).sort({ ts: -1 }).pretty()
```

### Redis Debugging

```bash
redis-cli MONITOR
redis-cli SLOWLOG GET 10
redis-cli INFO memory
```

## API Debugging

### HTTP Request Debugging

```bash
curl -v https://api.example.com/users
curl -i https://api.example.com/users
http GET https://api.example.com/users
```

```typescript
app.use(morgan(':method :url :status :response-time ms - :res[content-length]'));
```

```python
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info("request_processed", method=request.method, path=request.url.path, status_code=response.status_code, duration_ms=duration * 1000)
    return response
```

## Performance Debugging

### CPU Profiling

```bash
0x node app.js
clinic doctor -- node app.js
```

```python
import cProfile
import pstats
```

```go
import (
    "net/http"
    _ "net/http/pprof"
)
```

### Memory Debugging

```typescript
import { writeHeapSnapshot } from 'v8';
```

```python
from memory_profiler import profile
```

## Production Debugging

### Application Performance Monitoring (APM)

```typescript
import 'newrelic';
import tracer from 'dd-trace';
import * as Sentry from '@sentry/node';
```

### Distributed Tracing

```typescript
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';
```

### Log Aggregation

```yaml
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
```

## Common Debugging Scenarios

### 1. High CPU Usage

```typescript
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

### 2. Memory Leaks

```typescript
class DataService {
  constructor(eventBus) {
    this.eventBus = eventBus;
    this.handler = (data) => this.processData(data);
    eventBus.on('data', this.handler);
  }

  destroy() {
    this.eventBus.off('data', this.handler);
  }
}
```

### 3. Slow Database Queries

```sql
CREATE INDEX idx_orders_user_id_created_at
ON orders(user_id, created_at DESC);
```

### 4. Connection Pool Exhaustion

```typescript
async function getUser(id) {
  const result = await pool.query('SELECT * FROM users WHERE id = $1', [id]);
  return result.rows[0];
}
```

### 5. Race Conditions

```typescript
async function incrementCounter() {
  return await redis.incr('counter');
}
```

## Debugging Checklist

- [ ] Read error message completely
- [ ] Check logs for context
- [ ] Reproduce the issue reliably
- [ ] Isolate the problem
- [ ] Verify assumptions
- [ ] Enable debug logging
- [ ] Add strategic log points
- [ ] Use debugger breakpoints
- [ ] Profile performance if slow
- [ ] Add regression test after fix

## Debugging Resources

- Node.js: https://nodejs.org/en/docs/guides/debugging-getting-started/
- Chrome DevTools: https://developer.chrome.com/docs/devtools/
- Clinic.js: https://clinicjs.org/
- Sentry: https://docs.sentry.io/
- DataDog: https://docs.datadoghq.com/
- New Relic: https://docs.newrelic.com/
