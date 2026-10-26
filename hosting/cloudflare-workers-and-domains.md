---
domain: web, ops
part: stack-rules
summary: Static site on Cloudflare Workers, domain, DNS and email
adapt: Replace domain and project names; assumes Cloudflare Registrar + Workers.
---

# Cloudflare: static site on Workers, custom domain, and what else a Worker can do

What was actually set up for a small product website, in the order it happened: the domain bought at **Cloudflare Registrar** and the front end (a static site of plain HTML, CSS and images) hosted on **Cloudflare Workers**, plus a plain explanation of Workers. **Why Workers:** hosting static front-end files there is free, so the whole site, including the domain's DNS and certificate, is handled in one dashboard. For a server (an API) see `render-backend.md`; for the other way round, a domain at Cloudflare but the site on Render, see `custom-domain-cloudflare-to-render.md`.

Last verified: 2026-10-18. Cloudflare changes screens and limits often; items marked **(check)** need confirming in the dashboard.

## 1. What we did

| Step | Result |
|---|---|
| Started on **GitHub Pages** (free, repository must be public) | Worked for the first weeks; the address was `<user>.github.io/<repo>/` |
| **Prerequisite:** having bought the domain at Cloudflare Registrar (Domain Registration in the dashboard) | The domain's DNS zone is created in the same account, so no nameserver change is needed |
| Moved to **Cloudflare Workers (static assets)**, connected to the GitHub repository | Every push to `main` deploys; no build step |
| Added a **custom domain** in the Cloudflare project (Settings → Domains & Routes) | The DNS records and the HTTPS certificate are created for you (no manual CNAMEs); the site is served on the bare domain, and `www.` redirects to it |
| Turned **GitHub Pages off** again | Otherwise a merge to `main` re-publishes the old copy (see "Gotchas") |
| Kept the **API on a different host** (not behind Cloudflare yet) | See `render-backend.md` |

## 2. The files in the website repository

`wrangler.jsonc` (the whole deploy configuration; no build command is needed):

```jsonc
{
  // Cloudflare static-assets deploy (no build step).
  // "name" must match the project name in Cloudflare (Workers & Pages).
  "name": "my-site",
  "compatibility_date": "2026-10-01",
  "assets": {
    "directory": "./",              // publish the repository root
    "not_found_handling": "404-page" // serve 404.html for unknown addresses
  }
}
```

`_headers` (plain text file in the root; Cloudflare applies it to static assets):

```
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/fonts/*
  Cache-Control: public, max-age=31536000, immutable
```

- Deploy command in the Cloudflare project: `npx wrangler deploy`. Build command: none.
- Cloudflare **drops the `.html` ending**: `/privacy.html` answers with a 307 redirect to `/privacy`. Write links between pages as the clean addresses (`/privacy`, `/support`), not with `.html`.
- Pull requests and branches get a build check ("Workers Builds") on the commit in GitHub, but they do not appear in the repository's Deployments list.

## 3. Steps to repeat this yourself

0. **Prerequisite:** having bought a domain at Cloudflare Registrar (Domain Registration in the dashboard), check that it appears in your account with auto-renew on. Its DNS zone is already there.
1. Put the site in a GitHub repository with `wrangler.jsonc` as above.
2. Cloudflare dashboard → **Workers & Pages** → create a project from the Git repository. The project name must match `name` in `wrangler.jsonc`.
3. Deploy command `npx wrangler deploy`; leave the build command empty.
4. Push to `main` and check that the `*.workers.dev` address shows the site.
5. Project → **Settings → Domains & Routes** → add your domain. Because the domain is registered at Cloudflare, its DNS is already there: Cloudflare creates the records and the certificate for you. (A domain bought elsewhere must first point its nameservers at Cloudflare.)
6. Add `www` as well and make it redirect to the bare domain (one redirect rule, or a second custom domain plus a redirect **(check which one you used)**).
7. Turn on "Always use HTTPS" and test with a private browser window.
8. Turn **GitHub Pages off** (Settings → Pages → source: none) if you used it before, and delete the old `github-pages` environment if you want a clean repository.

## 4. DNS and email on your own domain

- With the domain registered at Cloudflare, the DNS zone is in the same account, which is what makes the custom-domain step automatic. Records for mail (SPF, DKIM, DMARC) are added in the same **DNS → Records** page.
- **Sending mail** from the domain (for example verification emails from an app) needs the sending service to verify the domain: add the SPF and DKIM records the service shows you, and a DMARC record. Without them, mail lands in spam or is refused.
- **Receiving mail** for a public address such as `support@your-domain` without a mailbox: Cloudflare **Email Routing** forwards it to a real inbox. Test by sending a message from a different address and replying to it **(check how yours was set up)**.
- Use one contact address everywhere (store listing, support page, privacy policy, app, review contact).

## 5. What is a Worker?

A **Worker** is a small program (JavaScript or TypeScript, also Python) that runs on Cloudflare's servers close to the visitor, with no server for you to manage. A request arrives, your code runs, a response goes back.

What we used is the simplest form: **static assets**. Cloudflare stores your files and serves them; no code of yours runs. The same project can later get a script (`"main": "src/index.js"` in `wrangler.jsonc`) that runs *before* the assets, for example to redirect or to answer an API call.

Other things a Worker can do:

| Use | How |
|---|---|
| Redirects and rewrites (old address → new address) | A few lines, or Redirect Rules in the dashboard without code |
| Add or change headers on every response | In code, or the `_headers` file for static files |
| Small API endpoints (a contact form, a counter) | A script with `fetch` handler; store data with KV, D1 (SQLite) or R2 |
| Scheduled jobs | **Cron Triggers** run a script on a schedule |
| Protect or speed up another server | A Worker (or plain DNS proxying) in front of your API can cache, rate-limit or filter |
| Store files | **R2** (S3-compatible object storage, no egress fees); used here for photos behind the backend |

**Limits on the free plan** include a daily request allowance and a short CPU time per request **(check current numbers: Cloudflare's pricing page)**. A static site is served without counting against script limits; scripts count.

### Putting Cloudflare in front of an API: pros and cons

| | Pros | Cons |
|---|---|---|
| **Proxy the API through Cloudflare** (the domain's DNS record points to the API host with the proxy switched on) | Absorbs floods before they reach your server; hides the real address if you lock the origin down; one place for rate-limit and bot rules; caching for public endpoints | The API address changes (apps need an update); an extra hop; features such as advanced rate limiting can need a paid plan **(check)**; the app can still be reached directly unless the origin only accepts Cloudflare |
| **Write a Worker that forwards requests to the API** | Full control in code (custom limits, header checks, logging) | You maintain code; counts toward Worker request limits; easy to get IP and header handling wrong |
| **Leave the API as it is** | Nothing to change, no cost | Per-IP limits can be faked if the code trusts headers Cloudflare would have set; floods reach the server |

Whatever you choose, never trust `CF-Connecting-IP` or `X-Forwarded-For` unless **your own proxy** sets them (see `checklists/login-security-checklist.md`).

## 6. Gotchas we hit

- **A merge re-published the old site.** "Unpublish" on GitHub Pages only took the site down; the source setting remained, so the next merge to `main` rebuilt it. Set the Pages source to none, or delete the Pages site with the API.
- **Deployments list is stale.** Old `github-pages` deployments stay until the `github-pages` environment is deleted.
- **`.html` links.** Links with `.html` cause an extra redirect.
- **Project name mismatch.** If the `name` in `wrangler.jsonc` does not match the Cloudflare project, the deploy fails.
