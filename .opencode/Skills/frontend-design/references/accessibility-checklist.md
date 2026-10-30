# Accessibility Checklist

Use this file when implementing or reviewing accessible frontend behavior.

## Keyboard Navigation

Every interactive element must be keyboard accessible.

```tsx
<button onClick={handleClick}>Click me</button>
```

Prefer semantic interactive elements over recreating them with generic containers.

## ARIA Labels

Label interactive elements that lack visible text.

```tsx
<button aria-label="Close dialog"><XIcon /></button>
```

Label form inputs with explicit labels or appropriate ARIA when no visible label exists.

## Focus Management

Move focus intentionally when UI state changes, especially for dialogs, drawers, and dynamic content.

```tsx
useEffect(() => {
  if (isOpen) closeRef.current?.focus();
}, [isOpen]);
```

## Meaningful Empty And Error States

Do not show blank surfaces.

```tsx
<div role="status" className="text-center py-12">
  <h3 className="mt-2 text-sm font-medium">No tasks</h3>
  <p className="mt-1 text-sm text-muted">Get started by creating a new task.</p>
</div>
```

## Verification Checklist

- [ ] all interactive elements are keyboard accessible
- [ ] labels are present and meaningful
- [ ] focus is managed for dialogs and dynamic UI
- [ ] loading, error, and empty states communicate clearly
- [ ] color is not the sole indicator of meaning
- [ ] contrast meets the required baseline

## Output Expectation

When using this reference, specify:
- keyboard risks
- labeling gaps
- focus-management needs
- empty/error/loading accessibility requirements
