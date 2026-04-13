# Experiment 005: Linear SVM + Scaling + Fine C Grid

## Approach
Scaled linear SVM with fine-grained grid search over C (1, 3, 5, 7, 10, 15, 20, 30, 50, 100).

## Rationale
Experiment 004 crossed the 97% threshold with C=10 on a coarse grid. A finer search around that region may find a better regularization sweet spot, particularly to improve fold 3 (90%).

## What changed from previous experiments
Finer C grid focused on the winning region from 004. Same pipeline (StandardScaler + linear SVM).

## Evaluation
**Primary metric:** Accuracy
**Validation:** Stratified 5-fold cross-validation
**Success threshold:** 97% accuracy
