from faker import Faker
import pandas as pd
import random

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

databases = [
    "HRDB",
    "FinanceDB",
    "CustomerDB",
    "PayrollDB",
    "AuditDB"
]

sensitive_tables = [
    "salary",
    "credit_cards",
    "bank_accounts",
    "employees",
    "customers"
]

normal_tables = [
    "logs",
    "products",
    "inventory",
    "attendance",
    "tickets",
    "assets",
    "vendors",
    "projects"
]

records = []

for user_num in range(NUM_USERS):

    user_id = f"USR{user_num:05}"

    role = random.choice(roles)

    department = random.choice(departments)

    user_type = random.choices(
        [
            "NORMAL",
            "POWER",
            "SUSPICIOUS",
            "INSIDER"
        ],
        weights=[60,15,15,10]
    )[0]

    event_count = random.randint(
        250,
        350
    )

    drift_start = int(
        event_count * 0.7
    )

    for event in range(event_count):

        db = random.choice(databases)

        country = "India"

        failed_queries = 0

        query_frequency = random.randint(
            1,
            10
        )

        privileged_user = role in [
            "Admin",
            "DBA"
        ]

        if user_type == "NORMAL":

            table = random.choice(
                normal_tables
            )

            query_type = random.choice([
                "SELECT",
                "INSERT",
                "UPDATE"
            ])

            rows_accessed = random.randint(
                10,
                1000
            )

            download_size = round(
                random.uniform(
                    0,
                    10
                ),
                2
            )

            risk = "LOW"

        elif user_type == "POWER":

            if privileged_user:

                table = random.choice(
                    sensitive_tables
                )

                rows_accessed = random.randint(
                    1000,
                    50000
                )

                download_size = round(
                    random.uniform(
                        5,
                        50
                    ),
                    2
                )

                risk = random.choice([
                    "LOW",
                    "MEDIUM"
                ])

            else:

                table = random.choice(
                    normal_tables
                )

                rows_accessed = random.randint(
                    100,
                    5000
                )

                download_size = round(
                    random.uniform(
                        1,
                        20
                    ),
                    2
                )

                risk = "LOW"

            query_type = random.choice([
                "SELECT",
                "UPDATE"
            ])

        elif user_type == "SUSPICIOUS":

            table = random.choice(
                sensitive_tables +
                normal_tables
            )

            query_type = random.choice([
                "SELECT",
                "UPDATE",
                "DELETE"
            ])

            rows_accessed = random.randint(
                5000,
                100000
            )

            download_size = round(
                random.uniform(
                    20,
                    200
                ),
                2
            )

            failed_queries = random.randint(
                1,
                5
            )

            query_frequency = random.randint(
                10,
                30
            )

            risk = "MEDIUM"

        else:

            if event > drift_start:

                table = random.choice(
                    sensitive_tables
                )

                query_type = "SELECT"

                rows_accessed = random.randint(
                    100000,
                    1000000
                )

                download_size = round(
                    random.uniform(
                        200,
                        1000
                    ),
                    2
                )

                failed_queries = random.randint(
                    3,
                    10
                )

                query_frequency = random.randint(
                    30,
                    100
                )

                risk = "HIGH"

            else:

                table = random.choice(
                    normal_tables
                )

                query_type = random.choice([
                    "SELECT",
                    "UPDATE"
                ])

                rows_accessed = random.randint(
                    50,
                    2000
                )

                download_size = round(
                    random.uniform(
                        0,
                        10
                    ),
                    2
                )

                risk = "LOW"

        if random.random() < 0.10:

            risk = random.choice([
                "LOW",
                "MEDIUM",
                "HIGH"
            ])

        execution_time = random.randint(
            10,
            5000
        )

        behavior_score = round(
            (
                rows_accessed / 10000 +
                download_size / 10 +
                failed_queries * 5 +
                query_frequency * 1.5
            ),
            2
        )

        records.append({

            "query_id":
                f"QRY{len(records):06}",

            "user_id":
                user_id,

            "role":
                role,

            "department":
                department,

            "database_name":
                db,

            "table_name":
                table,

            "query_type":
                query_type,

            "rows_accessed":
                rows_accessed,

            "execution_time_ms":
                execution_time,

            "timestamp":
                fake.date_time_this_year(),

            "hour":
                random.randint(0,23),

            "day_of_week":
                fake.day_of_week(),

            "weekend_access":
                random.choice([
                    True,
                    False
                ]),

            "source_ip":
                fake.ipv4(),

            "country":
                country,

            "device_type":
                random.choice([
                    "Windows Laptop",
                    "MacBook",
                    "Linux Workstation"
                ]),

            "sensitive_table":
                table in sensitive_tables,

            "download_size_mb":
                download_size,

            "failed_query_attempts":
                failed_queries,

            "query_frequency_last_hour":
                query_frequency,

            "database_sensitivity":
                random.choice([
                    "LOW",
                    "MEDIUM",
                    "HIGH",
                    "CRITICAL"
                ]),

            "privileged_user":
                privileged_user,

            "behavior_anomaly_score":
                behavior_score,

            "risk_label":
                risk
        })

df = pd.DataFrame(records)

df.to_csv(
    "dam_query_dataset_v2.csv",
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