# gRPC API Design

## Protocol Buffers Schema

```protobuf
syntax = "proto3";

package user;

service UserService {
  rpc GetUser (GetUserRequest) returns (User);
  rpc ListUsers (ListUsersRequest) returns (ListUsersResponse);
  rpc CreateUser (CreateUserRequest) returns (User);
  rpc StreamUsers (StreamUsersRequest) returns (stream User);
}

message User {
  string id = 1;
  string email = 2;
  string name = 3;
  int64 created_at = 4;
}
```

## Implementation (Node.js)

```typescript
import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';

const packageDefinition = protoLoader.loadSync('user.proto');
const userProto = grpc.loadPackageDefinition(packageDefinition).user;
const server = new grpc.Server();

server.addService(userProto.UserService.service, {
  async getUser(call, callback) {
    const user = await userService.findById(call.request.id);
    callback(null, user);
  },

  async streamUsers(call) {
    const users = await userService.findAll();
    for (const user of users) {
      call.write(user);
    }
    call.end();
  },
});
```

## Benefits

- Binary protocol with high performance
- Strong typing through protobuf
- Client/server code generation
- Streaming support

## Best Fit

Use gRPC for:
- internal service-to-service traffic
- high-throughput systems
- strongly typed contracts
- streaming-heavy internal platforms
