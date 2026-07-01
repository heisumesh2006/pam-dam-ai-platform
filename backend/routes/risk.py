from fastapi import APIRouter

from risk_engine import calculate_risk

router = APIRouter(
    prefix="/predict",
    tags=["Unified Risk"]
)


@router.get("/final")
def final_risk(
    pam_anomaly: bool,
    dam_anomaly: bool
):

    return calculate_risk(
        pam_anomaly,
        dam_anomaly
    )