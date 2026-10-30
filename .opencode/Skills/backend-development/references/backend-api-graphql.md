# GraphQL API Design

## Contents

- Schema Definition
- Queries
- Mutations
- Resolvers
- Best Practices
- DataLoader Example

## Schema Definition

```graphql
type User {
  id: ID!
  email: String!
  name: String!
  posts: [Post!]!
  createdAt: DateTime!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  published: Boolean!
  createdAt: DateTime!
}

type Query {
  user(id: ID!): User
  users(limit: Int = 50, offset: Int = 0): [User!]!
  post(id: ID!): Post
  posts(authorId: ID, published: Boolean): [Post!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
}
```

## Queries

```graphql
query {
  user(id: "123") {
    id
    name
    email
    posts {
      id
      title
      published
    }
  }
}

query GetUser($userId: ID!) {
  user(id: $userId) {
    id
    name
  }
}
```

## Mutations

```graphql
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    email
    name
    createdAt
  }
}
```

## Resolvers (NestJS Example)

```typescript
@Resolver(() => User)
export class UserResolver {
  constructor(
    private userService: UserService,
    private postService: PostService,
  ) {}

  @Query(() => User, { nullable: true })
  async user(@Args('id') id: string) {
    return this.userService.findById(id);
  }

  @ResolveField(() => [Post])
  async posts(@Parent() user: User) {
    return this.postService.findByAuthorId(user.id);
  }
}
```

## Best Practices

1. Avoid N+1 with DataLoader.
2. Use cursor pagination where collections are large.
3. Return structured errors.
4. Limit query depth.
5. Enforce query complexity limits.

## DataLoader Example

```typescript
import DataLoader from 'dataloader';

const postLoader = new DataLoader(async (authorIds: string[]) => {
  const posts = await db.posts.findAll({ where: { authorId: authorIds } });
  return authorIds.map(id => posts.filter(p => p.authorId === id));
});
```
