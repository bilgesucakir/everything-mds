---
domain: general
part: templates
summary: How to hand a task to another assistant session
adapt: Nothing project-specific.
---

# Briefing another agent

Use this when you hand a task to another assistant session (a separate iOS, backend or website session, for example). The first line is what the other person or session sees in a preview, so make it a complete sentence.

## Template

```
One-line summary: what to build and why (a full sentence).

CONTEXT
- Where the project is (repo, branch) and what state it is in.
- Related cards or issues (links).
- Decisions already made by the owner, with dates. State clearly which text replaces older text.

WHAT TO BUILD
1. Concrete steps, one per number.
2. Inputs and outputs (for an API: path, method, request, response).
3. Edge cases that matter (errors, empty states, old versions of the client).

RULES
- Branch: which one to use. Do not merge.
- Ask before committing.
- Do not touch: build numbers, live services, demo accounts, other people's files.
- Do not deploy or merge until the owner says so.
- Tests and docs expected.

WHEN DONE
- Tell the owner (or me) what changed, how to try it, and what is still open.
- Send exact interfaces (JSON shape, file names) to the other agents who need them.
```

## Tips

- One task per message. Corrections go in a second short message that says which part is replaced.
- Name the open decision and who decides it ("ask the owner which id to use").
- If an agent is not reachable, give the owner the same text to paste into a new session.
- Never rely on `@file` references across sessions: paste the text.
