---
description: Lock in evaluation rules and baseline approach before any modeling. Outputs experiment-design.md
---

# ML Experiment Design

Prerequisites: both `.ml-workflow/problem-frame.md` and `.ml-workflow/data-assessment.md` must exist. If either is missing, tell the user which command to run first and stop.

## Purpose

Commit to how you'll evaluate experiments and what baseline they must beat — **before seeing any model results**. This prevents unconsciously changing your metric to fit your best model.

**This command does NOT write or run any code.** It produces a design document that `/ml-baseline` and `/ml-experiment` will consume.

## How this works

Read the problem frame and data assessment first. Use them to make informed suggestions for each question — don't ask generic questions when the upstream artifacts already have the answer.

Ask the user these questions **one at a time**. For each, propose a recommendation based on what you know, then let the user accept, modify, or override it.

## Questions (in order)

### 1. Evaluation Metric
Based on the error priority in the problem frame and the target distribution in the data assessment, present 2-3 candidate metrics as options with a recommended pick. Explain in one sentence why you recommend the one you do. Also suggest 1-2 secondary metrics.

Example format:
"For your primary metric, I'd suggest one of:
  1. **Accuracy** — straightforward since errors are symmetric *(recommended)*
  2. **Macro F1** — weights each class equally, useful if balance shifts later
  3. **Log loss** — penalizes confident wrong predictions

I'd go with #1 because [reason]. Which do you prefer?"

### 2. Validation Strategy
Based on dataset size and structure from the data assessment, present 2-3 validation options with a recommended pick. Make an effort to suggest a type of cross-validation strategy, even for temporal datasets, since a single split can lead to overfitting.

Example format:
"For validation:
  1. **Stratified 5-fold CV** — good for small datasets, preserves class balance *(recommended)*
  2. **Stratified 10-fold CV** — lower variance but more compute
  3. **80/20 stratified hold-out** — simplest, but high variance at this sample size

I'd go with #1 because [reason]. Which do you prefer?"

### 3. Baseline Approach
Present 2-3 baseline options with a recommended pick. The baseline is the simplest credible approach — the thing all future experiments must beat. `/ml-baseline` will implement and run whichever the user picks.

Example format:
"For the baseline:
  1. **Majority class classifier** — always predicts the most common class *(recommended)*
  2. **Logistic regression with defaults** — simple but actually learns
  3. **Random prediction weighted by class frequency** — true floor

I'd go with #1 because [reason]. Which do you prefer?"

### 4. Success Threshold
Ask what performance level makes this model worth deploying. Present 2-3 suggested thresholds based on the metric chosen, or let them name their own.

"What [primary metric] score would make this model worth using? A few reference points:
  1. **90%** — high bar, strong confidence
  2. **85%** — solid improvement over baseline
  3. **80%** — modest but meaningful

Which sounds right, or name your own?"

## Output

Write `.ml-workflow/experiment-design.md` using the user's decisions. Use this format:

```markdown
# Experiment Design

## Primary Metric
[metric name — justification]

## Secondary Metrics
[1-2 metrics to monitor]

## Validation Strategy
[split method, rationale, specifics]

## Baseline Approach
[what to implement — this is the spec for /ml-baseline]

## Success Threshold
[minimum performance to justify deployment]

---
*Designed on: [date]*
```

After writing the file, tell the user to run `/ml-baseline` next.
