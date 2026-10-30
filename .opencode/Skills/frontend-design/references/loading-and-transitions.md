# Loading And Transitions

Use this file when defining skeletons, optimistic updates, or transition behavior.

## Loading States

Prefer skeletons for content loading over generic spinners when content structure is known.

```tsx
function TaskListSkeleton() {
  return (
    <div className="space-y-3" aria-busy="true" aria-label="Loading tasks">
      {Array.from({ length: 3 }).map((_, i) => (
        <div key={i} className="h-12 bg-muted animate-pulse rounded" />
      ))}
    </div>
  );
}
```

## Optimistic Updates

Use optimistic updates when the action is common, reversible, and the user benefits from immediate feedback.

```tsx
function useToggleTask() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: toggleTask,
    onMutate: async (taskId) => {
      await queryClient.cancelQueries({ queryKey: ['tasks'] });
      const previous = queryClient.getQueryData(['tasks']);

      queryClient.setQueryData(['tasks'], (old: Task[]) =>
        old.map(t => t.id === taskId ? { ...t, done: !t.done } : t)
      );

      return { previous };
    },
    onError: (_err, _taskId, context) => {
      queryClient.setQueryData(['tasks'], context?.previous);
    },
  });
}
```

## Transition Rules

- transitions should reinforce state change, not decorate idleness
- prefer restrained motion on dense application surfaces
- use skeletons, optimistic updates, and small transitions together only when they improve comprehension

## Output Expectation

When using this reference, specify:
- loading-state style
- whether optimistic updates are appropriate
- transition intensity and purpose
