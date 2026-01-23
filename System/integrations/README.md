# Integrations

Optional integrations that extend Personal OS with external tools.

## Available Integrations

| Integration | Description | Setup |
|-------------|-------------|-------|
| [Granola](./granola/) | Sync meeting notes and transcripts | `Set up Granola integration` |
| [Slack](./slack/) | Check messages and channel activity | `Set up Slack integration` |
| [Linear](./linear/) | Sync issues with local tasks | `Set up Linear integration` |
| [Google Calendar](./google-calendar/) | Check schedule, block time | `Set up Google Calendar integration` |
| [Atlassian](./atlassian/) | Jira issues, Confluence search | `Set up Atlassian integration` |

## How Integrations Work

Each integration connects an external tool via MCP (Model Context Protocol):

1. **MCP Server** - Runs locally, connects to external API
2. **Skills** - Guide your agent on how to use the tools
3. **Config** - Your credentials, stored locally

## Adding Integrations

Each integration folder contains:

- `README.md` - Full documentation and manual setup
- `mcp-config.json` - MCP server configuration template
- `skills/` - Integration skill definitions

Canonical runtime skills for this repository are in `.agents/skills/`.

## Using Integrations

Most integrations can be set up by telling your agent:

```
Set up [integration name] for my Personal OS
```

Your agent should follow the setup instructions to install and configure everything.

## Privacy

All integrations:
- Store credentials locally in `.mcp.json` (gitignored)
- Run MCP servers on your machine
- Don't send data to third parties
- Only access what you authorize

## Contributing

To add a new integration:

1. Create a folder under `System/integrations/`
2. Add `README.md` with documentation
3. Add `mcp-config.json` template
4. Add skills under `skills/[skill-name]/SKILL.md`
5. Update this README with the new integration
