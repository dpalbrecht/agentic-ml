---
description: Define the ML problem before touching data. Outputs problem-frame.md
---

# ML Problem Frame — Quick Intake

Collect the minimum information needed for downstream commands (`/ml.explore`, `/ml.design`, `/ml.experiment`) to make good decisions. This should take under 5 minutes.

## How this works

Ask the user these questions **one at a time**. Keep it brisk — confirm you understood, then move on. Don't push back unless something is genuinely ambiguous or contradictory. Trust that the user knows their problem.

If the user provides extra context unprompted, capture it — don't ignore useful information just because it wasn't asked for.

## Questions (in order)

### 1. Task
"What are you trying to predict or optimize? What's the target variable?"

You need: the target column/concept and whether this is classification, regression, ranking, etc. If it's obvious from their answer, don't ask them to classify it — just confirm.

### 2. What matters most
"When the model is wrong, which direction is more costly? (e.g., false positives vs. false negatives, overestimating vs. underestimating)"

You need: error asymmetry. This drives metric selection in `/ml.design`. If they say "both equally bad" that's a valid answer — move on.

### 3. Constraints
"Any hard constraints I should know about? (e.g., must be interpretable, latency limits, can't use certain features, regulatory rules)"

You need: anything that eliminates modeling approaches. If none, move on fast.

### 4. Data
"Where's your data? Point me to the file(s) in `data/` or tell me where to find them."

You need: a path. If they haven't placed data yet, tell them to drop it in `data/` and come back.

## After All Questions

Write `.ml-workflow/problem-frame.md` using the user's own words. Use this format:

```markdown
# Problem Frame

**Target:** [what they're predicting, task type]
**Error priority:** [which errors cost more, or "symmetric"]
**Constraints:** [hard constraints, or "none"]
**Data:** [file path(s)]

---
*Framed on: [date]*
```

That's it. No padding. Then tell the user to run `/ml.explore` next.
