# Training Your Agent to Write in Your Voice

How to make your coding agent write like you, not like generic AI.

## Why this matters

Out of the box, most agents default to polished but generic writing.  
For emails, updates, docs, and strategy notes, you want your own voice.

This tutorial works with Claude Code, Codex, Pi, OpenClaw, and similar agents.

## Step 1: Create a voice sample folder

Create a folder and add 5-10 real samples:

```text
Resources/
└── voice-samples/
    ├── email-to-colleague.md
    ├── email-to-exec.md
    ├── slack-messages.md
    ├── linkedin-post.md
    ├── technical-doc-excerpt.md
    └── product-spec-intro.md
```

Good samples:
- Writing you actually sent
- Different contexts (internal, external, public)
- Material that sounds like you today

Avoid:
- Over-edited content
- Corporate templates you never naturally use
- Copied text

## Step 2: Extract a voice guide (progressive disclosure)

Do not ask the agent to read everything at once. Start with 2-3 files, then expand only if needed.

Prompt:

```text
Analyze these files first:
- Resources/voice-samples/email-to-colleague.md
- Resources/voice-samples/slack-messages.md
- Resources/voice-samples/technical-doc-excerpt.md

Extract a practical voice guide with:
1) Sentence length and rhythm
2) Openers/closers I use
3) Repeated phrases I prefer
4) Phrases/patterns I should avoid
5) Tone by audience
6) Structure rules for short updates vs longer docs

If confidence is low, ask me for one additional sample category instead of reading everything.
```

## Step 3: Save the guide in AGENTS.md

Add a section in `AGENTS.md` under writing guidance:

```markdown
## My Writing Voice

### Always
- [Pattern 1]
- [Pattern 2]

### Avoid
- [Anti-pattern 1]
- [Anti-pattern 2]

### By audience
- Internal: [style]
- External: [style]
- Executive: [style]

### Source examples
- Resources/voice-samples/
```

## Step 4: Test with a real output

Prompt:

```text
Draft a one-paragraph update to my VP about a one-week launch delay.

Use my writing voice from AGENTS.md.
If needed, read only one additional sample from Resources/voice-samples/.
```

Then refine with direct feedback:

```text
Too formal. I would not say "I wanted to reach out."
Use shorter sentences, fewer qualifiers, and end with a clear ask.
Try again.
```

## Step 5: Maintain the voice guide

Every month:
- Add 2-3 recent samples
- Remove stale patterns
- Re-run voice extraction on only changed samples

## Common issues

Too formal:
- Add casual internal messages
- Expand the "Avoid" list with exact phrases

Too casual:
- Add audience-specific rules in `AGENTS.md`
- Provide one stronger executive sample

Wrong structure:
- Add explicit templates for each output type (status update, email, memo)

---

Back to: [Tutorials Home](README.md)
