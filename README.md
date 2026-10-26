# everything-mds

Markdown files I reuse across projects: checklists, templates, rules for AI coding assistants, and notes on tools. They are written to be useful to other people too, so they contain no personal data and they are general.


## Contents

| File | What it is for |
|---|---|
| [`claude/global-rules.md`](claude/global-rules.md) | Rules to give an AI coding assistant on every project (ask before committing, honesty, secrets, deploys) |
| [`claude/dependency-vulnerability-check.md`](claude/dependency-vulnerability-check.md) | Before adding a framework or library: check known vulnerabilities and patch status, tell the owner, ask for an option |
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

## Extractor: take only what you need

Two ways to copy just the notes you need into another project: **run the script**, or **give a prompt to your assistant**.

Every note is tagged with a **domain** (`general`, `web`, `ios`, `backend`, `ops`, `design`) and a **part** (`working-agreements`, `conventions`, `stack-rules`, `checklists`, `templates`, `playbooks`, `reference`) in its front matter. Mixed files tag single sections with `<!-- tags: domain=ios; part=templates -->` under the heading. A section is kept when its domain matches **any** chosen domain and its part matches **any** chosen part (no filter = all).

### Option 1: run the script (Python 3, no dependencies)

```bash
git clone https://github.com/bilgesucakir/everything-mds.git ~/everything-mds   # once
python3 ~/everything-mds/extractor/extract.py list                                   # what exists
python3 ~/everything-mds/extractor/extract.py get --domain general,web -o docs/rules.md
python3 ~/everything-mds/extractor/extract.py get --domain general,web --part working-agreements,checklists --zip -o rules.zip
python3 ~/everything-mds/extractor/extract.py check                                  # validate tags (when adding notes)
python3 ~/everything-mds/extractor/extract.py build-page                             # rebuild extractor/index.html
```

Prefer clicking? Open `extractor/index.html` in a browser, tick domains and parts, download the file (works offline; re-run `build-page` after editing notes).

### Option 2: give this prompt to your assistant (in the new project)

Fill in the `<...>` parts. A fuller version is in [`extractor/AGENT-PROMPT.md`](extractor/AGENT-PROMPT.md).

```text
Look up https://github.com/bilgesucakir/everything-mds (or ~/everything-mds if it exists on this machine; clone it into a temp folder otherwise). Read its README section "Extractor". Then copy into THIS project only the notes I need:
- Project: <name>, kind: <web app / iOS app / API>, languages: <...>, hosting: <...>.
- Domains: <e.g. general, web>. Parts: <all, or e.g. working-agreements, conventions, checklists>.
Run `python3 <repo>/extractor/extract.py list`, then `get --domain <...> -o docs/rules-from-everything-mds.md` (or read the files by hand if you cannot run it).
Put the working rules into this project's CLAUDE.md (or reference the combined file from it). Adapt names, paths, hosts and example.com to this project and follow each file's `adapt:` note.
Do NOT copy: domains I did not ask for, case studies and worked examples from other products, vendor/plan/cost facts of other projects, anything marked (check) without re-verifying, or any secrets.
Do not commit. Show me the diff and what you copied, changed and left out.
```
