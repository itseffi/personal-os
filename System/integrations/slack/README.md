# Slack Integration

Sync Slack messages and channels into your Personal OS workflow.

## What This Does

- **Check messages** from specific channels or DMs
- **Daily briefing** includes relevant Slack activity
- **Create tasks** from Slack messages

## Prerequisites

1. **Slack workspace** access
2. **Node.js 18+** installed
3. **Slack app token** with required scopes

## Quick Setup

Tell your agent:

```
Set up Slack integration for my Personal OS
```

## Manual Installation

### Step 1: Clone the Slack MCP Server

```bash
cd ~/Projects
git clone https://github.com/modelcontextprotocol/servers.git
cd servers/src/slack
npm install
```

### Step 2: Get Slack Bot Token

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Create a new app or use existing
3. Add Bot Token Scopes: `channels:history`, `channels:read`, `users:read`
4. Install to workspace
5. Copy the Bot User OAuth Token

### Step 3: Add to `.mcp.json`

```json
{
  "mcpServers": {
    "slack": {
      "command": "node",
      "args": ["/path/to/servers/src/slack/dist/index.js"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token-here",
        "SLACK_TEAM_ID": "T0123456789"
      }
    }
  }
}
```

### Step 4: Restart Your Agent Session

## Available Tools

| Tool | Description |
|------|-------------|
| `slack_list_channels` | List available channels |
| `slack_get_channel_history` | Get recent messages from a channel |
| `slack_post_message` | Send a message to a channel |
| `slack_search_messages` | Search messages across channels |

## Example Usage

### Morning check
```
Check my Slack for anything important
```

### Search for topic
```
Search Slack for messages about "deployment"
```

## Privacy

- Only accesses channels the bot is invited to
- Messages stay local - not sent anywhere
- Bot token stored in your local `.mcp.json`

## Credits

MCP Server: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
