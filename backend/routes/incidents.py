from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Incident

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.get("/")
def get_incidents(
    db: Session = Depends(get_db)
):

    incidents = db.query(Incident).order_by(
        Incident.id.desc()
    ).all()

    return incidents