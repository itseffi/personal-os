# Skill Evals

Lightweight regression evals for skill quality and structure.

## Scope

These evals validate:
- Skill packaging structure in `.agents/skills/*/SKILL.md`
- Required frontmatter fields (`name`, `description`) and folder-name alignment
- `agents/openai.yaml` metadata schema
- Routing boundaries (`When to Use`, `When Not to Use`)
- Basic instruction quality checks (has sections, has process steps)
- Behavioral case-file schema in `Evals/skills/cases/*.json`

## Run

```bash
python scripts/validate_skills.py
python scripts/validate_skill_eval_cases.py
python scripts/run_skill_evals.py --provider fixture
```

For a live model run (OpenAI-compatible endpoint):

```bash
python scripts/run_skill_evals.py --provider openai --model your-model-id
```

## Extend

Add targeted eval fixtures for high-value skills (for example `verification`, `tdd`, and `writing-plans`) and keep expected outputs under `Evals/skills/fixtures/`.

Behavioral case files should live under:

- `Evals/skills/cases/`

Manual scored runs should be saved under:

- `Evals/skills/results/`
