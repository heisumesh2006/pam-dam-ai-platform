def calculate_risk(
    pam_score: float,
    pam_anomaly: bool,
    dam_anomaly: bool
):

    final_score = pam_score

    if pam_anomaly:
        final_score += 10

    if dam_anomaly:
        final_score += 20

    final_score = min(final_score, 100)

    if final_score < 40:
        level = "LOW"
        action = "Continue Monitoring"

    elif final_score < 75:
        level = "MEDIUM"
        action = "Review User Activity"

    else:
        level = "HIGH"
        action = "Terminate Session Immediately"

    return {
        "pam_score": round(pam_score, 2),
        "pam_anomaly": pam_anomaly,
        "dam_anomaly": dam_anomaly,
        "final_score": round(final_score, 2),
        "threat_level": level,
        "recommended_action": action
    }


if __name__ == "__main__":

    result = calculate_risk(
        pam_score=82,
        pam_anomaly=True,
        dam_anomaly=True
    )

    print(result)