# 📘 Assignment: Data Pipeline & Model Serving with FastAPI

## 🎯 Objective

Build an end-to-end data pipeline: clean and transform a small dataset, train a simple scikit-learn model, and expose prediction endpoints with FastAPI. Students will learn reproducible training, basic evaluation, and how to serve models as an API (plus a Dockerfile for containerization).

## ⏳ Suggested Duration

2 weeks (core tasks + extension tasks)

## 📝 Tasks

### 🛠️ 1 — Data cleaning & exploration

#### Description
Load the provided CSV, inspect missing values, and apply simple cleaning and feature transformations.

#### Requirements

- Load `data.csv` using `pandas`.
- Handle or impute missing values sensibly.
- Scale or normalize features where appropriate.
- Output a short evaluation report (printed summary statistics and a train/test split score).

### 🛠️ 2 — Train a simple model

#### Description
Train a small scikit-learn model (e.g., Logistic Regression or RandomForest) to predict the target column.

#### Requirements

- Implement a training function that saves the trained model to `model.joblib`.
- Use a train/test split and report accuracy and a simple classification report.

### 🛠️ 3 — Serve predictions with FastAPI

#### Description
Create a FastAPI app that loads the trained model and exposes a prediction endpoint.

#### Requirements

- `GET /` returns a JSON welcome message and short assignment info.
- `POST /predict` accepts a JSON body with the feature values and returns a JSON prediction (class and probability).
- The app should load `model.joblib` on startup and return a helpful 400/500 error when requests are invalid.

### 🛠️ 4 — Containerize (optional but recommended)

#### Description
Add a `Dockerfile` so the model API can be run in a container.

#### Requirements

- Provide a minimal `Dockerfile` that installs dependencies and runs the FastAPI app with `uvicorn`.

## Starter code

Use `starter-code.py` as the entrypoint — it includes functions to load data, train a model, save the model, and run the FastAPI app.

## Files you will find

- `starter-code.py` — training + FastAPI app starter
- `data.csv` — small sample dataset
- `requirements.txt` — dependencies
- `Dockerfile` — optional container image

## Evaluation

- Working API that returns correct predictions for test inputs.
- Clear training script that produces `model.joblib` and prints evaluation metrics.
- Clean, readable code and brief README notes describing choices and how to run locally.

## Run locally (quick)

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Train and start the API (starter script will train if model missing):

```bash
python starter-code.py
```

3. Send a prediction request:

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"feature1": 1.2, "feature2": 3.4}'
```

## Extensions (optional)

- Add a `POST /train` endpoint to retrain the model from uploaded CSV.
- Add authentication for the API endpoints.
- Persist data in a lightweight DB (SQLite) and track model versions.
