# Backend Design Patterns

## Repository Pattern

Use to separate business logic from persistence concerns.

```typescript
interface UserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<void>;
}
```

## Factory Pattern

Use when callers should not know concrete class construction details.

## Decorator Pattern

Use to add behavior around an object without changing the original implementation.

## Observer Pattern

Use for event publication and subscriber notification.

```typescript
class EventEmitter {
  private observers: Map<string, Observer[]> = new Map();
}
```
