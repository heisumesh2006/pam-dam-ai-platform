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
    "tickets"
]

for i in range(100000):

    role = random.choice(roles)

    department = random.choice(
        departments
    )

    high_risk = random.random() < 0.1

    medium_risk = random.random() < 0.2

    db = random.choice(
        databases
    )

    if high_risk:

        table = random.choice(
            sensitive_tables
        )

        query_type = random.choice(
            ["SELECT","DELETE"]
        )

        rows_accessed = random.randint(
            100000,
            1000000
        )

        execution_time = random.randint(
            2000,
            15000
        )

        sensitive = True

        download_size = round(
            random.uniform(
                100,
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

        country = random.choice([
            "Russia",
            "Germany",
            "Brazil",
            "Netherlands",
            "Singapore"
        ])

        risk = "HIGH"

    elif medium_risk:

        table = random.choice(
            sensitive_tables +
            normal_tables
        )

        query_type = random.choice(
            ["SELECT","UPDATE"]
        )

        rows_accessed = random.randint(
            1000,
            50000
        )

        execution_time = random.randint(
            500,
            3000
        )

        sensitive = table in sensitive_tables

        download_size = round(
            random.uniform(
                10,
                100
            ),
            2
        )

        failed_queries = random.randint(
            1,
            3
        )

        query_frequency = random.randint(
            10,
            30
        )

        country = random.choice([
            "India",
            "Germany",
            "Brazil"
        ])

        risk = "MEDIUM"

    else:

        table = random.choice(
            normal_tables
        )

        query_type = random.choice(
            [
                "SELECT",
                "INSERT",
                "UPDATE"
            ]
        )

        rows_accessed = random.randint(
            1,
            1000
        )

        execution_time = random.randint(
            10,
            500
        )

        sensitive = False

        download_size = round(
            random.uniform(
                0,
                10
            ),
            2
        )

        failed_queries = random.randint(
            0,
            1
        )

        query_frequency = random.randint(
            1,
            10
        )

        country = "India"

        risk = "LOW"

    query_templates = {

        "SELECT":
            f"SELECT * FROM {table}",

        "UPDATE":
            f"UPDATE {table} SET status='active'",

        "DELETE":
            f"DELETE FROM {table}",

        "INSERT":
            f"INSERT INTO {table} VALUES (...)"
    }

    query_text = query_templates[
        query_type
    ]

    hour = random.randint(
        0,
        23
    )

    day = fake.day_of_week()

    weekend = day in [
        "Saturday",
        "Sunday"
    ]

    privileged_user = role in [
        "Admin",
        "DBA"
    ]

    behavior_score = round(
        (
            failed_queries*8 +
            query_frequency*1.5 +
            rows_accessed/10000 +
            download_size/10
        ),
        2
    )

    records.append({

        "query_id":
            f"QRY{i:06}",

        "user_id":
            f"USR{random.randint(1,1200):05}",

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

        "query_text":
            query_text,

        "rows_accessed":
            rows_accessed,

        "execution_time_ms":
            execution_time,

        "timestamp":
            fake.date_time_this_year(),

        "hour":
            hour,

        "day_of_week":
            day,

        "weekend_access":
            weekend,

        "source_ip":
            fake.ipv4(),

        "country":
            country,

        "device_type":
            random.choice([
                "Windows Laptop",
                "MacBook",
                "Linux Workstation",
                "Tablet",
                "Mobile"
            ]),

        "sensitive_table":
            sensitive,

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
    "dam_query_dataset.csv",
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

print("\nAverage Rows Accessed")
print(
    round(
        df["rows_accessed"]
        .mean(),
        2
    )
)