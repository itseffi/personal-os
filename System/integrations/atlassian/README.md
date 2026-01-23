# Atlassian Integration

Connect Jira and Confluence with your Personal OS.

## What This Does

- **Sync Jira issues** with local tasks
- **Search Confluence** for documentation
- **Create issues** from Personal OS tasks
- **Update status** bidirectionally

## Prerequisites

1. **Atlassian Cloud** account
2. **Node.js 18+** installed
3. **Atlassian API token**

## Quick Setup

Tell your agent:

```
Set up Atlassian integration for my Personal OS
```

## Manual Installation

### Step 1: Clone the Atlassian MCP Server

```bash
cd ~/Projects
git clone https://github.com/modelcontextprotocol/servers.git
cd servers/src/atlassian
npm install
npm run build
```

### Step 2: Get Atlassian API Token

1. Go to [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Create a new API token
3. Copy the token

### Step 3: Add to `.mcp.json`

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "node",
      "args": ["/path/to/servers/src/atlassian/dist/index.js"],
      "env": {
        "ATLASSIAN_EMAIL": "your-email@company.com",
        "ATLASSIAN_API_TOKEN": "your-api-token",
        "ATLASSIAN_DOMAIN": "yourcompany.atlassian.net"
      }
    }
  }
}
```

### Step 4: Restart Your Agent Session

## Available Tools

### Jira
| Tool | Description |
|------|-------------|
| `jira_list_issues` | List issues assigned to you |
| `jira_create_issue` | Create a new issue |
| `jira_update_issue` | Update issue status/details |
| `jira_search` | JQL search across issues |

### Confluence
| Tool | Description |
|------|-------------|
| `confluence_search` | Search pages and content |
| `confluence_get_page` | Get page content |
| `confluence_create_page` | Create new page |

## Example Usage

### Check Jira issues
```
What are my Jira tickets?
```

### Search Confluence
```
Search Confluence for "API documentation"
```

### Create from task
```
Create a Jira ticket for this task
```

## Privacy

- Credentials stored locally
- Only accesses your Atlassian instance
- No data sent to third parties

## Credits

MCP Server: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
