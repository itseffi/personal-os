# Google Calendar Integration

Sync your calendar with Personal OS for better daily planning.

## What This Does

- **Check schedule** for today/week
- **Block time** for focused work
- **Daily planning** includes calendar context
- **Find free slots** for scheduling

## Prerequisites

1. **Google account** with Calendar
2. **Node.js 18+** installed
3. **Google Cloud credentials**

## Quick Setup

Tell your agent:

```
Set up Google Calendar integration for my Personal OS
```

## Manual Installation

### Step 1: Clone the Google Calendar MCP Server

```bash
cd ~/Projects
git clone https://github.com/modelcontextprotocol/servers.git
cd servers/src/google-calendar
npm install
```

### Step 2: Set Up Google Cloud Credentials

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project or select existing
3. Enable Google Calendar API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download `credentials.json`

### Step 3: Authenticate

```bash
node dist/index.js --auth
```

Follow the browser prompt to authorize.

### Step 4: Add to `.mcp.json`

```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "node",
      "args": ["/path/to/servers/src/google-calendar/dist/index.js"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "/path/to/credentials.json",
        "GOOGLE_TOKEN_PATH": "/path/to/token.json"
      }
    }
  }
}
```

### Step 5: Restart Your Agent Session

## Available Tools

| Tool | Description |
|------|-------------|
| `calendar_list_events` | Get events for date range |
| `calendar_create_event` | Create a new event |
| `calendar_update_event` | Modify existing event |
| `calendar_delete_event` | Remove an event |
| `calendar_find_free_time` | Find available slots |

## Example Usage

### Check today's schedule
```
What's on my calendar today?
```

### Find time for deep work
```
Find 2 hours of free time this week for focused work
```

### Block time
```
Block 2pm-4pm tomorrow for project work
```

## Privacy

- Credentials stored locally
- Only accesses your calendar
- No data sent to third parties

## Credits

MCP Server: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
