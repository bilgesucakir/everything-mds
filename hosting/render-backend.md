---
domain: backend, ops
part: stack-rules
summary: Small Spring Boot API on Render with Atlas, R2 and Brevo email, and operating lessons
adapt: Stack-specific (Java, Atlas, R2, Brevo). Take section 3 'Operations lessons' if using Render; skip 1-2 otherwise.
---

# Backend on Render with Atlas, R2 and email: what we run and what it costs to watch

A small Java (Spring Boot) API for a mobile app, run as one service. This describes the setup and the operating lessons, without secrets. Replace the names with your own.

Last verified: 2026-10-18.

## 1. The pieces
<!-- tags: part=reference -->

| Piece | Service | Notes |
|---|---|---|
| API | **Render** web service (Docker), one fixed-price instance, region close to your users | Health check path `/actuator/health`; auto-deploy on every push to the deploy branch |
| Database | **MongoDB Atlas** | A paid tier gives automatic daily backups; the free tier has none |
| Photo storage | **Cloudflare R2** (private bucket) or the database (GridFS) | A setting chooses where *new* photos go; old ones stay readable |
| Email | **Brevo** (SMTP) | Free plan has a daily send limit; the app also caps mail per day |
| Uptime | **Better Stack** | Free plan: one monitor on the health endpoint; email alerts only |

## 2. Configuration rules
<!-- tags: part=stack-rules -->

- A `render.yaml` ("Blueprint") describes the service. Secrets are marked `sync: false` so their values are **never in the file or in git**; set them in the Render dashboard.
- Generate the JWT signing secret once (`generateValue: true`) and keep it stable across deploys.
- The server **refuses to start** with a development secret on a real host (see `checklists/login-security-checklist.md`).
- Settings that choose behaviour (`UPLOAD_STORAGE`, migration flags) are set in the dashboard, not in the file, so a Blueprint sync never resets them.
- One variable holds the service's own public URL; it is baked into email links, so update it if the assigned URL differs.
- A mail sender address must be one your SMTP provider is allowed to send from (verify the domain with SPF/DKIM first).

## 3. Operations lessons
<!-- tags: part=conventions; domain=ops, backend -->

- **Auto-deploy on merge means a merge is a deploy.** While an app is in store review, do not merge backend changes: the reviewer uses the live API.
- **Render has no spending cap.** Keep one fixed-price instance and check the billing page and bandwidth emails weekly.
- **Backups:** decide where they are and test a restore; the free database tier has none.
- **Billing alerts** on every paid service (database, object storage, hosting) so a bug or attack cannot become a bill.
- **Migrations that copy data** (database to R2): default off, dry run first, never delete the source.
- **Monitoring:** one monitor on the health endpoint; add alerts on spikes of failed logins and 429 responses.
- **Cold starts:** a service that sleeps makes the first request slow; use an always-on instance for anything a reviewer or user must reach quickly.
- **Is the API behind Cloudflare?** Here it was not (the app calls the Render address). Read `cloudflare-workers-and-domains.md` section 5 for what that means for rate limits.
