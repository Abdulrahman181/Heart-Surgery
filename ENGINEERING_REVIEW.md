# Engineering Review — `Abdulrahman181/Heart-Surgery`

**Review scope:** every tracked Python/notebook/README/dependency file in the repository at review time. The repository contained one Jupyter notebook, `README.md`, `requirements.txt`, and `.gitignore`; it did not contain standalone Python application modules or the source CSV.

## Executive summary

The original notebook was an exploratory artifact with a working outline but was not a reliable, portable training workflow. It used relative data paths without schema checks, fit imputers/scalers on all rows before splitting, depended on undeclared `xgboost`, TensorFlow, and Keras packages, mutated categorical columns with `LabelEncoder`, used a duplicate observed-mortality column where an observed/expected comparison was intended, and reported only accuracy without class-balance context. The original notebook also retained execution metadata and did not provide a dependency-free static check.

The notebook has been rewritten into a top-to-bottom, data-gated workflow. It now validates the input schema, reports a clear message when the licensed CSV is absent, keeps the optional image non-fatal, handles year parsing portably, performs descriptive analysis without global model imputation, and uses a scikit-learn `Pipeline`/`ColumnTransformer` so imputation and one-hot encoding are fit on `X_train` only. The baseline is deterministic (`RANDOM_STATE = 42`), uses stratification when possible, and reports accuracy, balanced accuracy, a classification report, and a confusion matrix.

## Findings and disposition

| Area | Finding in original repository | Disposition |
|---|---|---|
| Data availability | The dataset was not committed and the prior `pd.read_csv` call exposed only a raw file error. | Added `CARDIAC_SURGERY_DATA` configuration, default path behavior, a clear `FileNotFoundError`, required-column validation, and documentation that no metrics are claimed without the licensed data. |
| Portability | Banner and CSV paths were implicit relative paths; fixed-column dropping failed when optional columns were absent. | Added `Path`-based environment configuration and `errors="ignore"` for optional identifiers. |
| Missing values and leakage | `KNNImputer` and `StandardScaler` were fit before the train/test split, leaking information from held-out rows. The autoencoder was fit on all rows and was not used to filter or correct data. | Removed the unnecessary autoencoder/TensorFlow/Keras path. Numeric median and categorical most-frequent imputers now live inside the training pipeline. |
| Categorical preprocessing | `LabelEncoder` was reused for feature columns and mutated the analysis frame; unknown categories were not handled. | Replaced with `OneHotEncoder(handle_unknown="ignore")` in a `ColumnTransformer`; the original analysis data remains suitable for EDA. |
| Model dependencies | `xgboost` was imported but absent from `requirements.txt`; TensorFlow/Keras were listed despite not being needed for a defensible baseline. | Replaced XGBoost with declared scikit-learn `LogisticRegression` and removed unnecessary heavy dependencies. Added direct notebook/runtime dependencies, JupyterLab, IPython, and Ruff. |
| Target/split | No target-class validation, no stratification, no fixed model seed, and no guard for too-small labeled data. | Added guards for labeled row count and class count, fixed `random_state`, and conditional stratification with an explicit warning when a class is too rare. |
| Metrics | Only accuracy was printed (and the original comparison call reversed arguments); the plot duplicated `Observed Mortality Rate` while claiming observed-vs-expected. | Added balanced accuracy, classification report, confusion matrix, and corrected observed/expected aggregation and labeling. |
| Notebook hygiene | The original notebook contained stale execution metadata from prior runs (its stored outputs were empty) and no static validation command. | Rebuilt with all outputs empty and execution counts unset. Added `validate_notebook.py` and `tests/test_static_validation.py`. |

## Files changed or added

- `cardiac-surgery-and-percutaneous (1).ipynb` — portable EDA and leakage-safe baseline classifier; stale outputs removed.
- `README.md` — data schema, setup, validation commands, reproducibility, and limitations.
- `requirements.txt` — declared, lighter runtime and validation dependencies; removed undeclared/unneeded XGBoost/TensorFlow/Keras requirements.
- `.gitignore` — added common cache and generated-artifact exclusions.
- `validate_notebook.py` — dependency-free JSON/AST/static notebook validator.
- `tests/test_static_validation.py` — two standard-library unit tests for notebook presence and static validity.
- `ENGINEERING_REVIEW.md` — this review.

## Validation performed

All checks below were run in the repository working tree:

```text
python validate_notebook.py
Notebook validation passed: /home/ubuntu/github_priority/Heart-Surgery/cardiac-surgery-and-percutaneous (1).ipynb

python -m unittest discover -s tests -v
Ran 2 tests in 0.002s — OK

ruff check validate_notebook.py tests
All checks passed!

ruff check --select E9,F821 'cardiac-surgery-and-percutaneous (1).ipynb'
All checks passed!
```

The notebook's code cells were also parsed with Python AST as part of the validator. All code-cell outputs are empty and execution counts are unset.

## Execution caveat

A full notebook run was **not claimed**: the repository does not contain `data/cardiac-surgery.csv`, and the environment does not have the project's ML stack installed. Installing dependencies or obtaining the licensed dataset was outside this audit. Consequently, no numerical model result, chart result, or data-quality conclusion is presented as an observed result here. After supplying the CSV, run the notebook from top to bottom and review class balance and schema before interpreting any metrics.
