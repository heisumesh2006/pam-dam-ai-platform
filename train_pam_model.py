import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error,r2_score
import joblib

df = pd.read_csv("pam_login_dataset.csv")

target_map = {
    "LOW":20,
    "MEDIUM":60,
    "HIGH":90
}

df["risk_score"] = df["risk_label"].map(target_map)

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
y = df["risk_score"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train,y_train)

pred = model.predict(X_test)

print("MAE:",mean_absolute_error(y_test,pred))
print("R2:",r2_score(y_test,pred))

joblib.dump(model,"pam_risk_model.pkl")

print("\nModel Saved:")
print("pam_risk_model.pkl")