# Backend API Design

Use this file as the entry point for API design work. Load only the narrower reference that matches the task.

## Read This First For

- deciding between REST, GraphQL, and gRPC
- routing API design work to the right detailed reference
- checking API-wide security and documentation requirements

## Reference Routing

- REST resource design, status codes, payloads, pagination, filtering, versioning:
  `references/backend-api-rest.md`
- GraphQL schema design, queries, mutations, resolvers, N+1 prevention:
  `references/backend-api-graphql.md`
- gRPC schemas, implementation shape, internal-service tradeoffs:
  `references/backend-api-grpc.md`

## API-Wide Decision Matrix

| Feature | REST | GraphQL | gRPC |
|---------|------|---------|------|
| **Use Case** | Public APIs, CRUD | Flexible data fetching | Microservices, performance |
| **Performance** | Moderate | Moderate | Fastest (7-10x REST) |
| **Caching** | HTTP caching built-in | Complex | No built-in caching |
| **Browser Support** | Native | Native | Requires gRPC-Web |
| **Learning Curve** | Easy | Moderate | Steep |
| **Streaming** | Limited (SSE) | Subscriptions | Bi-directional |
| **Tooling** | Excellent | Excellent | Good |
| **Documentation** | OpenAPI/Swagger | Schema introspection | Protobuf definition |

## API Security Checklist

- [ ] HTTPS/TLS only
- [ ] Authentication in place
- [ ] Authorization checks enforced
- [ ] Rate limiting configured
- [ ] Input validation on all endpoints
- [ ] CORS configured properly
- [ ] Security headers configured
- [ ] Versioning implemented
- [ ] Error messages do not leak internals
- [ ] Audit logging enabled

## Documentation Baseline

For REST, use OpenAPI/Swagger. For GraphQL, rely on schema introspection plus examples. For gRPC, treat protobuf definitions as contracts.

## Resources

- **REST Best Practices:** https://restfulapi.net/
- **GraphQL:** https://graphql.org/learn/
- **gRPC:** https://grpc.io/docs/
- **OpenAPI:** https://swagger.io/specification/
