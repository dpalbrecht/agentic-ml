---
description: Implement and run the baseline defined in experiment-design.md. Outputs to experiments/000-baseline/
---

# ML Baseline

Prerequisites: `.ml-workflow/problem-frame.md`, `.ml-workflow/data-assessment.md`, and `.ml-workflow/experiment-design.md` must all exist. If any are missing, tell the user which command to run first and stop.

## Purpose

Implement the baseline approach defined in the experiment design, run it, and record results. This establishes experiment 000 — the floor that `/ml-experiment` must beat.

**This command writes code, runs it in Docker, and records results.** No user interaction needed — just execute.

## What to do

1. **Read all upstream artifacts** — problem frame, data assessment, and experiment design. Extract:
   - Data path and feature set (from data assessment)
   - Baseline approach (from experiment design)
   - Primary metric, secondary metrics (from experiment design)
   - Validation strategy (from experiment design)

2. **Research the baseline approach** — Use WebSearch to investigate the specific baseline technique being implemented. Search for:
   - Best practices and recommended hyperparameters for this model/approach on this type of problem
   - Common pitfalls and failure modes
   - Relevant scikit-learn (or other library) API usage and parameters that matter
   - Preprocessing steps commonly paired with this approach

   Keep research focused and practical — you're looking for implementation guidance, not a literature review.

3. **Create `experiments/000-baseline/`**

4. **Write `experiments/000-baseline/research.md`** — save what you found:
   ```markdown
   # Experiment 000: Baseline — Research

   ## Approach Researched
   [the baseline approach]

   ## Key Findings
   - [practical findings that will inform the implementation]

   ## Sources
   - [URLs consulted]
   ```

5. **Write `experiments/000-baseline/design.md`:**
   ```markdown
   # Experiment 000: Baseline

   ## Approach
   [baseline approach from experiment design]

   ## Rationale
   Establishes the floor. All future experiments must beat this.

   ## Evaluation
   [primary metric, secondary metrics, validation strategy — all from experiment design]
   ```

6. **Write `experiments/000-baseline/run.py`** — a standalone script that:
   - Loads the data from the path in the data assessment
   - Uses the recommended feature set from the data assessment
   - Implements exactly the baseline approach from the experiment design
   - Evaluates using exactly the validation strategy from the experiment design
   - Reports the primary metric and any secondary metrics
   - Prints results clearly to stdout

7. **Run it in Docker:**
   - Build if needed: `docker build -t agentic-automl .`
   - Run: `docker run --rm -v "$(pwd)":/project agentic-automl python experiments/000-baseline/run.py`
   - If it fails, fix the script and re-run. Don't ask the user to debug.

8. **Write `experiments/000-baseline/results.md`** using actual results from the run:

   ```markdown
   # Experiment 000: Baseline — Results

   ## Approach
   [what was implemented]

   ## Results
   **Primary metric ([name]):** [value]
   **Secondary metrics:** [name: value, ...]

   ## Validation Details
   [per-fold results if cross-validation]

   ## vs. Success Threshold
   [success threshold from experiment design] → [met / not met / gap of X]

   ---
   *Run on: [date]*
   ```

After writing results, give the user a brief summary: what the baseline scored, how it compares to the success threshold, and tell them to run `/ml-experiment` to try to beat it.
