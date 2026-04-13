# Experiment 004: SVM + Scaling + Full Grid Search

## Approach
SVM with StandardScaler preprocessing and grid search over kernel (linear, rbf, poly), C (0.1, 1, 10, 100), and gamma (scale, auto, 0.01, 0.1, 1).

## Rationale
Experiment 003 tuned C and gamma but fixed the kernel to RBF, landing at 96.67%. Since linear logistic regression also scored 96.67%, the optimal kernel may not be RBF. Adding kernel to the search space lets the data decide.

## What changed from previous experiments
Added kernel (linear, rbf, poly) to the grid search. C and gamma grids same as 003.

## Evaluation
**Primary metric:** Accuracy
**Validation:** Stratified 5-fold cross-validation
**Success threshold:** 97% accuracy
