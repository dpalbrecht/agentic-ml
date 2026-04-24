---
description: Explore the dataset against the problem frame. Outputs data-assessment.md
---

# ML Data Exploration

Prerequisite: `.ml-workflow/problem-frame.md` must exist. If it doesn't, tell the user to run `/ml-frame` first and stop.

## Environment

**All code runs in Docker.** Never install packages in the user's global environment.

1. Build the container if it doesn't exist yet: `docker build -t agentic-ml .`
2. Run scripts with the project mounted: `docker run --rm -v "$(pwd)":/project agentic-ml python scripts/explore.py`
3. If you need a new package, add it to `requirements.txt` and rebuild the image before running.

## Code persistence

**Save all code to `scripts/`.** Every script you write must be a standalone, re-runnable Python file. Never use throwaway inline code that disappears after execution.

For this command, write your exploration code to `scripts/explore.py`. The user should be able to re-run it themselves with `docker run --rm -v "$(pwd)":/project agentic-ml python scripts/explore.py`.

## What to do

1. Read the problem frame and inspect the datasets in /data.
2. Think about the best tools to explore the dataset given the problem and dataset size. For example, Pandas is fine for moderately sized data but Polars is best for large datasets (millions of rows).
3. Write the exploration script and run it in Docker.
4. Use the output to write the assessment.

Do the analysis yourself. Don't ask the user questions — just do the work and present findings. Only ask if something is genuinely ambiguous (e.g., the data path doesn't exist).

## Analysis checklist

The script should print results for:

1. **Shape & schema** — rows, columns, dtypes, column names. If no header row, infer or ask.
2. **Target variable** — distribution (class counts for classification, histogram stats for regression). Flag if imbalanced (>3:1 ratio).
3. **Missing values** — count per column. Flag columns with >10% missing.
4. **Feature distributions** — quick summary stats. Flag outliers (>3 std from mean), zero-variance columns, or highly correlated pairs (>0.95).
5. **Leakage check** — flag any feature that looks like it could leak the target (same name, suspiciously perfect correlation, or derived from future data).
6. **Signal structure** — are feature-target correlations spread across many features, or concentrated in a few? If only a handful of features show meaningful signal (even weak signal), flag this explicitly — it suggests most features may be noise and feature selection should be explored during experimentation.
7. **Data quality issues** — duplicates, inconsistent formatting, mixed types in columns, anything weird.

## Output

Write `.ml-workflow/data-assessment.md` with this format:

```markdown
# Data Assessment

## Overview
[rows, columns, file(s)]

## Target: [column name]
[distribution summary — class counts or stats]

## Features
[table: column | dtype | missing % | notes]

## Issues Found
[bullet list of problems, or "None" — be specific]

## Leakage Risk
[any concerns, or "None identified"]

## Signal Structure
[Is signal spread across many features or concentrated in a few? If concentrated, flag that feature selection may improve modeling and note which features carry the signal.]

## Recommended Feature Set
[which columns to use and why, which to drop and why]

---
*Assessed on: [date]*
```

Keep it tight. After writing the file, give the user a brief verbal summary of the key findings (2-3 sentences) and tell them to run `/ml-design` next.
