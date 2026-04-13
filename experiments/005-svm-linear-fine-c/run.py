import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold, GridSearchCV, cross_val_score

# Load data
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv("data/iris.data", header=None, names=columns)

X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

# Pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("svc", SVC(kernel="linear", random_state=42)),
])

# Fine C grid around the winning C=10 from experiment 004
param_grid = {
    "svc__C": [1, 3, 5, 7, 10, 15, 20, 30, 50, 100],
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid = GridSearchCV(pipe, param_grid, cv=cv, scoring="accuracy", refit=True)
grid.fit(X, y)

print("Experiment 005: Linear SVM + Scaling + Fine C Grid")
print("=" * 50)
print(f"\nBest params: {grid.best_params_}")
print(f"Best CV accuracy: {grid.best_score_:.4f}")

# Per-fold results for best params
best_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("svc", SVC(kernel="linear", C=grid.best_params_["svc__C"], random_state=42)),
])
scores = cross_val_score(best_pipe, X, y, cv=cv, scoring="accuracy")

print(f"\nPrimary metric (Accuracy): {scores.mean():.4f}")
print(f"\nPer-fold results:")
for i, s in enumerate(scores, 1):
    print(f"  Fold {i}: {s:.4f}")
print(f"\nMean: {scores.mean():.4f} (+/- {scores.std():.4f})")
