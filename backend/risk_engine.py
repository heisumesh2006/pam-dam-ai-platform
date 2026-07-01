def calculate_risk(pam_anomaly: bool, dam_anomaly: bool):

    if not pam_anomaly and not dam_anomaly:
        return {
            "threat_level": "LOW",
            "risk_score": 20,
            "recommended_action": "Continue Monitoring"
        }

    if pam_anomaly and not dam_anomaly:
        return {
            "threat_level": "MEDIUM",
            "risk_score": 60,
            "recommended_action": "Review Privileged Session"
        }

    if not pam_anomaly and dam_anomaly:
        return {
            "threat_level": "HIGH",
            "risk_score": 85,
            "recommended_action": "Investigate Database Activity"
        }

    return {
        "threat_level": "CRITICAL",
        "risk_score": 100,
        "recommended_action": "Terminate Session Immediately"
    }