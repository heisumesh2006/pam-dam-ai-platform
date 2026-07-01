from database.models import Incident


def create_incident(
    db,
    source,
    anomaly,
    threat_level,
    recommended_action
):

    incident = Incident(
        source=source,
        anomaly=anomaly,
        threat_level=threat_level,
        recommended_action=recommended_action
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident