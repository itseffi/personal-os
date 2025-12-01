# Subagents: Specialized AI Assistants

## What Are Subagents?

Subagents are specialized AI assistants you configure for specific tasks or projects. Instead of giving the same context every time you start a new chat, you define it once and the agent always knows what to do.

Think of it like this: your main AI assistant is a generalist. Subagents are specialists—a robotics engineer who knows your hardware, a research assistant who knows your domain, or a code reviewer who knows your standards.

## Why Use Them?

**No more repeating yourself**
Instead of pasting "here's my hardware config, here are the sensor limits, here are the code patterns..." every session, the subagent already knows.

**Consistent outputs**
The agent follows the same rules every time. Your behavior code will use consistent patterns. Your research will check the same sources.

**Faster context loading**
The subagent reads only what it needs. A hardware debugging agent doesn't need your meeting notes.

**Shareable with your team**
Commit subagents to your repo. Now everyone has the same specialized assistants.

---

## How to Set Them Up

### Claude Code

Create a markdown file in `.claude/agents/`:

```
your-repo/
└── .claude/
    └── agents/
        └── my-agent.md
```

**Format:**

```markdown
---
name: my-agent
description: When to use this agent (shown in agent picker)
tools: Read, Edit, Write, Grep, Glob
model: sonnet
---

# System Prompt

Your instructions here. Tell the agent:
- What it does
- What files to reference
- Rules to follow
- Output format expected
```

**Use it:** Run `/agents` in Claude Code to see and select your agents.

### Factory

Create a markdown file in `.factory/droids/`:

```
your-repo/
└── .factory/
    └── droids/
        └── my-droid.md
```

**Format:**

```markdown
---
name: my-droid
description: When to use this droid
model: inherit
tools: ["Read", "Edit", "Grep", "Glob", "LS"]
---

# System Prompt

Your instructions here.
```

**Key differences from Claude Code:**
- `tools` is an array with quotes: `["Read", "Edit"]`
- Tool names differ slightly: `LS` instead of `Bash(ls)`, `FetchUrl` instead of `WebFetch`
- Use `model: inherit` to match the parent session

---

## Real Example: Reachy Mini Development Agent

Here's a subagent I use for Reachy Mini—the expressive desktop robot from Pollen Robotics × Hugging Face:

```markdown
---
name: reachy-dev
description: Reachy Mini development - behaviors, sensors, Hugging Face AI integration
tools: Read, Glob, Grep, Edit, Write, Bash
model: sonnet
---

# Reachy Mini Development Agent

You help develop expressive behaviors and AI integrations for Reachy Mini.

## Hardware Context
- 6 DOF head movement + full 360° body rotation
- 2 animated antennas for expression
- Wide-angle camera, 4 microphones (Wireless version)
- Python SDK with async support
- Hugging Face Hub for AI models

## Before Any Task
Check these files for current state:
- `Knowledge/reachy-config.md` - Calibration, DOF limits
- `Knowledge/hf-models.md` - Which AI models we're using
- `Tasks/` - Current priorities

## Code Standards
- Use async for smooth movements
- Keep expression loops under 50ms
- Handle camera FPS drops during inference
- Test all 4 mics for spatial audio
```

Now when I say "help me build an interactive greeting behavior", the agent knows my hardware constraints, where to find config files, and what coding patterns to use.

---

## How I Created This Without Writing It Manually

I didn't write that agent definition by hand. Here's what I did:

**Step 1:** Asked Claude Code:
> "I want a subagent for Reachy Mini development. How do I set that up?"

**Step 2:** Pointed to my existing docs:
> "Here's context: `Knowledge/reachy-config.md`, `Knowledge/hf-models.md`, and `docs/coding-patterns.md`"

**Step 3:** Claude Code read the files, extracted the key constraints, and generated the agent definition.

**Step 4:** I reviewed it, tweaked a few things, done.

Total time: 3 minutes. Writing it manually would have taken 15+.

**The pattern:**
```
1. "I want a subagent for [task]"
2. "Here are context files: [paths]"
3. Let the AI synthesize them into an agent definition
4. Review and tweak
```

You probably already have the context documented somewhere—config files, style guides, lessons learned. Point the AI at them instead of rewriting everything.

---

## Tips

**Start simple.** Your first subagent can be 10 lines. Add detail as you discover what's missing.

**Reference files, don't duplicate.** Point to existing docs (`Knowledge/config.md`) rather than copying content into the agent. Keeps things maintainable.

**Restrict tools.** A research agent doesn't need `Bash`. Fewer tools = more focused behavior.

**Write good descriptions.** This is how the AI decides when to suggest this agent. Be specific: "Reachy Mini behavior development" not "robot stuff".

---

## Quick Start

1. Create the directory:
   ```bash
   mkdir -p .claude/agents
   ```

2. Create your agent file:
   ```bash
   touch .claude/agents/my-agent.md
   ```

3. Add the YAML frontmatter + instructions

4. Test it with `/agents` in Claude Code