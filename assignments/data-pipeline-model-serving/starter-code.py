import os
from typing import List

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

DATA_PATH = "data.csv"
MODEL_PATH = "model.joblib"

app = FastAPI()


class FeatureInput(BaseModel):
    feature1: float
    feature2: float


def load_data(path: str = DATA_PATH):
    df = pd.read_csv(path)
    X = df[["feature1", "feature2"]]
    y = df["label"]
    return X, y


def train_and_save_model(path: str = DATA_PATH, model_path: str = MODEL_PATH):
    X, y = load_data(path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print("Model trained. Test accuracy:", acc)
    print(classification_report(y_test, preds))
    joblib.dump(model, model_path)
    return model


def load_model(model_path: str = MODEL_PATH):
    if not os.path.exists(model_path):
        return None
    return joblib.load(model_path)


@app.on_event("startup")
def startup_event():
    global MODEL
    MODEL = load_model()
    if MODEL is None:
        print("No model found — training a new model from data.csv")
        MODEL = train_and_save_model()
    else:
        print("Loaded model from", MODEL_PATH)


@app.get("/")
def read_root():
    return {"message": "Data Pipeline & Model Serving assignment — FastAPI model server"}


@app.post("/predict")
def predict(input: FeatureInput):
    if MODEL is None:
        raise HTTPException(status_code=500, detail="Model not available")
    features = [[input.feature1, input.feature2]]
    try:
        pred = MODEL.predict(features)[0]
        proba = MODEL.predict_proba(features).max()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"prediction": int(pred), "probability": float(proba)}


if __name__ == "__main__":
    # When run directly, train (if needed) and start the server
    if not os.path.exists(MODEL_PATH):
        train_and_save_model()
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
