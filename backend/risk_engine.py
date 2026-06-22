def calculate_risk(
    pam_score,
    dam_score
):

    final_score = (
        pam_score * 0.4 +
        dam_score * 0.6
    )

    if final_score < 40:

        level = "LOW"

    elif final_score < 75:

        level = "MEDIUM"

    else:

        level = "HIGH"

    return {
        "pam_score": round(
            pam_score,
            2
        ),
        "dam_score": round(
            dam_score,
            2
        ),
        "final_score": round(
            final_score,
            2
        ),
        "threat_level": level
    }


if __name__ == "__main__":

    result = calculate_risk(
        pam_score=65,
        dam_score=88
    )

    print("\n===== UNIFIED RISK =====\n")

    for k,v in result.items():
        print(
            f"{k}: {v}"
        )