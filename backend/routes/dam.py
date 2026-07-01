from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pandas as pd

from schemas import DAMRequest
from models_loader import models
from database.database import get_db
from database.crud import create_incident

router = APIRouter(
    prefix="/predict",
    tags=["DAM"]
)


@router.post("/dam-anomaly")
def predict_dam_anomaly(
    data: DAMRequest,
    db: Session = Depends(get_db)
):

    sample = pd.DataFrame([data.model_dump()])

    prediction = int(
        models.dam_anomaly_model.predict(sample)[0]
    )

    anomaly = prediction == -1

    if anomaly:
        threat = "HIGH"
        action = "Investigate Database Activity"
    else:
        threat = "LOW"
        action = "Continue Monitoring"

    create_incident(
        db=db,
        source="DAM",
        anomaly=anomaly,
        threat_level=threat,
        recommended_action=action
    )

    return {
        "model": "DAM Isolation Forest",
        "anomaly": anomaly,
        "threat_level": threat,
        "recommended_action": action
    }