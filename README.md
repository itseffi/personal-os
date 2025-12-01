# Personal OS

Your AI-powered productivity system. Built for Claude Code, works with any AI coding agent.

---

## Quick Start

1. **Clone this repo**
   ```bash
   git clone https://github.com/itseffi/personal-os.git
   cd personal-os
   ```

2. **Run setup**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Start using**
   ```
   Open in Claude Code and say: "What should I work on today?"
   ```

---

## What's Inside

```
personal-os/
├── AGENTS.md           # AI agent instructions (the brain)
├── GOALS.md            # Your goals and priorities
├── BACKLOG.md          # Quick capture inbox
├── Tasks/              # Your active work
├── Knowledge/          # Your notes and docs
├── Resources/          # Voice samples, templates, references
├── Workflows/          # Daily rituals (standup, backlog, review, wrap-up)
├── Skills/             # AI skills (planning, analysis, research...)
├── Evals/              # Session reviews
├── Tutorials/          # Learning guides
└── System/             # MCP server, templates, integrations
```

---

## Key Features

### **AI Memory**
Your agent remembers your preferences, goals, and working style across sessions through structured markdown files.

### **Task Management**
- YAML frontmatter for metadata
- Priority levels (P0-P3)
- Status tracking
- Goal alignment

### **Daily Workflows**
- Daily standup (pick your focus)
- Backlog processing (turn notes into tasks)
- Weekly reviews (reflect on progress)
- Wrap-up protocol (document completed work)

### **Skills**
- Planning (brainstorming, hypothesis design, writing plans)
- Building (TDD, verification)
- Analysis (debugging, root cause, MECE, problem structuring)
- Research (JTBD, assumptions, experiments, opportunity solution tree)
- Decisions (decision journal, DAVCI, reversibility)
- Strategy (crux diagnosis, competitor analysis)
- Meetings (IDEAS summary, hidden agendas, influence)
- Stakeholders (power map, difficult conversations)

---

## How It Works

### The Memory Stack

```
AGENTS.md        →    Instructions layer (how AI behaves)
GOALS.md         →    Priority layer (what matters)
Tasks/*.md       →    State layer (current work)
Knowledge/*.md   →    Context layer (reference)
```

### Semantics by Location

Where a file lives tells the AI what it *is*:
- `Tasks/fix-bug.md` → Actionable work
- `Knowledge/fix-bug.md` → Documentation
- Files use YAML frontmatter for metadata

### Privacy First

Your personal data stays local (gitignored):
- `Tasks/` - your work
- `Knowledge/` - your notes
- `BACKLOG.md` - your inbox
- `GOALS.md` - your goals

Only system files are version controlled.

---

## Example Usage

**Daily**
```
"What should I work on today?"
```

**Capture ideas:**
```
Add to BACKLOG.md, then: "Process my backlog"
```

**Build something:**
```
"Let's brainstorm a new feature for [idea]"
"Create a spec for [feature]"
"Create a plan from this spec"
```

**Weekly:**
```
"Run weekly review"
```

---

## Documentation

- [Build Your Personal OS](Tutorials/build-your-personal-os.md) - Complete guide
- [Memory & Context](Tutorials/memory.md) - How agents remember
- [Workflows](Workflows/README.md) - Daily rituals
- [Skills](Skills/README.md) - AI skills by activity
- [Tutorials](Tutorials/README.md) - All learning guides

---

## Tech Stack

- **File Format:** Markdown with YAML frontmatter
- **AI Agent:** Claude Code (Cursor, or any coding agent)
- **Optional:** MCP integrations (Slack, Linear, Calendar, Atlassian, Granola)
- **Version Control:** Git

---

## Contributing

Issues and PRs welcome.

