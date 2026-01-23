# Knowledge

Reference documents, research, specs, and notes. Tasks reference these via `resource_refs`.

## What Goes Here

- **Specs and briefs**: Project requirements, feature specifications
- **Meeting notes**: Decisions, action items, attendees
- **Research**: Market analysis, technical findings, user insights
- **Process docs**: How-tos, checklists, runbooks
- **References**: Important links, contacts, credentials (encrypted)

## Structure Suggestions

```
Knowledge/
├── README.md
├── style-guide.md        # Writing standards
├── transcripts/          # Meeting transcripts
├── research/             # Research documents
└── specs/                # Project specifications
```

## Template

```markdown
# [Document Title]

**Type:** [spec|notes|research|process|reference]
**Created:** YYYY-MM-DD
**Updated:** YYYY-MM-DD

## Summary
Brief overview of what this document contains.

## Content
Main content here...

## Related
- Tasks that reference this
- Other Knowledge docs
```

## Tips

- Keep documents focused on one topic
- Update the "Updated" date when making changes
- Link from tasks using `resource_refs` in YAML
- Use clear, descriptive filenames
