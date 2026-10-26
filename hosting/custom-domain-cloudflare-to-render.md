---
domain: web, ops
part: playbooks
summary: Domain at Cloudflare, site on Render
adapt: Replace example.com / my-service. Only if hosting on Render.
---

# Domain at Cloudflare, site on Render

The steps followed for several projects: the domain was bought at, and its DNS lives at, **Cloudflare**, and the site or service runs on **Render**. Examples used here: `example.com` (the domain) and `my-service` (the Render service). Screens change, so items marked **(check)** need confirming in each dashboard.

Last verified: 2026-10-18.

## 1. What each service does

| Service | Role |
|---|---|
| **Cloudflare Registrar** | Sells the domain at cost and keeps its DNS (the address book that says which server answers for the name) |
| **Render** | Runs the site (a static site, or a web service in a Docker container) and gives it a certificate (the padlock, HTTPS) |

Cloudflare only points the name at Render. The files and the code stay on Render.

## 2. Steps

1. **Prerequisite:** having bought a domain at Cloudflare Registrar (Domain Registration in the dashboard), check that it appears in your account. Its DNS zone is created automatically in the same account.
2. **Deploy the project on Render** and open its address (`my-service.onrender.com`) to check that it works before touching the domain.
3. In Render, open the service → **Settings → Custom Domains → Add Custom Domain**. Add both `example.com` (the "bare" or apex domain) and `www.example.com`. Render shows the DNS target to use (the service's `onrender.com` host name).
4. In Cloudflare → the domain → **DNS → Records**, add:

   | Type | Name | Target | Proxy |
   |---|---|---|---|
   | CNAME | `www` | `my-service.onrender.com` | **DNS only** (grey cloud) |
   | CNAME | `@` | `my-service.onrender.com` | **DNS only** (grey cloud) |

   - A CNAME on the bare domain (`@`) is normally not allowed in DNS. Cloudflare allows it by **CNAME flattening** (it answers with the target's IP addresses). Other DNS providers use an ALIAS or ANAME record, or an A record to the IP address Render lists **(check Render's current instructions)**.
   - Keep the records **DNS only** while Render verifies the domain and issues the certificate.
5. Back in Render, press **Verify** next to each domain. Render then **issues a free TLS certificate** automatically; this usually takes minutes, sometimes longer **(check)**.
6. Open `https://example.com` and `https://www.example.com`. One should redirect to the other; Render does this for you when both are added **(check which way it redirects)**.
7. Update everything that contains the address: the app or site's own base-URL setting, links in emails, the privacy policy, the store listing, and canonical tags on the pages.

## 3. Optional: turn on Cloudflare's proxy afterwards

Switching the records to **Proxied** (orange cloud) puts Cloudflare in front of Render: DDoS protection, caching, rules.

- Set Cloudflare **SSL/TLS mode to Full (strict)** first, so the connection between Cloudflare and Render stays encrypted and verified **(check)**.
- Only then trust Cloudflare's `CF-Connecting-IP` header, and only for traffic that really arrives through the proxy. The service is still reachable directly at its `onrender.com` address, where that header can be faked (see `checklists/login-security-checklist.md`).
- Proxying can interfere with certificate renewal on some setups; if a certificate fails to renew, switch the record to DNS only and verify again **(check)**.

## 4. Two ways to host the same domain

| | **Cloudflare Workers (static assets)** | **Render (static site or web service)** |
|---|---|---|
| Good for | Plain HTML/CSS sites, redirects, tiny APIs | Anything with a server: APIs, Docker apps, databases next to it |
| Domain setup | One step in the Cloudflare project; DNS records are created for you | Records added by hand in Cloudflare, then Verify in Render |
| Cost | Free for static files (limits apply **(check)**) | Static sites are free **(check)**; web services have a paid plan with a fixed monthly price |
| Deploys | Push to `main` | Push to the deploy branch (auto-deploy) |
| Watch out for | The `.html` redirect, project name must match | Free services sleep (slow first request); no spending cap; a merge is a deploy |

Both can use the same Cloudflare-registered domain, even in the same account: for example one site on Workers and another on Render. See `cloudflare-workers-and-domains.md` for the Workers path.

## 5. Check list after setup

- [ ] Both `https://example.com` and `https://www.example.com` open with a valid padlock.
- [ ] The `http://` versions redirect to `https://`.
- [ ] One address is the main one; the other redirects.
- [ ] The old `onrender.com` address is no longer used in links, emails or settings.
- [ ] Email for the domain (sending and receiving) is set up separately; see section 4 of `cloudflare-workers-and-domains.md`.
- [ ] A reminder in the calendar for the domain renewal date; keep auto-renew on and a valid card.
