# Tasks

Individual task files with YAML frontmatter and progress tracking.

## Task Template

```yaml
---
title: [Actionable task name]
category: [technical|outreach|research|writing|admin|personal|other]
priority: [P0|P1|P2|P3]
status: n  # n=not_started, s=started, b=blocked, d=done
created_date: YYYY-MM-DD
due_date: YYYY-MM-DD  # optional
estimated_time: 30  # minutes, optional
resource_refs:
  - Knowledge/related-doc.md
---

# [Task Name]

## Context
Why this matters. Link to goals. Reference material.

## Next Actions
- [ ] Step one
- [ ] Step two
- [ ] Step three

## Progress Log
- YYYY-MM-DD: Started work on X
- YYYY-MM-DD: Blocked on Y, waiting for Z
```

## Status Codes

- `n` - Not started (default)
- `s` - Started / in progress
- `b` - Blocked (add blocker details to Progress Log)
- `d` - Done

## Priority Guidelines

- **P0**: Critical, must complete this week (max 3)
- **P1**: Important, has deadline or affects others (max 5)
- **P2**: Normal priority, schedule when ready
- **P3**: Low priority, nice-to-have

## Filename Convention

Use lowercase with hyphens:
- `write-quarterly-report.md`
- `fix-login-bug.md`
- `call-investor-john.md`
