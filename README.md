# everything-mds

Markdown files I reuse across projects: checklists, templates, rules for AI coding assistants, and notes on tools. They are written to be useful to other people too, so they contain no personal data.


## Contents

| File | What it is for |
|---|---|
| [`claude/global-rules.md`](claude/global-rules.md) | Rules to give an AI coding assistant on every project (ask before committing, honesty, secrets, deploys) |
| [`claude/agent-briefing-template.md`](claude/agent-briefing-template.md) | How to hand a task to another assistant session |
| [`app-review/app-store-review-checklist.md`](app-review/app-store-review-checklist.md) | What to verify before, during and after App Store review |
| [`app-review/submission-playbook.md`](app-review/submission-playbook.md) | Step-by-step order of work for a first submission, and the traps |
| [`app-review/review-notes-template.md`](app-review/review-notes-template.md) | App Review notes: template and worked example |
| [`checklists/ui-quality-checklist.md`](checklists/ui-quality-checklist.md) | 20 UI checks and a ten-minute phone test |
| [`checklists/login-security-checklist.md`](checklists/login-security-checklist.md) | Login and API security review points |
| [`checklists/privacy-data-checklist.md`](checklists/privacy-data-checklist.md) | Data inventory, user rights, policy, Apple privacy answers |
| [`claude/project-claude-md-guide.md`](claude/project-claude-md-guide.md) | What to put in each project's `CLAUDE.md` (backend, iPhone app, website) with templates |
| [`workflow/board-and-cards.md`](workflow/board-and-cards.md) | GitHub Projects conventions and `gh` tips |
| [`hosting/cloudflare-workers-and-domains.md`](hosting/cloudflare-workers-and-domains.md) | Domain at Cloudflare, static front end on Workers (free), DNS and email notes, what else Workers can do |
| [`hosting/custom-domain-cloudflare-to-render.md`](hosting/custom-domain-cloudflare-to-render.md) | Domain at Cloudflare, site on Render: DNS records, certificate, optional proxy, and Workers vs Render |
| [`hosting/render-backend.md`](hosting/render-backend.md) | A small API on Render with Atlas, R2 and email, and the operating lessons |
| [`design/design-asset-specs.md`](design/design-asset-specs.md) | App icon, screenshot and header asset sizes and rules |
| [`design/fonts.md`](design/fonts.md) | Where to find free fonts and how to check a licence |

## How to use

- Copy a file into a project and edit it, or link to it.
- Assistant rules (`claude/`) go where the tool reads them, for example `~/.claude/CLAUDE.md` or a project's `CLAUDE.md`.
- Checklists: copy the file into your repo's `docs/` and tick the boxes per release.

## Planned

- Editor setup notes (VS Code layout and extensions).
- Email on a custom domain (sending with SPF/DKIM, receiving with Email Routing): the exact steps, to be filled in from the real dashboards.
- More checklists as they are written (release, accessibility, backend operations).