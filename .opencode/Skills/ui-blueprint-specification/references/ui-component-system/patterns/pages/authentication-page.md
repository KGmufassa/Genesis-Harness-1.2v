---
pattern_id: authentication-page
pattern_type: page
aliases: [login, signup, password-reset]
use_when: [identity access, account entry, credential recovery]
avoid_when: [authenticated app workspace]
requires: [form states, validation, security messaging]
---

# Page Pattern — authentication-page

Use for login, signup, reset password, verification, or session recovery.

Preferred layout: `single-column`.

Requires validation, error, loading, success, and security-sensitive feedback behavior.
