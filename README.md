# Agentic ML

A personal ML workflow tool that enforces discipline on ML projects by breaking them into sequential phases, each producing a markdown artifact that the next phase consumes.

The idea: most ML projects fail because people jump to modeling before understanding the problem and defining the solution. This workflow prevents that by locking in decisions at each phase before moving on.

## Does it work?
Heck yes it does. Check out the experiments over at [Agentic-ML Experiments](https://github.com/dpalbrecht/agentic-ml-experiments).

## Workflow

Five Claude Code slash commands, run in order:

1. **`/ml-frame`** — Quick interview. Captures target, error priority, constraints, data path. Outputs `.ml-workflow/problem-frame.md`.
2. **`/ml-explore`** — Writes and runs a data exploration script in Docker. Outputs `.ml-workflow/data-assessment.md`.
3. **`/ml-design`** — Interactive. Locks in the evaluation metric, validation strategy, baseline approach, and success threshold. Outputs `.ml-workflow/experiment-design.md`.
4. **`/ml-baseline`** — Implements the baseline from the design doc, runs it in Docker, records results. Outputs `experiments/000-baseline/`.
5. **`/ml-experiment`** — The iterative loop. Reads all upstream artifacts plus every prior experiment. Proposes a next experiment, waits for approval, implements it, runs it, records results. Run as many times as needed. Outputs `experiments/NNN-name/`.

Each command checks that its prerequisite artifacts exist before running.

## Directory Structure

```
.ml-workflow/           Rules artifacts — set once, don't change across experiments
  problem-frame.md
  data-assessment.md
  experiment-design.md

experiments/            Each experiment is self-contained
  000-baseline/
    design.md
    run.py
    results.md
  001-random-forest/
    design.md
    run.py
    results.md

scripts/                Non-experiment code (exploration, utilities)
data/                   Input datasets
.claude/commands/       The slash command definitions
Dockerfile              Python environment
requirements.txt        Python dependencies
CLAUDE.md               Rules for Claude Code (auto-loaded)
```

## Conventions

- **All code runs in Docker.** Never installs packages into the user's global Python. Build with `docker build -t agentic-ml .`, run with `docker run --rm -v "$(pwd)":/project agentic-ml python <script>`. New dependencies go in `requirements.txt`, then rebuild.
- **All scripts are persisted.** No throwaway inline code. Experiment code in `experiments/NNN-name/run.py`, utilities in `scripts/`. Anything written must be standalone and re-runnable.
- **Append-only experiment history.** Don't edit past experiments — run a new one. The history is the value.
- **Evaluation is frozen at `/ml-design`.** Primary metric and validation strategy don't change across experiments. This prevents metric-shopping.

## Installing into a New Project

Clone `agentic-ml` once, then install it into any project directory:

```bash
# one-time: clone the tooling somewhere you'll keep it
git clone <your-agentic-ml-url> ~/Desktop/github/agentic-ml

# for each new ML project:
mkdir -p ~/my-ml-project
cd ~/my-ml-project
~/Desktop/github/agentic-ml/install.sh .
```

The install script copies the tooling files (commands, Dockerfile, CLAUDE.md, requirements.txt) into the target and creates empty `data/`, `scripts/`, `.ml-workflow/`, and `experiments/` directories. Project-specific artifacts are never touched.

Re-running the install script overwrites the tooling files — that's how you get updates when you improve a command in `agentic-ml`. Your project artifacts stay put.

## Getting Started

1. Install the tooling into your project (above).
2. Drop your dataset into `data/`.
3. Run the commands in order: `/ml-frame`, `/ml-explore`, `/ml-design`, `/ml-baseline`.
4. Iterate with `/ml-experiment` until you hit your success threshold.

## For Claude in a New Chat

If you're starting a new conversation with Claude about this project, the key things to know are above. Also read `CLAUDE.md` (the operating rules) and whichever phase artifacts exist in `.ml-workflow/` and `experiments/`. Don't suggest breaking conventions — the structure is the whole point.
