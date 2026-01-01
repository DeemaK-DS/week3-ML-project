# Week 3 — Baseline ML System (Train + Evaluate + Predict)

This project aims to **predict students’ academic grades** using a **baseline machine learning system** built with a clean, CLI-driven workflow.  
It demonstrates end-to-end ML system design, including synthetic data generation, reproducible model training with versioned artifacts, and batch prediction with schema guardrails.

## Data Description

This project uses a **synthetic student performance dataset** generated for educational and demonstration purposes.

### Unit of analysis
- One row represents **one student**

### Identifier
- **`student_id`**
  - Unique identifier for each student
  - Treated as a **passthrough ID**
  - Not used as a model feature, but preserved in prediction outputs

### Features
The following columns are used as **model features (X)**:
- **`study_hours`** – number of hours spent studying
- **`gender`** – student gender (categorical)
- **`marks`** – numeric exam score
- **`father_edu`** – father’s education level
- **`mother_edu`** – mother’s education level

### Target variable
- **`grade`** (classification target)
  - Represents the student’s final academic outcome
  - Used as the label during model training and evaluation

### Data format
- Input data is stored under `data/processed/`
- Supported formats:
  - CSV (`.csv`)
  - Parquet (`.parquet`)

### Notes
- The dataset is **synthetic and not representative of real students**
- It is designed to demonstrate:
  - feature/target separation
  - reproducible training
  - batch prediction using a CLI-based ML system



## Quickstart

### 1) Setup
```bash
uv sync
```

### 2) Create sample data (if needed)
```bash
uv run ml-baseline make-sample-data
```

This writes a small demo feature table to:
- `data/processed/features.csv` (and `.parquet` if available)

### 3) Train a baseline model
```bash
uv run ml-baseline train --target grade
```

Artifacts are written to:
- `models/runs/<run_id>/...`
- `models/registry/latest.txt` points to the most recent run

### 4) Batch predict
```bash
uv run ml-baseline predict --run latest --input data/processed/features_infer.csv --output outputs/preds.csv
```

### 5) Tests
```bash
uv run pytest
```
The system is considered successful when training artifacts are saved under models/runs/, the latest run is registered, batch predictions are written to outputs/preds.csv, and all tests pass

---
