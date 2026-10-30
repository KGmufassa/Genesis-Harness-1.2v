# REST API Design

## Contents

- Resource-Based URLs
- HTTP Status Codes
- Request/Response Format
- Pagination
- Filtering And Sorting
- Versioning Strategies
- Documentation

## Resource-Based URLs

**Good:**
```text
GET    /api/v1/users
GET    /api/v1/users/:id
POST   /api/v1/users
PUT    /api/v1/users/:id
PATCH  /api/v1/users/:id
DELETE /api/v1/users/:id

GET    /api/v1/users/:id/posts
POST   /api/v1/users/:id/posts
```

**Bad:**
```text
GET /api/v1/getUser?id=123
POST /api/v1/createUser
GET /api/v1/user-posts
```

## HTTP Status Codes

**Success:**
- `200 OK`
- `201 Created`
- `204 No Content`

**Client errors:**
- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `409 Conflict`
- `422 Unprocessable Entity`
- `429 Too Many Requests`

**Server errors:**
- `500 Internal Server Error`
- `502 Bad Gateway`
- `503 Service Unavailable`
- `504 Gateway Timeout`

## Request/Response Format

**Request:**
```typescript
POST /api/v1/users
Content-Type: application/json

{
  "email": "user@example.com",
  "name": "John Doe",
  "age": 30
}
```

**Success response:**
```typescript
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/v1/users/123

{
  "id": "123",
  "email": "user@example.com",
  "name": "John Doe",
  "age": 30,
  "createdAt": "2025-01-09T12:00:00Z",
  "updatedAt": "2025-01-09T12:00:00Z"
}
```

**Error response:**
```typescript
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format",
        "value": "invalid-email"
      }
    ],
    "timestamp": "2025-01-09T12:00:00Z",
    "path": "/api/v1/users"
  }
}
```

## Pagination

```typescript
GET /api/v1/users?page=2&limit=50

{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 50,
    "total": 1234,
    "totalPages": 25,
    "hasNext": true,
    "hasPrev": true
  },
  "links": {
    "first": "/api/v1/users?page=1&limit=50",
    "prev": "/api/v1/users?page=1&limit=50",
    "next": "/api/v1/users?page=3&limit=50",
    "last": "/api/v1/users?page=25&limit=50"
  }
}
```

## Filtering and Sorting

```text
GET /api/v1/users?status=active&role=admin&sort=-createdAt,name&limit=20
```

## Versioning Strategies

**URL versioning:**
```text
/api/v1/users
/api/v2/users
```

**Header versioning:**
```text
Accept: application/vnd.myapi.v2+json
```

**Recommendation:** URL versioning for simplicity and discoverability.

## Documentation

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /api/v1/users:
    get:
      summary: List users
```
