# Pi Agent Setup

Use this guide to run Personal OS with Pi as the agent frontend.

## Optional: Fully Local Backend on Mac

If you want fully local/offline execution, run a local model server first.

### Local server with llama.cpp

```bash
brew install llama.cpp
llama-server \
  -hf unsloth/GLM-4.7-Flash-GGUF:UD-Q4_K_XL \
  --jinja \
  --temp 0.7 --top-p 1.0 --min-p 0.01 \
  --repeat-penalty 1.0 --fit on \
  --port 8080
```

Quantization guidance:
- 16 GB RAM: `UD-Q3_K_XL`
- 24 GB RAM: `UD-Q4_K_XL`
- 36 GB+ RAM: `UD-Q6_K`

Fallback model for smaller machines:

```bash
llama-server -hf bartowski/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M --fit on --jinja --port 8080
```

### Connect Pi to local server

```bash
npm install -g @mariozechner/pi-coding-agent
```

Create `~/.pi/agent/models.json`:

```json
{
  "providers": {
    "llama-cpp": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "none",
      "models": [{ "id": "GLM-4.7-Flash" }]
    }
  }
}
```

Run `pi`, select your local model, then continue with repo setup below.

## What Pi Needs

- This workspace as working directory
- Access to `AGENTS.md` (shared behavior)
- Access to canonical skills in `.agents/skills/`

## Recommended Setup

1. Open Pi in:
```bash
<repo-root>
```

2. Ensure Pi uses this repo's canonical skills path:
```bash
<repo-root>/.agents/skills
```

3. Start with:
```text
Read AGENTS.md and run the daily standup workflow
```

## Optional: Local-Only Runtime

If you run Pi with a local model backend, this repo still works unchanged.
Skills and workflows are model-agnostic.

## Notes

- `PI.md` and `AGENTS.md` are wrappers/instructions only.
- The source of truth for skills remains `.agents/skills/*/SKILL.md`.
