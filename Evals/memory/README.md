# Memory Impact Evals

These evals test whether enabling memory-search behavior actually changes outputs in the expected direction.

## Scope

- A/B comparisons (baseline vs memory-search-enabled)
- Expected behavior deltas:
  - stronger goal alignment
  - better blocked-task handling
  - better context use (knowledge lookup, dedup checks)

## Run

```bash
python scripts/run_memory_impact_evals.py
```

Results are written to:

- `Evals/memory/results/`
