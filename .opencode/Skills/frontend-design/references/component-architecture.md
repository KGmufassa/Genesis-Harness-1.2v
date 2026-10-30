# Component Architecture

Use this file when structuring components, splitting responsibilities, or deciding how UI code should be organized.

## File Structure

Colocate everything related to a component.

```text
src/components/
  TaskList/
    TaskList.tsx
    TaskList.test.tsx
    TaskList.stories.tsx
    use-task-list.ts
    types.ts
```

Use this structure when the component has meaningful local complexity. Do not create extra files for trivial components.

## Prefer Composition Over Configuration

**Good:**
```tsx
<Card>
  <CardHeader>
    <CardTitle>Tasks</CardTitle>
  </CardHeader>
  <CardBody>
    <TaskList tasks={tasks} />
  </CardBody>
</Card>
```

**Avoid:**
```tsx
<Card
  title="Tasks"
  headerVariant="large"
  bodyPadding="md"
  content={<TaskList tasks={tasks} />}
/>
```

Use composition when:
- the layout should stay flexible
- consumers need structural control
- configuration props are starting to multiply

## Keep Components Focused

Prefer components that do one clear job.

```tsx
export function TaskItem({ task, onToggle, onDelete }: TaskItemProps) {
  return (
    <li className="flex items-center gap-3 p-3">
      <Checkbox checked={task.done} onChange={() => onToggle(task.id)} />
      <span className={task.done ? 'line-through text-muted' : ''}>{task.title}</span>
      <Button variant="ghost" size="sm" onClick={() => onDelete(task.id)}>
        <TrashIcon />
      </Button>
    </li>
  );
}
```

Split components when:
- they exceed a reasonable mental unit
- they mix unrelated responsibilities
- they become difficult to test or restyle

## Separate Data Fetching From Presentation

Use container/presentation separation when async data or state complexity would otherwise pollute the rendering component.

```tsx
export function TaskListContainer() {
  const { tasks, isLoading, error } = useTasks();

  if (isLoading) return <TaskListSkeleton />;
  if (error) return <ErrorState message="Failed to load tasks" retry={refetch} />;
  if (tasks.length === 0) return <EmptyState message="No tasks yet" />;

  return <TaskList tasks={tasks} />;
}

export function TaskList({ tasks }: { tasks: Task[] }) {
  return (
    <ul role="list" className="divide-y">
      {tasks.map(task => <TaskItem key={task.id} task={task} />)}
    </ul>
  );
}
```

## Output Expectation

When using this reference, specify:
- component boundaries
- whether composition is preferred over prop configuration
- where data handling lives
- which pieces are reusable primitives vs feature components
