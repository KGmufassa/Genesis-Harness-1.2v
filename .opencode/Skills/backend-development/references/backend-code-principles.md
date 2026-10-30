# Backend Code Principles

## SOLID Principles

### Single Responsibility Principle

A class or module should have one reason to change.

### Open/Closed Principle

Extend behavior without modifying existing decision-heavy code.

### Liskov Substitution Principle

Subtypes must honor base expectations and not break callers.

### Interface Segregation Principle

Prefer smaller interfaces so implementations do not depend on methods they do not use.

### Dependency Inversion Principle

Depend on abstractions, not concrete infrastructure choices.

```typescript
interface Database {
  query(sql: string, params: any[]): Promise<any>;
}
```
