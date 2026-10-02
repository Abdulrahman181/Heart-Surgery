# Heart Surgery Exploratory Analysis

This repository contains an exploratory Jupyter notebook analyzing cardiac surgery and percutaneous coronary intervention outcomes. It is **not** a clinical decision-support tool, and its analyses should not be interpreted as clinical guidance.

## Required input data

The source CSV is not included in this repository. The notebook expects the file named:

`cardiac-surgery-and-percutaneous-coronary-interventions-by-hospital-beginning-2008-1.csv`

Place a copy obtained from an authorized source at `data/<filename>` in the repository. The notebook also recognizes the original Kaggle input location when running in Kaggle. If neither location exists, it stops with an explanatory `FileNotFoundError`. This repository does not include credentials or automate dataset downloads; do not commit API keys or other credentials.

A banner image is optional. If you have the image, place it at `assets/Cardiac-Surgery-banner.webp`; in Kaggle, the original `/kaggle/input/picture/` location is also checked. The notebook continues without the image if it is unavailable.

## Environment and running

Use Python 3.10 or newer and install Jupyter plus the notebook's imported libraries (NumPy, pandas, Matplotlib, seaborn, scikit-learn, TensorFlow/Keras, and XGBoost). For example:

```bash
python -m pip install jupyter numpy pandas matplotlib seaborn scikit-learn tensorflow xgboost
jupyter lab
```

Open `cardiac-surgery-and-percutaneous (1).ipynb` and run its cells from top to bottom after supplying the CSV. Dependency versions are not currently locked, and the notebook has not been executed end-to-end in this repository because its input data is not present.

## Validation and limitations

Run the repository's local syntax check with:

```bash
python -m unittest discover -s tests -v
```

This check validates notebook JSON and Python syntax only. It does not validate the analysis, train the model, or establish predictive performance. The notebook uses an external dataset, and its reported/visual analyses should be regenerated from a known input before relying on them. No dataset is redistributed here; verify source permissions and documentation before use.
