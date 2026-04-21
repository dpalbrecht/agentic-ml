# Agentic ML Workflow

A structured ML workflow that enforces discipline through sequential phases.

## Workflow

1. `/ml-frame` → `.ml-workflow/problem-frame.md` — Define the problem before touching data
2. `/ml-explore` → `.ml-workflow/data-assessment.md` — Understand the data, no modeling yet
3. `/ml-design` → `.ml-workflow/experiment-design.md` — Lock in evaluation rules and baseline approach
4. `/ml-baseline` → `experiments/000-baseline/` — Implement and run the baseline
5. `/ml-experiment` → `experiments/NNN-name/` — Iterative experiments (run as many times as needed)

## Directory Structure

```
.ml-workflow/           ← "rules" artifacts that don't change across experiments
  problem-frame.md
  data-assessment.md
  experiment-design.md

experiments/            ← each experiment is self-contained
  000-baseline/
    design.md           ← what and why
    run.py              ← the code
    results.md          ← what happened
  001-name/
    design.md
    run.py
    results.md

scripts/                ← non-experiment code (explore.py, utilities)
data/                   ← input datasets
```

## Rules

- Never skip phases. Each command checks that its prerequisite artifacts exist.
- The problem frame is the constitution. All decisions trace back to it.
- Experiment log entries are append-only. Don't edit past experiments — run a new one.
- The validation strategy and primary metric are set in the experiment design and never change across experiments.

## Environment

- **All code runs in Docker.** Never install packages in the user's global Python environment.
- Build: `docker build -t agentic-ml .`
- Run: `docker run --rm -v "$(pwd)":/project agentic-ml python <script>`
- New dependencies go in `requirements.txt`, then rebuild the image.

## Code Persistence

- **Every script must be saved.** No throwaway inline code.
- Experiment code lives in `experiments/NNN-name/run.py`.
- Non-experiment code lives in `scripts/`.
- All scripts must be standalone and re-runnable inside the container.
