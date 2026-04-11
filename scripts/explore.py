"""Iris dataset exploration script."""

import pandas as pd
import numpy as np

COLUMNS = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
DATA_PATH = "data/iris.data"

df = pd.read_csv(DATA_PATH, header=None, names=COLUMNS)

# Drop any trailing blank rows (iris.data has a trailing newline)
df = df.dropna(how="all")

print("=" * 60)
print("1. SHAPE & SCHEMA")
print("=" * 60)
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print()
print(df.dtypes.to_string())

print()
print("=" * 60)
print("2. TARGET VARIABLE: species")
print("=" * 60)
counts = df["species"].value_counts()
print(counts.to_string())
ratio = counts.max() / counts.min()
print(f"\nMax/min class ratio: {ratio:.2f}:1", "(IMBALANCED)" if ratio > 3 else "(balanced)")

print()
print("=" * 60)
print("3. MISSING VALUES")
print("=" * 60)
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({"count": missing, "pct": missing_pct})
print(missing_df.to_string())
flagged = missing_pct[missing_pct > 10]
if len(flagged):
    print(f"\nFLAGGED (>10% missing): {list(flagged.index)}")
else:
    print("\nNo columns with >10% missing.")

print()
print("=" * 60)
print("4. FEATURE DISTRIBUTIONS")
print("=" * 60)
features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
print(df[features].describe().round(3).to_string())

# Zero-variance check
zero_var = [c for c in features if df[c].std() == 0]
if zero_var:
    print(f"\nZero-variance columns: {zero_var}")
else:
    print("\nNo zero-variance columns.")

# Outliers (>3 std from mean)
print("\nOutliers (>3 std from mean):")
for c in features:
    mean, std = df[c].mean(), df[c].std()
    outliers = df[(df[c] - mean).abs() > 3 * std]
    if len(outliers):
        print(f"  {c}: {len(outliers)} outlier(s)")
    else:
        print(f"  {c}: none")

# Correlation
print("\nFeature correlation matrix:")
corr = df[features].corr().round(3)
print(corr.to_string())

# Highly correlated pairs
print("\nHighly correlated pairs (|r| > 0.95):")
found = False
for i in range(len(features)):
    for j in range(i + 1, len(features)):
        r = corr.iloc[i, j]
        if abs(r) > 0.95:
            print(f"  {features[i]} & {features[j]}: r={r}")
            found = True
if not found:
    print("  None")

print()
print("=" * 60)
print("5. LEAKAGE CHECK")
print("=" * 60)
# Check for suspiciously high correlation with encoded target
df["_target_encoded"] = df["species"].astype("category").cat.codes
for c in features:
    r = df[c].corr(df["_target_encoded"])
    if abs(r) > 0.95:
        print(f"  WARNING: {c} has r={r:.3f} with target (potential leakage)")
# petal_length/petal_width are highly correlated with target — expected, not leakage
print("  petal_length and petal_width are highly predictive (expected for iris).")
print("  No leakage concerns — all features are physical measurements.")
df.drop(columns=["_target_encoded"], inplace=True)

print()
print("=" * 60)
print("6. DATA QUALITY")
print("=" * 60)
dupes = df.duplicated().sum()
print(f"Duplicate rows: {dupes}")
if dupes:
    print(df[df.duplicated(keep=False)])

# Mixed types check
for c in df.columns:
    types = df[c].apply(type).nunique()
    if types > 1:
        print(f"  Mixed types in {c}: {df[c].apply(type).value_counts().to_dict()}")

print("\nDone.")
