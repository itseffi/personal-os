# Subagents (Optional Pattern)

Use this only if your runtime supports subagents/agent delegation.

Personal OS does not require subagents to work. The core architecture is:
- `AGENTS.md` + wrapper files (`CLAUDE.md`, `CODEX.md`, `PI.md`, `OPENCLAW.md`)
- Skills in `.agents/skills/*/SKILL.md`
- Workflows in `Workflows/*.md`
- State and context in `Tasks/`, `Knowledge/`, `GOALS.md`, `BACKLOG.md`

## When to Use Subagents

Use subagents when a task benefits from strict specialization, for example:
- one agent to synthesize research evidence
- one agent to produce a structured plan
- one agent to verify output quality

Do not use subagents for simple tasks where one agent can complete the work directly.

## Recommended Pattern in This Repo

If your runtime supports delegation:
1. Main agent reads `AGENTS.md` and selects the relevant workflow.
2. Delegate only scoped subtasks (research extraction, plan drafting, verification).
3. Require each subagent to reference the same source-of-truth files.
4. Main agent merges outputs and applies final verification discipline.

## Minimal Subagent Prompt Template

```markdown
Role: [specialist role]

Objective:
- [single, clear outcome]

Scope:
- Read only:
  - AGENTS.md
  - Workflows/[workflow].md
  - [specific files]

Constraints:
- Follow task schema in AGENTS.md
- Do not modify unrelated files
- Return concise output with explicit assumptions

Verification:
- List checks run
- Mark unknowns clearly
```

## Example: Daily Prioritization with Delegation

Main prompt:

```text
Use daily-standup workflow and propose top 3 tasks.
If needed, delegate:
1) one subagent for task-state extraction from Tasks/*.md
2) one subagent for goal alignment checks against GOALS.md
Then synthesize and return one final prioritized list.
```

## Runtime Notes

- Subagent features are runtime-dependent and may differ across Claude Code, Codex, Pi, OpenClaw, and other tools.
- Keep Personal OS portable by storing durable logic in:
  - `.agents/skills/`
  - `Workflows/`
  - `AGENTS.md`

---

Back to: [Tutorials Home](README.md)
