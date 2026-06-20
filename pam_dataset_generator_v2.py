from faker import Faker
import pandas as pd
import random
import numpy as np

fake = Faker()

NUM_USERS = 1000

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
    "Hyderabad",
    "Chennai"
]

foreign_locations = [
    ("Germany", "Berlin"),
    ("Singapore", "Singapore"),
    ("Brazil", "Sao Paulo"),
    ("Netherlands", "Amsterdam"),
    ("Russia", "Moscow")
]

records = []

for user_num in range(NUM_USERS):

    user_id = f"USR{user_num:05}"

    role = random.choice(roles)

    department = random.choice(departments)

    username = fake.user_name()

    user_type = random.choices(
        [
            "NORMAL",
            "POWER",
            "SUSPICIOUS",
            "INSIDER"
        ],
        weights=[65, 15, 10, 10]
    )[0]

    home_city = random.choice(indian_cities)

    trusted_device = random.choice([
        "Windows Laptop",
        "MacBook",
        "Linux Workstation"
    ])

    event_count = random.randint(
        120,
        180
    )

    drift_start = int(
        event_count * 0.7
    )

    for event in range(event_count):

        country = "India"
        city = home_city

        vpn_used = False

        failed_attempts = 0

        alerts = 0

        jit_requests = 0

        sessions = random.randint(
            1,
            5
        )

        critical_system = False

        privileged = role in [
            "Admin",
            "DBA"
        ]

        if user_type == "NORMAL":

            login_hour = random.randint(
                8,
                18
            )

            previous_risk_score = round(
                random.uniform(0, 25),
                2
            )

            risk = "LOW"

        elif user_type == "POWER":

            if role in [
                "DBA",
                "Admin"
            ]:

                login_hour = random.choice([
                    1, 2, 3, 4,
                    22, 23
                ])

                sessions = random.randint(
                    10,
                    25
                )

                critical_system = True

                jit_requests = random.randint(
                    1,
                    4
                )

                previous_risk_score = round(
                    random.uniform(
                        15,
                        40
                    ),
                    2
                )

                risk = random.choice([
                    "LOW",
                    "MEDIUM"
                ])

            else:

                login_hour = random.randint(
                    7,
                    20
                )

                previous_risk_score = round(
                    random.uniform(
                        15,
                        40
                    ),
                    2
                )

                risk = "LOW"

        elif user_type == "SUSPICIOUS":

            if random.random() < 0.6:

                country, city = random.choice(
                    foreign_locations
                )

            vpn_used = random.choice([
                True,
                False
            ])

            failed_attempts = random.randint(
                1,
                5
            )

            login_hour = random.randint(
                0,
                23
            )

            previous_risk_score = round(
                random.uniform(
                    30,
                    70
                ),
                2
            )

            risk = "MEDIUM"

        else:

            login_hour = random.randint(
                8,
                18
            )

            if event > drift_start:

                alerts = random.randint(
                    5,
                    15
                )

                jit_requests = random.randint(
                    8,
                    20
                )

                sessions = random.randint(
                    15,
                    40
                )

                critical_system = True

                previous_risk_score = round(
                    random.uniform(
                        60,
                        95
                    ),
                    2
                )

                if random.random() < 0.7:
                    risk = "HIGH"
                else:
                    risk = "MEDIUM"

            else:

                previous_risk_score = round(
                    random.uniform(
                        10,
                        30
                    ),
                    2
                )

                if random.random() < 0.2:
                    risk = "MEDIUM"
                else:
                    risk = "LOW"

        if random.random() < 0.08:

            risk = random.choice([
                "LOW",
                "MEDIUM",
                "HIGH"
            ])

        day = fake.day_of_week()

        weekend = day in [
            "Saturday",
            "Sunday"
        ]

        behavior_score = round(
            (
                failed_attempts * 4 +
                alerts * 3 +
                jit_requests * 2 +
                previous_risk_score * 0.4 +
                sessions * 0.5
            ),
            2
        )

        records.append({

            "user_id": user_id,

            "username": username,

            "role": role,

            "department": department,

            "login_timestamp":
                fake.date_time_this_year(),

            "login_hour":
                login_hour,

            "day_of_week":
                day,

            "device_type":
                trusted_device,

            "device_trusted":
                True if random.random() > 0.1 else False,

            "ip_address":
                fake.ipv4(),

            "country":
                country,

            "city":
                city,

            "vpn_used":
                vpn_used,

            "failed_attempts":
                failed_attempts,

            "mfa_enabled":
                random.choice([
                    True,
                    True,
                    False
                ]),

            "login_success":
                random.choice([
                    True,
                    True,
                    True,
                    False
                ]),

            "session_duration_minutes":
                random.randint(
                    15,
                    500
                ),

            "privileged_account":
                privileged,

            "critical_system_access":
                critical_system,

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
                random.randint(
                    1,
                    25
                ),

            "behavior_anomaly_score":
                behavior_score,

            "risk_label":
                risk
        })

df = pd.DataFrame(records)

df.to_csv(
    "pam_login_dataset_v2.csv",
    index=False
)

print("\nShape")
print(df.shape)

print("\nRisk Distribution")
print(
    df["risk_label"]
    .value_counts()
)

print("\nUnique Users")
print(
    df["user_id"].nunique()
)