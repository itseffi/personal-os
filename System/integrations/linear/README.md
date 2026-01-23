# Linear Integration

Sync Linear issues with your Personal OS tasks.

## What This Does

- **Sync issues** from Linear to local tasks
- **Create issues** in Linear from Personal OS
- **Update status** bidirectionally
- **Daily planning** includes Linear priorities

## Prerequisites

1. **Linear account** with API access
2. **Node.js 18+** installed
3. **Linear API key**

## Quick Setup

Tell your agent:

```
Set up Linear integration for my Personal OS
```

## Manual Installation

### Step 1: Clone the Linear MCP Server

```bash
cd ~/Projects
git clone https://github.com/jerhadf/linear-mcp-server.git
cd linear-mcp-server
npm install
npm run build
```

### Step 2: Get Linear API Key

1. Go to [linear.app/settings/api](https://linear.app/settings/api)
2. Create a new personal API key
3. Copy the key

### Step 3: Add to `.mcp.json`

```json
{
  "mcpServers": {
    "linear": {
      "command": "node",
      "args": ["/path/to/linear-mcp-server/dist/index.js"],
      "env": {
        "LINEAR_API_KEY": "lin_api_xxxxx"
      }
    }
  }
}
```

### Step 4: Restart Your Agent Session

## Available Tools

| Tool | Description |
|------|-------------|
| `linear_list_issues` | List issues assigned to you |
| `linear_create_issue` | Create a new issue |
| `linear_update_issue` | Update issue status/details |
| `linear_search_issues` | Search across issues |
| `linear_get_teams` | List available teams |

## Example Usage

### Check assigned issues
```
What are my Linear issues?
```

### Create issue from task
```
Create a Linear issue for "Fix authentication bug"
```

### Sync status
```
Mark my Linear issue LIN-123 as done
```

## Privacy

- API key stored locally in `.mcp.json`
- Only accesses your Linear workspace
- No data sent to third parties

## Credits

MCP Server: [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)
