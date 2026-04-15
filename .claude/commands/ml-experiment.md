---
description: Design, run, and record an experiment. Reads all prior results to decide what to try next. Repeatable.
---

# ML Experiment

Prerequisites: `.ml-workflow/problem-frame.md`, `.ml-workflow/data-assessment.md`, `.ml-workflow/experiment-design.md`, and `experiments/000-baseline/results.md` must all exist. If any are missing, tell the user which command to run first and stop.

## Purpose

This is the iterative experimentation loop. Each run:
1. Reads all context (upstream artifacts + all prior experiment results)
2. Proposes a next experiment
3. Waits for user approval
4. Implements, runs, and records results

**This command can be run any number of times.** Each run creates a new numbered experiment directory.

## Step 1: Read everything

Read all of:
- `.ml-workflow/problem-frame.md`
- `.ml-workflow/data-assessment.md`
- `.ml-workflow/experiment-design.md`
- Every `experiments/*/results.md` (scan all existing experiment directories)
- Every `experiments/*/design.md` (to understand what's already been tried and why)
- Every `experiments/*/research.md` (to avoid re-researching the same topics)

## Step 2: Propose the next experiment

Based on what you've learned from all prior experiments, propose what to try next. Present it to the user for approval before writing any code.

Your proposal should include:
- **What:** the approach (model, feature engineering, hyperparameter changes, etc.)
- **Why:** what you expect to learn or improve, based on patterns in prior results
- **How it differs** from what's already been tried

Guidelines for proposing experiments:
- Change one thing at a time when possible — it's easier to learn from results
- If the last experiment nearly hit the success threshold, try refinements
- If it was far off, try a different approach
- Don't repeat an experiment that's already been tried
- Escalate complexity only when simpler approaches have been exhausted

Ask: "Here's what I'd try next: [proposal]. Want me to run this, or would you prefer something different?"

**Wait for user approval before proceeding.**

## Step 3: Research the approved approach

Before writing code, use WebSearch to research the specific technique being implemented. Search for:
- Best practices and recommended hyperparameters for this model/approach on this type of problem
- Common pitfalls and failure modes
- Relevant library API usage and parameters that matter
- Preprocessing or feature engineering tips commonly paired with this approach
- Any recent findings or benchmarks relevant to the approach

Keep research focused and practical — you're looking for implementation guidance, not a literature review. Use what you find to inform the implementation in Step 4.

## Step 4: Implement and run

Determine the next experiment number by scanning existing directories (e.g., if `000-baseline` and `001-random-forest` exist, the next is `002`).

Create a short, descriptive directory name: `experiments/[NNN]-[short-name]/`

1. **Write `experiments/[NNN]-[name]/research.md`** — save what you found in Step 3:
   ```markdown
   # Experiment [NNN]: [Name] — Research

   ## Approach Researched
   [the technique/model being implemented]

   ## Key Findings
   - [practical findings that will inform the implementation]

   ## Sources
   - [URLs consulted]
   ```

2. **Write `experiments/[NNN]-[name]/design.md`:**
   ```markdown
   # Experiment [NNN]: [Name]

   ## Approach
   [what's being tried]

   ## Rationale
   [why this is the logical next step given prior results]

   ## What changed from previous experiments
   [specific differences]

   ## Evaluation
   [same primary metric, secondary metrics, validation strategy from experiment design]
   ```

3. **Write `experiments/[NNN]-[name]/run.py`** — a standalone script that:
   - Loads data using the same path and feature set as prior experiments
   - Implements the proposed approach
   - Uses the same validation strategy from the experiment design (always)
   - Reports primary and secondary metrics
   - Prints results clearly to stdout

4. **Run it in Docker:**
   - Build if needed: `docker build -t agentic-automl .`
   - Run: `docker run --rm -v "$(pwd)":/project agentic-automl python experiments/[NNN]-[name]/run.py`
   - If a new dependency is needed, add it to `requirements.txt` and rebuild first
   - If it fails, fix the script and re-run. Don't ask the user to debug.

5. **Write `experiments/[NNN]-[name]/results.md`:**
   ```markdown
   # Experiment [NNN]: [Name] — Results

   ## Approach
   [what was implemented]

   ## Results
   **Primary metric ([name]):** [value]
   **Secondary metrics:** [name: value, ...]

   ## Validation Details
   [per-fold results if cross-validation]

   ## vs. Baseline
   [baseline value] → [this value] ([+/- delta])

   ## vs. Best Previous
   [best previous value from experiment NNN] → [this value] ([+/- delta])

   ## vs. Success Threshold
   [success threshold] → [met / not met / gap of X]

   ## Observations
   [1-2 sentences: what did we learn? what does this suggest for the next experiment?]

   ---
   *Run on: [date]*
   ```

## Step 5: Report

After recording results, give the user a brief summary:
- What was tried
- How it performed vs. baseline, best previous, and success threshold
- What you'd suggest trying next (but don't run it — wait for the user to invoke `/ml-experiment` again)
