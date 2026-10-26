# Prompt for an agent: pull the right notes from everything-mds

Paste the block below into an assistant session in the **new** project. Replace the `<...>` parts. It works if the agent can read the repo from disk (clone it) or from GitHub.

````text
Set up this project's working rules and notes from the "everything-mds" repo (a collection of reusable markdown rules, checklists and templates).

Project: <name>. Kind: <e.g. PWA web app, no backend / iOS app / API>. Languages: <e.g. Turkish and English>. Hosting: <e.g. Cloudflare Workers>.
Repo location: <local path, e.g. ~/everything-mds, or the GitHub URL https://github.com/<owner>/everything-mds>.

How to find things:
1. Read the repo's README.md (section "Extractor"). Every note has front matter: `domain` (general, web, ios, backend, ops, design), `part` (working-agreements, conventions, stack-rules, checklists, templates, playbooks, reference), `summary` and `adapt` (what to change). A line `<!-- tags: domain=...; part=... -->` under a heading overrides the file's tags for that section.
2. If you have the repo on disk, run: `python3 <repo>/extractor/extract.py list`, then
   `python3 <repo>/extractor/extract.py get --domain <general,web,...> [--part <...>] -o <project>/docs/rules-from-everything-mds.md`.
   If you only have GitHub access, read the files and keep sections whose domain matches one of mine and whose part is useful (same rules, by hand).
3. Domains I want: <e.g. general, web>. Parts: <all | e.g. working-agreements, conventions, checklists>.

What to do with it:
- Put the working rules (claude/global-rules.md content) into this project's CLAUDE.md, or into the combined file and reference it from CLAUDE.md. Use the matching template from claude/project-claude-md-guide.md for the CLAUDE.md structure.
- Adapt: replace example names (example.com, my-service, product names), paths and hosts with this project's; follow each file's `adapt:` note; delete steps that do not apply.
- Say what you copied, what you changed, and what you left out and why.

Do NOT copy:
- Anything for a domain I did not ask for (e.g. ios / App Store files, backend/Render notes when there is no backend).
- Case studies and examples from other products ("What existed (a real example)", worked examples, fictional "Trailmark" notes) except as a pattern.
- Product-specific facts of other projects: feature names, accounts, vendors/plans (e.g. an email provider or database tier), costs, "last verified" dates. Re-verify anything marked (check) before relying on it.
- Secrets or personal data of any kind.
Do not commit; show me the diff and ask first.
````
