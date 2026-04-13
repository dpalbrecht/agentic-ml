# Experiment Design

## Primary Metric
Accuracy — classes are perfectly balanced and errors are symmetric, so accuracy is interpretable and undistorted.

## Validation Strategy
Stratified 5-fold cross-validation. 150 samples is too small for a single hold-out split; 5-fold gives stable estimates while preserving class balance in each fold.

## Baseline Approach
Logistic regression with default hyperparameters. Simple, learns from the data, and sets a meaningful floor that future experiments must beat.

## Success Threshold
97% accuracy — high bar, near-perfect classification required to justify deployment.

---
*Designed on: 2026-04-12*
