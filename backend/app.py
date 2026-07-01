from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas import PAMRequest
from models_loader import models

import pandas as pd

app = FastAPI(
    title="PAM-DAM AI Security API",
    version="1.0.0",
    description="AI Powered PAM & DAM Security Platform"
)


@app.get("/")
def home():
    return {
        "project": "PAM-DAM AI Security Platform",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "models": {
            "pam_risk_model": "Loaded",
            "pam_anomaly_model": "Loaded",
            "dam_anomaly_model": "Loaded"
        }
    }


@app.post("/predict/pam-risk")
def predict_pam_risk(data: PAMRequest):

    sample = pd.DataFrame([data.model_dump()])

    score = float(
        models.pam_risk_model.predict(sample)[0]
    )

    if score < 40:
        level = "LOW"
    elif score < 75:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return JSONResponse(
        {
            "risk_score": round(score,2),
            "risk_level": level
        }
    )


@app.post("/predict/pam-anomaly")
def predict_pam_anomaly(data: PAMRequest):

    sample = pd.DataFrame([data.model_dump()])

    prediction = int(
        models.pam_anomaly_model.predict(sample)[0]
    )

    if prediction == -1:
        anomaly = True
    else:
        anomaly = False

    return JSONResponse(
        {
            "anomaly": anomaly,
            "raw_prediction": prediction
        }
    )