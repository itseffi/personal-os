# Granola Integration

Sync your [Granola.ai](https://granola.ai) meeting notes and transcripts into your Personal OS Knowledge folder.

## What This Does

- **Search meetings** by title, participants, or content
- **Sync meeting notes** to your local `Knowledge/transcripts/` folder
- **Daily planning** includes recent meeting context
- **Pattern analysis** across your meetings (topics, frequency, participants)

## Prerequisites

1. **Granola.ai** installed and running on macOS
2. **Python 3.12+** installed
3. **uv** package manager (`brew install uv` or `pip install uv`)

## Quick Setup

Tell your agent:

```
Set up Granola integration for my Personal OS
```

Your agent should:
1. Clone the Granola MCP server
2. Configure your `.mcp.json`
3. Verify the connection works

## Manual Installation

### Step 1: Clone the Granola MCP Server

```bash
cd ~/Projects  # or wherever you keep repos
git clone https://github.com/proofgeist/granola-ai-mcp-server.git
cd granola-ai-mcp-server
uv sync
```

### Step 2: Test the Server

```bash
uv run python test_server.py
```

### Step 3: Add to `.mcp.json`

Add this to your project's `.mcp.json` file:

```json
{
  "mcpServers": {
    "granola": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/granola-ai-mcp-server",
        "run",
        "granola-mcp-server"
      ],
      "env": {
        "KNOWLEDGE_PATH": "/absolute/path/to/your/personal-os/Knowledge"
      }
    }
  }
}
```

Replace the paths with your actual locations.

### Step 4: Create Transcripts Folder

```bash
mkdir -p Knowledge/transcripts
```

### Step 5: Ensure Skills Are Available

Canonical runtime skills for this repo live in:

```bash
.agents/skills/
```

Integration source skills also live in:

```bash
System/integrations/granola/skills/
```

### Step 6: Restart Your Agent Session

Restart your agent session to load the new MCP server.

## Included Skills

### meeting-sync

Triggered by: "Sync my meetings", "What should I do today?", or during daily planning.

What it does:
1. Checks for new unsynced Granola meetings
2. Presents them to you with sync options
3. Exports selected meetings to `Knowledge/transcripts/`
4. Continues with your normal workflow

If you maintain an external Claude-specific skills folder, mirror this skill there manually.

## Available Tools

| Tool | Description |
|------|-------------|
| `search_meetings` | Search by title, content, or participants |
| `get_meeting_details` | Get full meeting metadata |
| `get_meeting_transcript` | Retrieve the transcript |
| `check_new_meetings` | List meetings not yet synced |
| `sync_meeting_to_local` | Export meeting to Knowledge folder |
| `analyze_meeting_patterns` | Analyze topics, frequency, participants |
| `get_last_sync_time` | Check when you last synced |
| `reset_sync` | Re-sync meetings from past N days |

## Example Usage

### Sync new meetings

```
Sync my Granola meetings
```

### Search for a topic

```
Search my meetings for "product roadmap"
```

### Daily planning with meetings

```
What should I work on today?
```

This automatically checks for new meetings and incorporates recent context.

### Analyze patterns

```
Who have I been meeting with most this month?
```

## How Syncing Works

1. `check_new_meetings` compares Granola cache against `.granola-sync.json`
2. `sync_meeting_to_local` exports selected meetings as markdown
3. Files are saved to `Knowledge/transcripts/YYYY-MM-DD_meeting-title.md`
4. Sync state is tracked so meetings aren't duplicated

## Troubleshooting

### "No Granola cache found"

Make sure Granola is installed and you've attended at least one meeting. The cache lives at:
```
~/Library/Application Support/Granola/cache-v3.json
```

### "uv: command not found"

Install uv:
```bash
brew install uv
# or
pip install uv
```

### MCP server not connecting

1. Check the path in `.mcp.json` is absolute
2. Verify `uv sync` ran successfully in the granola-mcp-server folder
3. Restart your agent session

### Meetings show "(no notes)"

Some calendar events in Granola don't have meeting content. These are typically placeholder events or meetings you didn't record.

## Related Skills

- **meeting-sync** - Sync workflow with user prompts
- **daily-planning** - Includes meeting check in daily planning

## Privacy

- All data stays local on your machine
- The MCP server reads from Granola's local cache only
- No external API calls are made
- Your transcripts are never sent anywhere

## Credits

MCP Server: [proofgeist/granola-ai-mcp-server](https://github.com/proofgeist/granola-ai-mcp-server)
