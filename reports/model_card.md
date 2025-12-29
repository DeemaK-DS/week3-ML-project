# Model Card — Week 3 Baseline

## Problem
- Predict: final grade (A, B, C, D, F) for each student
- Decision enabled: identify students at risk and support academic interventions
- Constraints: CPU-only; offline-first; batch inference

## Data (contract)
- Feature table: data/processed/features.csv
- Unit of analysis: one row per student
- Target column: grade (multiclass: A, B, C, D, F)
- Optional IDs (passthrough): user_id
