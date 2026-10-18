# One `CLAUDE.md` per project: what to put in it

An AI coding assistant reads a `CLAUDE.md` file at the root of the project (and `~/.claude/CLAUDE.md` for all projects; see `global-rules.md`). Each kind of project needs different rules. This page shows what a three-part product (backend, iPhone app, website) used, the gaps found, and templates to copy.

Last verified: 2026-10-18.

## What existed (a real example)

| Project | Instruction files | Findings |
|---|---|---|
| **Backend** (Java, Spring Boot) | `docs/CLAUDE.md`, 14 lines of **testing rules** (mock everything outside our code, tests never need real credentials, end-to-end tests belong to the owner) | Good rules, but it sits in `docs/`. Assistants load a `CLAUDE.md` from the folder they work in and its parents, so a file in a subfolder may not be read at the start of a session **(check)**. Move it to the repository root. Missing: deploy rules, security rules, documentation rules, commit rules |
| **iPhone app** (Swift, SwiftUI) | No `CLAUDE.md`. A project skill `apple-hig` (Apple's Human Interface Guidelines as about 70 markdown pages plus a script that refreshes them), `app-details.md`, a `docs/` folder with launch and compliance checklists | The most work is done here, but nothing tells the assistant the project rules (versions, strings, accessibility, release branch) at the start |
| **Website** (static HTML on Cloudflare) | `CLAUDE.md` at the root (purpose, pages, privacy-policy requirements, open facts) | It was written when the site was on GitHub Pages with no custom domain; the real setup is now Cloudflare Workers with a custom domain. Out-of-date instructions mislead the assistant. Update after every hosting change |
| **All** | Notes in the assistant's memory (decisions, ops, plans) | Memory is per user and per project, not shared; decisions that matter to every session should also live in the repository |

## Rules for writing a `CLAUDE.md`

- Short and concrete. Rules the assistant can check ("every target has the same build number"), not wishes.
- Say **why** for non-obvious rules (one sentence), so the assistant can judge edge cases.
- Link to longer documents instead of pasting them (`docs/...`).
- Keep it current: update it in the same pull request that changes the setup.
- Never put secrets or personal data in it.
- Start with the purpose of the project and what is **not** the assistant's job (end-to-end tests, store listing, billing).

## Template: backend API

```markdown
# <name> backend: rules for Claude

## Purpose
One paragraph: what the API serves, who calls it, where it runs.

## Tests
- Mock everything outside our own code (email, third-party APIs, the production database, anything that costs money).
- Tests never need real credentials or network access.
- End-to-end tests against real services belong to <owner>; do not write or run them.

## Security
- Every endpoint that takes an id checks that it belongs to the caller (or the caller is an admin).
- Admin access is checked on the server, from the database, not from the token.
- Do not trust forwarded-IP headers unless our own proxy sets them.
- No secrets in the repository; new settings go in the example env file with a placeholder.

## Documentation
- When a feature is built or an endpoint changes, update **in the same change**: the API specification (OpenAPI/Swagger descriptions, request and response examples, error codes), the README (settings table, rate limits, features) and the tests' documentation if any.
- A change that adds a setting also adds it to the example env file and the README table.

## Deploys and data
- Auto-deploy is on for the deploy branch: **do not merge** unless the owner says so.
- While the mobile app is in store review: no backend changes that can break the live API.
- Data migrations: default off, dry run first, never delete the source.

## Git
- Do not commit or push without asking. Feature branch + pull request.
```

## Template: iPhone app

```markdown
# <name> iOS app: rules for Claude

## Purpose
What the app does and who uses it.

## Builds and versions
- Every target (app, widgets, extensions) has the same version and build number.
- A build number is never reused. Do not change the build while a version is in review.
- Xcode edits to project files, plists and string catalogs are harmless; keep them out of feature commits.

## UI rules
- Follow the current Human Interface Guidelines; open the matching page of the `apple-hig` skill before designing a screen.
- Use system components, text styles (Dynamic Type) and semantic colours. No fixed font sizes, no hardcoded colours.
- Every image has an accessibility label or is hidden; icon-only buttons have labels; tap targets are at least 44 points.
- Support Dark mode, Increase Contrast, Reduce Motion and Larger Text.
- Destructive actions ask for confirmation.

## Text and languages
- All user text goes through the string catalog, in every shipped language. No hardcoded strings.
- Dates and numbers use system formatters.

## Permissions and privacy
- Ask for a permission when the feature is used, with a clear purpose string in each language.
- Keep the privacy manifest and the store privacy answers in sync with what the code does.

## Tests
- Unit tests mock the network and permissions. No test shows a real system prompt.

## Documentation
- When a feature is built, update the README or app notes (features, permissions, settings) and the store review notes for that release in the same change.
- If the feature talks to the backend, check that the API specification already describes it; if not, tell the owner.

## Branches and releases
- Release work happens on its own branch; do not merge to main without the owner's go.
- Describe every new feature in the review notes of that release.
```

## Template: static website

```markdown
# <name> site: rules for Claude

## Purpose
Which public pages must exist and why (for example privacy policy and support pages required by a store).

## Hosting (keep this current)
- Host, project name, deploy trigger (push to main), custom domain.
- Links between pages use clean addresses without `.html`.

## Pages and languages
- Every page has one file per language; change both together.
- Text must be true for the real product: no filler, no data types the app does not collect.

## Documentation
- When hosting, domain, pages or contact details change, update this file and the README in the same change.

## Rules
- Do not publish placeholder text.
- Fonts: self-hosted, licence file next to the font.
- Check at phone width, in dark mode, with keyboard focus.
- Do not push without the owner's go.
```

## Things to add later as projects grow

- A short "decisions" file (licences, which paid plans are in use, what is deliberately not done) that every session can read.
- A shared card and branch convention (see `workflow/board-and-cards.md`).
- Skill links the project relies on (see the tools table in `checklists/ui-quality-checklist.md`).
