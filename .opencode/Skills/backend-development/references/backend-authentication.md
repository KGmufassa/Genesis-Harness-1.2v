# Backend Authentication & Authorization

Modern authentication patterns including OAuth-aligned flows, JWT, RBAC, MFA, sessions, and API keys.

## Contents

- Use When
- Fast Rules
- OAuth And OIDC Flows
- JWT
- RBAC
- MFA
- Session Management
- Password Security
- API Key Authentication
- Authentication Decision Matrix
- Security Checklist

## Use When

- Designing login, session, token, RBAC, MFA, OAuth/OIDC, or API-key behavior
- Reviewing identity-related code for security or operational risk
- Choosing between browser sessions, bearer tokens, API keys, service credentials, and passkeys

## Fast Rules

- Verify current OAuth/OIDC, NIST, and OWASP guidance for security-sensitive work.
- Prefer established identity providers unless the product explicitly needs custom identity infrastructure.
- Keep tokens short-lived, scoped, auditable, and revocable.
- Deny by default for authorization checks.
- Use repository conventions and existing auth middleware before introducing a new auth stack.

## OAuth And OIDC Flows

Prefer OAuth 2.1-aligned authorization-code flows with PKCE where supported. OAuth 2.1 guidance has evolved through drafts and ecosystem adoption; check current primary documentation when exact standard status matters.

### Key Changes from OAuth 2.0

**Mandatory:**
- PKCE for all clients
- Exact redirect URI matching
- State parameter for CSRF protection

**Deprecated:**
- Implicit grant flow
- Resource owner password credentials grant
- Bearer token in query strings

### Authorization Code Flow with PKCE

```typescript
import crypto from 'crypto';

const codeVerifier = crypto.randomBytes(32).toString('base64url');
const codeChallenge = crypto
  .createHash('sha256')
  .update(codeVerifier)
  .digest('base64url');

const authUrl = new URL('https://auth.example.com/authorize');
authUrl.searchParams.set('client_id', 'your-client-id');
authUrl.searchParams.set('redirect_uri', 'https://app.example.com/callback');
authUrl.searchParams.set('response_type', 'code');
authUrl.searchParams.set('scope', 'openid profile email');
authUrl.searchParams.set('state', crypto.randomBytes(16).toString('hex'));
authUrl.searchParams.set('code_challenge', codeChallenge);
authUrl.searchParams.set('code_challenge_method', 'S256');

const tokenResponse = await fetch('https://auth.example.com/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'authorization_code',
    code: authCode,
    redirect_uri: redirectUri,
    client_id: clientId,
    code_verifier: codeVerifier,
  }),
});
```

## JWT (JSON Web Tokens)

### Structure

```text
Header.Payload.Signature
eyJhbGciOi...  .  eyJzdWIiOi...  .  SflKxwRJ...
```

### Best Practices

1. **Short expiration** - Access tokens 15 minutes, refresh tokens 7 days
2. **Use RS256** - Asymmetric signing
3. **Validate everything** - Signature, issuer, audience, expiration
4. **Include minimal claims**
5. **Refresh token rotation**

### Implementation

```typescript
import jwt from 'jsonwebtoken';

const accessToken = jwt.sign(
  {
    sub: user.id,
    email: user.email,
    roles: user.roles,
  },
  process.env.JWT_PRIVATE_KEY,
  {
    algorithm: 'RS256',
    expiresIn: '15m',
    issuer: 'https://api.example.com',
    audience: 'https://app.example.com',
  }
);

const decoded = jwt.verify(token, process.env.JWT_PUBLIC_KEY, {
  algorithms: ['RS256'],
  issuer: 'https://api.example.com',
  audience: 'https://app.example.com',
});
```

## Role-Based Access Control (RBAC)

### RBAC Model

```text
Users → Roles → Permissions → Resources
```

### Implementation (NestJS Example)

```typescript
export enum Role {
  ADMIN = 'admin',
  EDITOR = 'editor',
  VIEWER = 'viewer',
}

export const Roles = (...roles: Role[]) => SetMetadata('roles', roles);

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const requiredRoles = this.reflector.get<Role[]>('roles', context.getHandler());
    if (!requiredRoles) return true;

    const request = context.switchToHttp().getRequest();
    const user = request.user;

    return requiredRoles.some((role) => user.roles?.includes(role));
  }
}

@Post()
@UseGuards(JwtAuthGuard, RolesGuard)
@Roles(Role.ADMIN, Role.EDITOR)
async createPost(@Body() createPostDto: CreatePostDto) {
  return this.postsService.create(createPostDto);
}
```

### RBAC Best Practices

1. **Deny by default**
2. **Least privilege**
3. **Role hierarchy**
4. **Separate roles and permissions**
5. **Audit trail**

