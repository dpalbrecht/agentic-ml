# Experiment 001: Random Forest — Results

## Approach
Random forest classifier with default hyperparameters (100 estimators, random_state=42) on all four features.

## Results
**Primary metric (Accuracy):** 0.9467

## Validation Details
| Fold | Accuracy |
|------|----------|
| 1    | 0.9667   |
| 2    | 0.9667   |
| 3    | 0.9333   |
| 4    | 0.9667   |
| 5    | 0.9000   |

Mean: 0.9467 (+/- 0.0267)

## vs. Baseline
0.9667 → 0.9467 (−0.0200)

## vs. Best Previous
0.9667 (experiment 000) → 0.9467 (−0.0200)

## vs. Success Threshold
97% accuracy → **not met** (gap of 2.33%)

## Observations
Default random forest underperformed logistic regression. With only 150 samples and 4 clean features, the ensemble's variance hurts more than its flexibility helps. Next step: try a simpler non-linear model (e.g., SVM with RBF kernel) or tune the random forest to reduce overfitting.

---
*Run on: 2026-04-12*
