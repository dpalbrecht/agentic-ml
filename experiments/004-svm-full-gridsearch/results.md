# Experiment 004: SVM + Scaling + Full Grid Search — Results

## Approach
SVM with StandardScaler preprocessing and grid search over kernel (linear, rbf, poly), C (0.1, 1, 10, 100), and gamma (scale, auto, 0.01, 0.1, 1). Best params: C=10, kernel=linear.

## Results
**Primary metric (Accuracy):** 0.9733

## Validation Details
| Fold | Accuracy |
|------|----------|
| 1    | 1.0000   |
| 2    | 1.0000   |
| 3    | 0.9000   |
| 4    | 1.0000   |
| 5    | 0.9667   |

Mean: 0.9733 (+/- 0.0389)

## vs. Baseline
0.9667 → 0.9733 (+0.0067)

## vs. Best Previous
0.9667 (experiments 000, 002, 003) → 0.9733 (+0.0067)

## vs. Success Threshold
97% accuracy → **met** (0.9733 > 0.97)

## Observations
A scaled linear SVM with C=10 beat all prior experiments and crossed the 97% threshold. The grid search chose linear over RBF/poly — stronger regularization with C=10 on scaled features outperformed the default logistic regression. Fold 5 improved from 93.33% to 96.67%, closing the gap. Fold 3 remains the hardest at 90%.

---
*Run on: 2026-04-12*
