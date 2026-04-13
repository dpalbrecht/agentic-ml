import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Load data
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv("data/iris.data", header=None, names=columns)

X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

# Model
model = SVC(kernel="rbf", random_state=42)

# Stratified 5-fold CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")

# Report
print("Experiment 002: SVM with RBF Kernel")
print("=" * 40)
print(f"\nPrimary metric (Accuracy): {scores.mean():.4f}")
print(f"\nPer-fold results:")
for i, s in enumerate(scores, 1):
    print(f"  Fold {i}: {s:.4f}")
print(f"\nMean: {scores.mean():.4f} (+/- {scores.std():.4f})")
