# Experiment 006: k-NN + Scaling + Tuned k — Results

## Approach
k-Nearest Neighbors with StandardScaler and grid search over n_neighbors (1–20) and weights (uniform, distance). Best params: k=5, uniform weights.

## Results
**Primary metric (Accuracy):** 0.9733

## Validation Details
| Fold | Accuracy |
|------|----------|
| 1    | 1.0000   |
| 2    | 0.9667   |
| 3    | 0.9333   |
| 4    | 1.0000   |
| 5    | 0.9667   |

Mean: 0.9733 (+/- 0.0249)

## vs. Baseline
0.9667 → 0.9733 (+0.0067)

## vs. Best Previous
0.9733 (experiment 004) → 0.9733 (+0.0000)

## vs. Success Threshold
97% accuracy → **met** (0.9733 >= 0.97)

## Observations
k-NN matched the best previous accuracy at 97.33% but with a different error distribution: fold 3 improved (90% → 93.33%) while fold 2 dropped (100% → 96.67%). Lower variance across folds (std 0.0249 vs 0.0389) suggests more stable predictions. The 97.33% ceiling appears to be a hard limit for single models on this dataset — an ensemble combining k-NN and SVM predictions could potentially break through.

---
*Run on: 2026-04-12*
