# Experiment 000: Baseline

## Approach
Logistic regression with default hyperparameters on all four features (sepal_length, sepal_width, petal_length, petal_width).

## Rationale
Establishes the floor. All future experiments must beat this.

## Evaluation
**Primary metric:** Accuracy
**Validation:** Stratified 5-fold cross-validation
**Success threshold:** 97% accuracy
