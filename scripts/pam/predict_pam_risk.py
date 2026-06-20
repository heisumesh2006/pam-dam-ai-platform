import pandas as pd
import joblib

model = joblib.load("pam_risk_model.pkl")

sample = pd.DataFrame([{
    "role":0,
    "department":0,
    "login_hour":3,
    "device_type":0,
    "device_trusted":0,
    "country":1,
    "vpn_used":1,
    "failed_attempts":8,
    "mfa_enabled":1,
    "login_success":1,
    "session_duration_minutes":120,
    "privileged_account":1,
    "critical_system_access":1,
    "previous_risk_score":85,
    "jit_requests_last_30_days":7,
    "number_of_alerts":4,
    "number_of_sessions":20,
    "weekend_login":1,
    "login_frequency_last_7_days":15,
    "behavior_anomaly_score":95
}])

score = model.predict(sample)[0]

if score < 40:
    level = "LOW"
elif score < 75:
    level = "MEDIUM"
else:
    level = "HIGH"

print(f"Risk Score: {score:.2f}")
print(f"Threat Level: {level}")