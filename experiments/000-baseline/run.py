"""Experiment 000: Baseline — Logistic Regression on Iris dataset."""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Load data
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv("data/iris.data", header=None, names=columns)

X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

# Stratified 5-fold CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
model = LogisticRegression(max_iter=200)

scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")

print("=== Experiment 000: Baseline (Logistic Regression) ===")
print()
print("Per-fold accuracy:")
for i, s in enumerate(scores):
    print(f"  Fold {i+1}: {s:.4f}")
print()
print(f"Mean accuracy: {np.mean(scores):.4f} (+/- {np.std(scores):.4f})")