## Multi-Factor Authentication (MFA)

### TOTP (Time-Based One-Time Password)

```typescript
import speakeasy from 'speakeasy';
import QRCode from 'qrcode';

const secret = speakeasy.generateSecret({
  name: 'MyApp',
  issuer: 'MyCompany',
});

const qrCode = await QRCode.toDataURL(secret.otpauth_url);

const verified = speakeasy.totp.verify({
  secret: secret.base32,
  encoding: 'base32',
  token: userToken,
  window: 2,
});
```

### FIDO2/WebAuthn And Passkeys

**Benefits:**
- Phishing-resistant
- No shared secrets
- Hardware-backed security
- Better UX

**Implementation:**
```typescript
const publicKeyCredentialCreationOptions = {
  challenge: crypto.randomBytes(32),
  rp: { name: 'MyApp', id: 'example.com' },
  user: {
    id: Buffer.from(user.id),
    name: user.email,
    displayName: user.name,
  },
  pubKeyCredParams: [{ alg: -7, type: 'public-key' }],
  authenticatorSelection: {
    authenticatorAttachment: 'platform',
    userVerification: 'required',
  },
  timeout: 60000,
  attestation: 'direct',
};

import { verifyRegistrationResponse, verifyAuthenticationResponse } from '@simplewebauthn/server';
```

## Session Management

### Best Practices

1. **Secure cookies**
2. **Session timeout**
3. **Regenerate session ID**
4. **Server-side storage**
5. **CSRF protection**

### Implementation

```typescript
import session from 'express-session';
import RedisStore from 'connect-redis';
import { createClient } from 'redis';

const redisClient = createClient();
await redisClient.connect();

app.use(
  session({
    store: new RedisStore({ client: redisClient }),
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
      secure: true,
      httpOnly: true,
      sameSite: 'strict',
      maxAge: 1000 * 60 * 15,
    },
  })
);
```

## Password Security

### Argon2id

Prefer Argon2id for new password hashing when available. Existing bcrypt deployments can remain acceptable when configured with an appropriate cost and a migration plan exists for future rehashing.

**Why Argon2id:**
- Memory-hard
- Resistant to GPU and ASIC attacks
- Configurable CPU and memory cost

```typescript
import argon2 from 'argon2';

const hash = await argon2.hash('password123', {
  type: argon2.argon2id,
  memoryCost: 65536,
  timeCost: 3,
  parallelism: 4,
});

const valid = await argon2.verify(hash, 'password123');
```

### Password Policy

- **Minimum length:** 12 characters
- **No composition rules**
- **Check against breach databases**
- **No periodic rotation**
- **Allow all printable characters**

## API Key Authentication

### Best Practices

1. **Prefix keys**
2. **Hash stored keys**
3. **Key rotation**
4. **Scope limiting**
5. **Rate limiting**

```typescript
const apiKey = `sk_${env}_${crypto.randomBytes(24).toString('base64url')}`;

const hashedKey = crypto.createHash('sha256').update(apiKey).digest('hex');
await db.apiKeys.create({ userId, hashedKey, scopes: ['read'] });

const providedHash = crypto.createHash('sha256').update(providedKey).digest('hex');
const keyRecord = await db.apiKeys.findOne({ hashedKey: providedHash });
```

## Authentication Decision Matrix

| Use Case | Recommended Approach |
|----------|---------------------|
| Web application | Server-side session or OAuth/OIDC authorization code flow |
| Mobile app | OAuth/OIDC authorization code flow with PKCE |
| SPA | OAuth/OIDC authorization code flow with PKCE; avoid storing long-lived tokens in browser storage |
| Server-to-server | Client credentials grant + mTLS |
| Third-party API access | API keys with scopes |
| High-security | WebAuthn/FIDO2 + MFA |
| Internal admin | JWT + RBAC + MFA |
| Microservices | Service mesh (mTLS) + JWT |

## Security Checklist

- [ ] OAuth/OIDC flow uses PKCE where appropriate
- [ ] Access tokens are short-lived and refresh tokens are rotated where used
- [ ] RBAC with deny-by-default
- [ ] MFA required for admin accounts
- [ ] Passwords hashed with Argon2id
- [ ] Session cookies: HttpOnly, Secure, SameSite
- [ ] Rate limiting on auth endpoints
- [ ] Account lockout after failed attempts
- [ ] Password policy: 12+ chars, breach check
- [ ] Audit logging for authentication events

## Resources

- **OAuth 2.1:** https://oauth.net/2.1/
- **JWT Best Practices:** https://datatracker.ietf.org/doc/html/rfc8725
- **WebAuthn:** https://webauthn.guide/
- **NIST Password Guidelines:** https://pages.nist.gov/800-63-3/
- **OWASP Auth Cheat Sheet:** https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
