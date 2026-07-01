from pydantic import BaseModel


class PAMRequest(BaseModel):
    role: int
    department: int
    login_hour: int
    device_type: int
    device_trusted: int
    country: int
    vpn_used: int
    failed_attempts: int
    mfa_enabled: int
    login_success: int
    session_duration_minutes: int
    privileged_account: int
    critical_system_access: int
    previous_risk_score: float
    jit_requests_last_30_days: int
    number_of_alerts: int
    number_of_sessions: int
    weekend_login: int
    login_frequency_last_7_days: int
    behavior_anomaly_score: float


class DAMRequest(BaseModel):
    role: int
    department: int
    database_name: int
    table_name: int
    query_type: int
    rows_accessed: int
    execution_time_ms: float
    hour: int
    weekend_access: int
    country: int
    device_type: int
    sensitive_table: int
    download_size_mb: float
    failed_query_attempts: int
    query_frequency_last_hour: int
    database_sensitivity: int
    privileged_user: int
    behavior_anomaly_score: float