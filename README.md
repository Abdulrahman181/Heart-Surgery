# Cardiac Surgery Analysis

This repository contains a reproducible machine-learning notebook for **Cardiac Surgery Analysis**.

## Data

The dataset is intentionally not committed because of size/licensing constraints. Required input: Cardiac surgery CSV and optional banner image.

Set the environment variable `CARDIAC_SURGERY_DATA` to the local dataset path before running the notebook. The notebook defaults to a `data/` path for local execution.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export CARDIAC_SURGERY_DATA=/absolute/path/to/data
jupyter notebook
```

Run cells from top to bottom. Generated models and caches should remain local and are excluded from version control.

## Limitations and cautions

- Reported metrics depend on the dataset split, random seed, preprocessing, and library versions.
- These notebooks are educational/research artifacts, not production or medical decision systems.
- Validate data schema and class balance before training; do not interpret predictions as professional advice.
