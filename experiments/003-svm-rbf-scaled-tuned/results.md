# Experiment 003: SVM RBF + Scaling + Grid Search — Results

## Approach
SVM with RBF kernel, StandardScaler preprocessing, grid search over C (0.1, 1, 10, 100) and gamma (scale, auto, 0.01, 0.1, 1). Best params: C=10, gamma=0.1.

## Results
**Primary metric (Accuracy):** 0.9667

## Validation Details
| Fold | Accuracy |
|------|----------|
| 1    | 1.0000   |
| 2    | 1.0000   |
| 3    | 0.9333   |
| 4    | 1.0000   |
| 5    | 0.9000   |

Mean: 0.9667 (+/- 0.0422)

## vs. Baseline
0.9667 → 0.9667 (+0.0000)

## vs. Best Previous
0.9667 (experiments 000, 002) → 0.9667 (+0.0000)

## vs. Success Threshold
97% accuracy → **not met** (gap of 0.33%)

## Observations
Scaling + grid search didn't move the needle — still 96.67%. Three folds hit 100% but folds 3 and 5 consistently underperform across all experiments, suggesting a few hard-to-classify samples in those folds. The 0.33% gap is ~0.5 samples per fold. A model that handles those specific borderline versicolor/virginica cases differently may be needed — k-NN with tuned k could work, as it makes purely local decisions at those boundaries.

---
*Run on: 2026-04-12*
