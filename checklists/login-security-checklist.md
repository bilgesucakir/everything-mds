# Login and API security checklist

For an app with email-and-password accounts and a token-based API. It is a review aid, not a guarantee: it does not replace testing by someone independent.

## 1. Order of work on the login endpoint (cheap first, expensive last)

1. Global per-IP request limit (in memory, almost free).
2. Input validation: required fields, formats, **maximum lengths** (also for the password).
3. Login rate limit: per account **and** per IP.
4. Database lookup.
5. Password hash check (bcrypt, argon2) – the expensive step.
6. Extra checks (verified email, locked account), then issue tokens.

Add a **concurrency cap** around the password check: many different IPs, each below its own limit, can still use up the CPU. Over the cap, answer quickly with 429 or 503.

## 2. Hiding information

- Same message for "unknown email" and "wrong password".
- Same **timing** for both: for an unknown email, run a dummy hash check against a fixed hash.
- Forgot-password and resend-email answer the same way whether the email exists or not.

## 3. Client IP and rate limits

- Only trust headers set by **your own proxy**. If the API is reachable directly (not only through the CDN), a client can send any `CF-Connecting-IP` or `X-Forwarded-For` value and get a new limit on every request.
- Per-account limits do not depend on the IP; keep them.
- Know where counters live. In memory means they reset on restart and are per instance. Make sure old entries are cleaned up.
- Never lock an account hard after a few failures (an attacker can lock out a victim); slow down instead and notify the owner.

## 4. Tokens

- Signature required and verified; reject unsigned ("none") tokens.
- Secret is long (32 bytes or more), comes from the environment, and the server **refuses to start** with a development default on a real host.
- Short-lived access token; refresh tokens are random, stored **hashed**, rotated on use, and revoked on logout, password change and account deletion.
- On every request, load the user from the database: deleted or unverified accounts lose access at once, the **role comes from the database**, not from the token.
- A token version (or similar) invalidates old tokens after a password change or "log out everywhere".

## 5. Authorization

- Default deny: everything needs a login unless it is in a short public list.
- Every endpoint that takes an id (`/users/{id}`, `/items/{id}`) checks that the object belongs to the caller, or the caller is an admin (insecure direct object reference).
- Admin endpoints require the admin role **on the server**; hiding buttons in the app is not protection.
- The sign-up request cannot set a role or other privileged fields.
- Public file URLs (for example photos) rely on long random names: say so in the privacy policy, or put them behind signed URLs.

## 6. Password reset and email

- Reset codes: random, stored hashed, expire quickly, single use, locked after a few wrong tries, with their own rate limits.
- Resetting revokes existing sessions.
- Verification links and codes are single use and expire.
- Password rules enforced on the **server** (length, letter and number), plus a check against leaked passwords if you can.

## 7. Everything else on the surface

- API docs and admin panel files are public by default in many frameworks: decide if they should be.
- CORS lists only the origins you need; no credentials unless required.
- Security headers on the admin panel (content security policy, no framing).
- No secrets in the repository or its history; scan the history before making a repo public.
- Monitoring: alert on spikes of failed logins and 429 responses; a status check on the health endpoint.
- Spending caps on every paid service so an attack cannot become a bill.

## 8. Manual tests worth running (against a test account)

- Call protected endpoints with no token, an expired token, an old token after a password change, and a token for another user's id.
- Try the sign-up request with an extra `role` field.
- Send login requests with faked IP headers and watch the limits.
- Send a very long password.
- Compare response times for a known and an unknown email.
