from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pandas as pd

from schemas import PAMRequest
from models_loader import models
from database.database import get_db
from database.crud import create_incident

router = APIRouter(
    prefix="/predict",
    tags=["PAM"]
)


@router.post("/pam-anomaly")
def predict_pam_anomaly(
    data: PAMRequest,
    db: Session = Depends(get_db)
):

    sample = pd.DataFrame([data.model_dump()])

    prediction = int(
        models.pam_anomaly_model.predict(sample)[0]
    )

    anomaly = prediction == -1

    if anomaly:
        threat = "MEDIUM"
        action = "Review Privileged Session"
    else:
        threat = "LOW"
        action = "Continue Monitoring"

    create_incident(
        db=db,
        source="PAM",
        anomaly=anomaly,
        threat_level=threat,
        recommended_action=action
    )

    return {
        "model": "PAM Isolation Forest",
        "anomaly": anomaly,
        "threat_level": threat,
        "recommended_action": action
    }