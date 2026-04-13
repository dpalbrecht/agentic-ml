# Experiment 002: SVM with RBF Kernel — Results

## Approach
Support Vector Machine with RBF kernel and default hyperparameters on all four features.

## Results
**Primary metric (Accuracy):** 0.9667

## Validation Details
| Fold | Accuracy |
|------|----------|
| 1    | 1.0000   |
| 2    | 0.9667   |
| 3    | 0.9333   |
| 4    | 1.0000   |
| 5    | 0.9333   |

Mean: 0.9667 (+/- 0.0298)

## vs. Baseline
0.9667 → 0.9667 (+0.0000)

## vs. Best Previous
0.9667 (experiment 000) → 0.9667 (+0.0000)

## vs. Success Threshold
97% accuracy → **not met** (gap of 0.33%)

## Observations
SVM with RBF matched the baseline exactly (same per-fold scores). The non-linearity of the RBF kernel didn't help — the decision boundary may already be near-linear for the misclassified samples. Next step: try tuning the SVM (C and gamma) or scaling the features, since SVM is sensitive to feature scales and the defaults may not be optimal.

---
*Run on: 2026-04-12*
