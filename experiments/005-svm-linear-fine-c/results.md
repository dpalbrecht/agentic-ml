# Experiment 005: Linear SVM + Scaling + Fine C Grid — Results

## Approach
Scaled linear SVM with fine-grained grid search over C (1, 3, 5, 7, 10, 15, 20, 30, 50, 100). Best param: C=7.

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
0.9733 (experiment 004) → 0.9733 (+0.0000)

## vs. Success Threshold
97% accuracy → **met** (0.9733 >= 0.97)

## Observations
Fine-tuning C found C=7 as optimal but produced identical fold-level results to C=10. The per-fold scores are the same as experiment 004 — fold 3 (90%) is the bottleneck and is not sensitive to C tuning. Further gains likely require a different model or approach rather than more SVM tuning.

---
*Run on: 2026-04-12*
