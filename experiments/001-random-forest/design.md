# Experiment 001: Random Forest

## Approach
Random forest classifier with default hyperparameters (100 estimators) on all four features.

## Rationale
Baseline logistic regression scored 96.67%, 0.33% short of the 97% threshold. As a linear model, it can't capture non-linear feature interactions. Random forest is the natural next step — a non-linear ensemble that may close the gap.

## What changed from previous experiments
Model class: logistic regression → random forest. Everything else (features, validation, metric) stays the same.

## Evaluation
**Primary metric:** Accuracy
**Validation:** Stratified 5-fold cross-validation
**Success threshold:** 97% accuracy
