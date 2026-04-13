# Experiment 002: SVM with RBF Kernel

## Approach
Support Vector Machine with RBF kernel and default hyperparameters on all four features.

## Rationale
Baseline logistic regression (96.67%) is 0.33% short of the threshold. Random forest (94.67%) showed high-variance ensembles hurt on this small dataset. SVM with RBF adds non-linearity with better generalization on small, clean data due to margin-based optimization.

## What changed from previous experiments
Model class: logistic regression / random forest → SVM with RBF kernel. Everything else unchanged.

## Evaluation
**Primary metric:** Accuracy
**Validation:** Stratified 5-fold cross-validation
**Success threshold:** 97% accuracy
