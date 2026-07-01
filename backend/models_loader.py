import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAM_RISK_MODEL = os.path.join(
    BASE_DIR,
    "models",
    "pam",
    "pam_risk_model.pkl"
)

PAM_ANOMALY_MODEL = os.path.join(
    BASE_DIR,
    "models",
    "pam",
    "pam_isolation_forest.pkl"
)

DAM_ANOMALY_MODEL = os.path.join(
    BASE_DIR,
    "models",
    "dam",
    "dam_isolation_forest.pkl"
)


class ModelLoader:

    def __init__(self):

        print("=" * 50)
        print("Loading AI Models...")
        print("=" * 50)

        self.pam_risk_model = self.load(PAM_RISK_MODEL, "PAM Risk Model")

        self.pam_anomaly_model = self.load(
            PAM_ANOMALY_MODEL,
            "PAM Anomaly Model"
        )

        self.dam_anomaly_model = self.load(
            DAM_ANOMALY_MODEL,
            "DAM Anomaly Model"
        )

        print("=" * 50)
        print("All models loaded successfully.")
        print("=" * 50)

    def load(self, path, name):

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"{name} not found:\n{path}"
            )

        print(f"Loading {name}...")

        model = joblib.load(path)

        print(f"✓ {name} Loaded")

        return model


models = ModelLoader()