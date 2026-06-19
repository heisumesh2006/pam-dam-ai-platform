from faker import Faker
import pandas as pd
import random
import numpy as np

fake = Faker()

records = []

roles = [
    "Admin",
    "DBA",
    "Developer",
    "SecurityAnalyst",
    "Manager"
]

departments = [
    "IT",
    "Security",
    "Finance",
    "HR",
    "Operations"
]

indian_cities = [
    "Bengaluru",
    "Mumbai",
    "Delhi",
    "Pune",
    "Hyderabad"
]

foreign_locations = [
    ("Russia", "Moscow"),
    ("Germany", "Berlin"),
    ("Brazil", "Sao Paulo"),
    ("Netherlands", "Amsterdam"),
    ("Singapore", "Singapore")
]

for i in range(50000):

    role = random.choice(roles)
    dept = random.choice(departments)

    high_risk = random.random() < 0.1
    medium_risk = random.random() < 0.2

    if high_risk:

        country, city = random.choice(foreign_locations)

        login_hour = random.choice(
            [0,1,2,3,4,5,22,23]
        )

        device_trusted = False

        failed_attempts = random.randint(5,10)

        vpn_used = True

        privileged_account = role in [
            "Admin",
            "DBA"
        ]

        critical_system_access = True

        previous_risk_score = round(
            random.uniform(60,100),2
        )

        jit_requests = random.randint(3,10)

        alerts = random.randint(2,10)

        sessions = random.randint(10,30)

        risk = "HIGH"

    elif medium_risk:

        if random.random() < 0.5:
            country, city = random.choice(
                foreign_locations
            )
        else:
            country = "India"
            city = random.choice(
                indian_cities
            )

        login_hour = random.randint(
            6,20
        )

        device_trusted = random.choice(
            [True,False]
        )

        failed_attempts = random.randint(
            1,4
        )

        vpn_used = random.choice(
            [True,False]
        )

        privileged_account = role in [
            "Admin",
            "DBA"
        ]

        critical_system_access = random.choice(
            [True,False]
        )

        previous_risk_score = round(
            random.uniform(30,60),2
        )

        jit_requests = random.randint(1,5)

        alerts = random.randint(0,3)

        sessions = random.randint(2,10)

        risk = "MEDIUM"

    else:

        country = "India"

        city = random.choice(
            indian_cities
        )

        login_hour = random.randint(
            8,18
        )

        device_trusted = True

        failed_attempts = random.randint(
            0,1
        )

        vpn_used = False

        privileged_account = role in [
            "Admin",
            "DBA"
        ]

        critical_system_access = False

        previous_risk_score = round(
            random.uniform(0,30),2
        )

        jit_requests = random.randint(
            0,1
        )

        alerts = random.randint(
            0,1
        )

        sessions = random.randint(
            0,5
        )

        risk = "LOW"

    day = fake.day_of_week()

    weekend = day in [
        "Saturday",
        "Sunday"
    ]

    login_frequency = random.randint(
        1,20
    )

    behavior_anomaly_score = round(
        (
            failed_attempts*5 +
            alerts*8 +
            jit_requests*3 +
            previous_risk_score*0.5
        ),
        2
    )

    records.append({

        "user_id":f"USR{i:05}",

        "username":fake.user_name(),

        "role":role,

        "department":dept,

        "login_timestamp":fake.date_time_this_year(),

        "login_hour":login_hour,

        "day_of_week":day,

        "device_type":random.choice([
            "Windows Laptop",
            "MacBook",
            "Linux Workstation",
            "Tablet",
            "Mobile"
        ]),

        "device_trusted":device_trusted,

        "ip_address":fake.ipv4(),

        "country":country,

        "city":city,

        "vpn_used":vpn_used,

        "failed_attempts":failed_attempts,

        "mfa_enabled":random.choice([
            True,
            False
        ]),

        "login_success":random.choice([
            True,
            True,
            True,
            False
        ]),

        "session_duration_minutes":
            random.randint(10,500),

        "privileged_account":
            privileged_account,

        "critical_system_access":
            critical_system_access,

        "previous_risk_score":
            previous_risk_score,

        "jit_requests_last_30_days":
            jit_requests,

        "number_of_alerts":
            alerts,

        "number_of_sessions":
            sessions,

        "weekend_login":
            weekend,

        "login_frequency_last_7_days":
            login_frequency,

        "behavior_anomaly_score":
            behavior_anomaly_score,

        "risk_label":
            risk

    })

df = pd.DataFrame(records)

df.to_csv(
    "pam_login_dataset.csv",
    index=False
)

print(df.head())

print("\nShape")
print(df.shape)

print("\nRisk Distribution")
print(
    df["risk_label"]
    .value_counts()
)