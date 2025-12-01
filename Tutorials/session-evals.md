# Session Evals

Learn from your AI sessions by generating structured evaluations.

---

## 💻 Use Case

**Important:** Generate and annotate your first eval in 60 seconds.

1. After completing a task with your AI assistant, run:
   ```
   "Generate an eval from my recent session"
   ```

2. Review what was captured:
   ```
   "List my evals"
   ```

3. Add your judgement:
   ```
   "Annotate the latest eval as success with notes: completed refactor cleanly"
   ```

**Stretch goal:** Review pending evals at the end of the week to spot patterns.

**Super-stretch goal:** Use eval insights to update your AGENTS.md instructions.

---

## 🧰 Primitive

### The Problem

You complete work with AI assistants but have no systematic way to:
- Track what worked vs. what didn't
- Identify patterns in AI behavior
- Learn from past sessions to improve future ones
- Build an institutional memory of AI interactions

### The Solution

Session evals capture structured snapshots of your AI sessions:

```
┌─────────────────────────────────────────┐
│  Claude Code Session                    │
│  - User prompts                         │
│  - Tool calls made                      │
│  - Outcomes achieved                    │
└───────────────┬─────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│  generate_eval                          │
│  - Parses session trace                 │
│  - Extracts key patterns                │
│  - Creates markdown eval file           │
└───────────────┬─────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│  Eval File (Evals/)                     │
│  - Session metadata                     │
│  - Conversation flow                    │
│  - Tool usage summary                   │
│  - AI analysis + suggestions            │
└───────────────┬─────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│  annotate_eval                          │
│  - Your judgement (success/partial/fail)│
│  - Notes on what worked                 │
│  - Lessons for future sessions          │
└─────────────────────────────────────────┘
```

### Why This Works

Evals create a feedback loop. Without them, you repeat the same mistakes. With them, you:

- **Learn**: See which prompts lead to better outcomes
- **Improve**: Update AGENTS.md based on patterns
- **Track**: Measure AI effectiveness over time
- **Debug**: Understand why sessions go sideways

---

## Tools Available

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| `generate_eval` | Create eval from session | `session_id` (or `'recent'`) |
| `list_evals` | View all evals | `limit`, `judgement` filter |
| `annotate_eval` | Add judgement/notes | `eval_file`, `judgement`, `annotation` |
| `get_eval_summary` | Aggregate stats | none |

### Judgement Values

| Value | When to Use |
|-------|-------------|
| `success` | Task completed as expected |
| `partial` | Some progress, but gaps remain |
| `failure` | Task not completed or went wrong |
| `pending` | Not yet reviewed (default) |

---

## Anatomy of an Eval

Each eval is a markdown file with YAML frontmatter:

```yaml
---
session_id: abc123
project: personal-os
timestamp: 2025-01-15T10:30:00Z
model: claude-opus-4-5-20251101
message_count: 12
tool_call_count: 8
judgement: pending
annotation: ""
axial_codes: ['efficient-tool-use', 'clear-communication']
reviewed: false
---

# Session Eval: abc123

## User Intent
What the user asked for

## Conversation Flow
Turn-by-turn summary

## Tool Usage Summary
Table of tools and counts

## AI Analysis
- Suggested judgement
- Detected patterns
- Improvement suggestions
```

---

## Eval Workflow

```
┌─────────────────────────────────────────┐
│ Complete a session                      │
└───────────────┬─────────────────────────┘
                ↓
        ┌───────┴───────┐
        │ Was it        │
        │ significant?  │
        └───────┬───────┘
           Yes  │  No → Skip
                ↓
┌─────────────────────────────────────────┐
│ generate_eval session_id='recent'       │
└───────────────┬─────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│ Review the eval file                    │
│ - Does the AI analysis match reality?   │
│ - What actually happened?               │
└───────────────┬─────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│ annotate_eval with your judgement       │
│ - success / partial / failure           │
│ - Notes on what worked or didn't        │
└───────────────┬─────────────────────────┘
                ↓
        ┌───────┴───────┐
        │ Pattern       │
        │ emerging?     │
        └───────┬───────┘
           Yes  │  No → Done
                ↓
┌─────────────────────────────────────────┐
│ Update AGENTS.md with learnings         │
└─────────────────────────────────────────┘
```

---

## Tips

**When to generate evals:**
- After completing significant tasks
- When something went unexpectedly well or poorly
- At the end of focused work sessions

**What makes a good annotation:**
- Specific ("file search was slow") not vague ("could be better")
- Actionable ("add glob pattern hint to AGENTS.md")
- Honest (mark failures as failures to learn from them)

**Weekly review ritual:**
```
"Show me pending evals"
"What patterns do you see across my recent evals?"
```

---

## Common Patterns to Look For

| Pattern | Signal | Action |
|---------|--------|--------|
| Repeated clarification | Prompts are unclear | Improve AGENTS.md examples |
| Tool call failures | Missing context | Add tool usage hints |
| Successful shortcuts | Agent found efficiency | Document in workflows |
| Consistent partial | Scope too large | Break tasks smaller |

---

Back to: [Tutorials Home](README.md)
