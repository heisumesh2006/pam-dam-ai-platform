import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv("../../data/pam/pam_login_dataset_v2_final.csv")

categorical_cols = [
    "role",
    "department",
    "country",
    "city",
    "device_type"
]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

bool_cols = [
    "device_trusted",
    "vpn_used",
    "mfa_enabled",
    "login_success",
    "privileged_account",
    "critical_system_access",
    "weekend_login"
]

for col in bool_cols:
    df[col] = df[col].astype(int)

features = [
    "role",
    "department",
    "login_hour",
    "device_type",
    "device_trusted",
    "country",
    "vpn_used",
    "failed_attempts",
    "mfa_enabled",
    "login_success",
    "session_duration_minutes",
    "privileged_account",
    "critical_system_access",
    "previous_risk_score",
    "jit_requests_last_30_days",
    "number_of_alerts",
    "number_of_sessions",
    "weekend_login",
    "login_frequency_last_7_days",
    "behavior_anomaly_score"
]

X = df[features]

model = IsolationForest(
    n_estimators=300,
    contamination=0.05,
    random_state=42
)

model.fit(X)

predictions = model.predict(X)

df["anomaly"] = predictions

df["anomaly"] = df["anomaly"].map({
    1:0,
    -1:1
})

df["actual"] = df["risk_label"].apply(
    lambda x: 1 if x=="HIGH" else 0
)

accuracy = accuracy_score(
    df["actual"],
    df["anomaly"]
)

precision = precision_score(
    df["actual"],
    df["anomaly"]
)

recall = recall_score(
    df["actual"],
    df["anomaly"]
)

f1 = f1_score(
    df["actual"],
    df["anomaly"]
)

print("\n===== PAM ANOMALY MODEL =====\n")

print("Accuracy :",round(accuracy,4))
print("Precision:",round(precision,4))
print("Recall   :",round(recall,4))
print("F1 Score :",round(f1,4))

print("\nConfusion Matrix\n")
print(
    confusion_matrix(
        df["actual"],
        df["anomaly"]
    )
)

print("\nClassification Report\n")
print(
    classification_report(
        df["actual"],
        df["anomaly"]
    )
)

print("\nAnomalies Detected")
print(
    df["anomaly"].value_counts()
)

joblib.dump(
    model,
    "../../models/pam/pam_isolation_forest.pkl"
)

print("\nModel Saved:")
print("pam_isolation_forest.pkl")