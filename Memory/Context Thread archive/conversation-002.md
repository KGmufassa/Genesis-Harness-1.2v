# Conversation 002

Follow-up conversation about feature implementation.

## Updates

We added user authentication feature. This is a new feature.

## Decisions

We decided to use JWT for authentication. Final decision.

## Knowledge

We learned that JWT tokens need refresh rotation.

## Problems

Error: token expiry too short. Fixed by increasing to 24 hours.

## Preferences

Prefer short-lived access tokens with refresh tokens.
