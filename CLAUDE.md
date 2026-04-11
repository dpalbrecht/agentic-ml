# Agentic AutoML Workflow

A structured ML workflow that enforces discipline through sequential phases. Each phase produces an artifact that the next phase consumes.

## Workflow

1. `/ml-frame` → `.ml-workflow/problem-frame.md` — Define the problem before touching data
2. `/ml-explore` → `.ml-workflow/data-assessment.md` — Understand the data, no modeling yet
3. `/ml-design` → `.ml-workflow/experiment-design.md` — Commit to evaluation strategy before seeing results
4. `/ml-experiment` → `.ml-workflow/experiment-log.md` — Run experiments against pre-committed metrics

## Rules

- Never skip phases. Each command checks that its prerequisite artifact exists.
- The problem frame is the constitution. Design and experiment decisions must trace back to it.
- Artifacts live in `.ml-workflow/`. Scripts live in `scripts/`. Data lives in `data/`.
- Experiment log entries are append-only. Don't edit past entries — add a new one with revised thinking.

## Environment

- **All code runs in Docker.** Never install packages in the user's global Python environment.
- Build: `docker build -t agentic-automl .`
- Run: `docker run --rm -v "$(pwd)":/project agentic-automl python scripts/<script>.py`
- New dependencies go in `requirements.txt`, then rebuild the image.

## Code Persistence

- **Every script must be saved to `scripts/`.** No throwaway inline code.
- Scripts must be standalone and re-runnable inside the container.
- The user should be able to review and re-run any script at any time.
