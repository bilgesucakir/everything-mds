---
domain: general
part: conventions
summary: GitHub Projects board conventions, card contents, gh tips
adapt: Rename title prefixes to the new project's areas.
---

# Board and cards (GitHub Projects)

A simple way to keep a solo or small-team project organised across several repositories, and to hand cards to AI assistants.

## Title prefixes

| Prefix | Meaning |
|---|---|
| `[FE]` | App or front-end work |
| `[BE]` | Backend work |
| `[Owner]` | Something the owner must do (App Store Connect, billing, design, decisions) |
| `[All]` | Needs more than one part (for example app and backend) |
| `[Later]` | Not now; kept so it is not forgotten |

Write titles as what the result is, not the activity ("Settings: choose an app icon", not "Work on icons").

## Fields

- **Status:** Backlog → Ready → In progress → In review → Done.
- **Priority:** P0 (blocks a release), P1 (important), P2 (nice to have).
- **Size:** XS, S, M, L, XL (relative effort, not hours).

## What a good card contains

- The goal in one or two sentences.
- The decisions already made, with the date.
- Concrete points to build or check (a short list).
- Open questions, with who decides.
- Constraints: "not for the build that is in review", "do not deploy until the owner says".
- Links to related cards.

Use "**after approval**" or "**for release X**" in the text, not only in your head, when work must wait.

## Draft cards vs issues

- **Draft cards** live only on the board. Good for owner tasks and early ideas.
- **Issues** live in a repository and can be linked to pull requests. Use them when code is involved.
- Keep a release card per version with a numbered checklist, and link the feature cards from it.

## Command line tips (`gh`)

- Create a draft card: `gh project item-create <number> --owner <user> --title "..." --body "..."`.
- Add an existing issue: `gh project item-add <number> --owner <user> --url <issue-url>`.
- Set a single-select field by name: `gh project item-edit <number> --owner <user> --url <issue-url> --field "Status" --value "Backlog"`. For **draft cards** there is no URL; use the item id with `--id`, `--project-id`, `--field-id` and `--single-select-option-id`.
- Edit a draft's text with `--id <draft-issue-id>` and `--title` or `--body`; the draft id is not the same as the project item id.
- In shell scripts, do not reuse positional variables (`$1`, `$2`) for other values inside a function; it silently breaks the next call. A small Python script that calls `gh` is easier to get right.
- One field can be changed per call for non-draft items.

## Handing a card to an assistant

Use `agent-briefing-template.md`. Say which branch to use, what not to touch, and when to report back.
