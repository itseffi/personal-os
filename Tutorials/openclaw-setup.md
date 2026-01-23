# OpenClaw Setup

Use this guide to run Personal OS with OpenClaw.

## What OpenClaw Needs

- This workspace as working directory
- Access to `AGENTS.md` (shared behavior)
- Access to canonical skills in `.agents/skills/`

## Recommended Setup

### Option A: Symlink `skills` (recommended)

OpenClaw commonly loads workspace skills from `./skills`, so map it to this repo's canonical skills:

```bash
ln -sfn .agents/skills skills
```

### Option B: Configure extra skill dirs

In OpenClaw config, add:

```text
<repo-root>/.agents/skills
```

as an additional skills directory.

## Start Command

Open this workspace in OpenClaw and start with:

```text
Read AGENTS.md and run the daily standup workflow
```

## Notes

- `OPENCLAW.md` and `AGENTS.md` are wrappers/instructions only.
- Source of truth for skills remains `.agents/skills/*/SKILL.md`.
