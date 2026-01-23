# Session Evals

Review agent sessions to improve your workflows and AGENTS.md.

## Why Evals Matter

Every session with your coding agent is a learning opportunity:
- What worked well? Capture it.
- What went wrong? Fix AGENTS.md.
- What patterns emerge? Document them.

## Quick Workflow

### After a significant session:

```
You: Create an eval for this session
```

Your agent should:
1. Summarize what was requested
2. Analyze what happened
3. Note what worked/didn't
4. Suggest AGENTS.md improvements

### Or manually:

1. Create `Evals/YYYY-MM-DD-description.md`
2. Fill in the template below
3. Add judgement and learnings

## Eval Template

```markdown
# Session Eval: [Brief Description]

**Date:** YYYY-MM-DD
**Judgement:** pending | success | partial | failure

## User Intent
What did you ask for?

## What Happened
Brief summary of the session flow.

## What Worked
- Good patterns observed
- Effective approaches

## What Didn't Work
- Problems encountered
- Mistakes made

## Patterns (Axial Codes)
- [ ] good-context-gathering - Read/explored before acting
- [ ] efficient-tool-use - Minimal tool calls
- [ ] iterative-refinement - Improved based on feedback
- [ ] task-tracking - Used todo list
- [ ] incomplete - Stopped before done
- [ ] over-engineering - Did more than asked
- [ ] missed-requirements - Skipped something important

## AGENTS.md Improvements
What should be added/changed in AGENTS.md based on this session?

## Notes
Any other observations.
```

## Judgement Values

| Value | Meaning |
|-------|---------|
| `success` | Task completed correctly |
| `partial` | Mostly done, minor issues |
| `failure` | Task failed or wrong result |
| `pending` | Not yet reviewed |

## When to Create Evals

Create an eval when:
- A session went particularly well (capture the pattern)
- Something went wrong (prevent repeat)
- You learned something about working with your agent
- A new workflow emerged worth documenting

## Skill Evals

Session evals are different from skill regression evals.

- Session evals: this file (`Evals/`)
- Skill evals: `Evals/skills/README.md`

## Applying Learnings

After reviewing evals:
1. Update `AGENTS.md` with new instructions
2. Add gotchas or patterns discovered
3. Refine workflows in `Workflows/`
4. Update skills in `.agents/skills/` if relevant

## Example Eval

```markdown
# Session Eval: Built personal-os-main

**Date:** 2025-01-12
**Judgement:** success

## User Intent
Combine best parts of 4 folders into one personal-OS that works with a coding agent.

## What Happened
Explored all folders, identified key components, built unified structure.

## What Worked
- Thorough exploration before building
- Used todo list to track progress
- Asked clarifying questions (superpowers folder)

## What Didn't Work
- Initially missed evals system
- User had to prompt for it

## Patterns
- [x] good-context-gathering
- [x] task-tracking
- [ ] incomplete (evals were missing)

## AGENTS.md Improvements
Add: "When building systems, check for eval/feedback mechanisms"
```
