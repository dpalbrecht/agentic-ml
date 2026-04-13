# Experiment 003: SVM RBF + Scaling + Grid Search

## Approach
SVM with RBF kernel, StandardScaler preprocessing, and grid search over C (0.1, 1, 10, 100) and gamma (scale, auto, 0.01, 0.1, 1) to find optimal hyperparameters.

## Rationale
Experiment 002 showed SVM with RBF matched logistic regression exactly at 96.67%. SVM is distance-based and sensitive to feature scales — standardizing features lets the RBF kernel compute meaningful distances. Grid search over C and gamma finds the regularization/kernel-width sweet spot for this small dataset.

## What changed from previous experiments
Added StandardScaler preprocessing and grid search over C and gamma. Model class (SVM RBF) same as 002.

## Evaluation
**Primary metric:** Accuracy
**Validation:** Stratified 5-fold cross-validation
**Success threshold:** 97% accuracy
