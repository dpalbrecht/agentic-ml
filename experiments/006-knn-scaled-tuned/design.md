# Experiment 006: k-NN + Scaling + Tuned k

## Approach
k-Nearest Neighbors with StandardScaler preprocessing and grid search over n_neighbors (1–20) and weights (uniform, distance).

## Rationale
All prior experiments use global decision boundaries (logistic regression, SVM) or ensembles of global splits (random forest). Fold 3 at 90% appears to be a hard ceiling for these approaches. k-NN makes purely local decisions via neighborhood voting and may classify the borderline versicolor/virginica samples differently.

## What changed from previous experiments
Entirely different model class: k-NN instead of SVM. Grid search over k and weighting scheme.

## Evaluation
**Primary metric:** Accuracy
**Validation:** Stratified 5-fold cross-validation
**Success threshold:** 97% accuracy
