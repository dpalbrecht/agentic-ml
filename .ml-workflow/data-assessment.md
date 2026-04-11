# Data Assessment

## Overview
150 rows, 5 columns (4 numeric features + 1 target), single file `data/iris.data` (CSV, no header).

## Target: species
Perfectly balanced 3-class distribution:
- Iris-setosa: 50
- Iris-versicolor: 50
- Iris-virginica: 50

## Features

| Column | dtype | Missing % | Notes |
|--------|-------|-----------|-------|
| sepal_length | float64 | 0% | |
| sepal_width | float64 | 0% | 1 outlier (>3 std) |
| petal_length | float64 | 0% | Highly correlated with petal_width (r=0.963) |
| petal_width | float64 | 0% | Highly correlated with petal_length (r=0.963) |

## Issues Found
- 3 duplicate rows (2 setosa duplicates of row 9, 1 virginica duplicate of row 101). Known issue with this dataset — not a data pipeline error.
- petal_length and petal_width are highly correlated (r=0.963). Consider whether both are needed, though with only 4 features this is unlikely to cause problems.

## Leakage Risk
None identified. All four features are physical measurements taken at the same time as the class label. No temporal, ID, or derived features present.

## Recommended Feature Set
Use all four features: sepal_length, sepal_width, petal_length, petal_width. With only 4 features and 150 samples, there is no reason to drop any. The high petal correlation is noted but not actionable at this scale.

---
*Assessed on: 2026-04-10*
