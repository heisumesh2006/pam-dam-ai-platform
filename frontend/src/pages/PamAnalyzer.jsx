import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

export default function PamAnalyzer() {

    const navigate = useNavigate();

    const [form, setForm] = useState({
        role: 0,
        department: 0,
        login_hour: 2,
        device_type: 0,
        device_trusted: 0,
        country: 1,
        vpn_used: 1,
        failed_attempts: 8,
        mfa_enabled: 1,
        login_success: 1,
        session_duration_minutes: 120,
        privileged_account: 1,
        critical_system_access: 1,
        previous_risk_score: 90,
        jit_requests_last_30_days: 7,
        number_of_alerts: 4,
        number_of_sessions: 20,
        weekend_login: 1,
        login_frequency_last_7_days: 15,
        behavior_anomaly_score: 95
    });

    const [result, setResult] = useState(null);

    const randomize = () => {

        setForm({

            role: Math.floor(Math.random() * 5),
            department: Math.floor(Math.random() * 5),
            login_hour: Math.floor(Math.random() * 24),
            device_type: Math.floor(Math.random() * 3),
            device_trusted: Math.round(Math.random()),
            country: Math.floor(Math.random() * 3),
            vpn_used: Math.round(Math.random()),
            failed_attempts: Math.floor(Math.random() * 10),
            mfa_enabled: Math.round(Math.random()),
            login_success: 1,
            session_duration_minutes: Math.floor(Math.random() * 180),
            privileged_account: Math.round(Math.random()),
            critical_system_access: Math.round(Math.random()),
            previous_risk_score: Math.floor(Math.random() * 100),
            jit_requests_last_30_days: Math.floor(Math.random() * 10),
            number_of_alerts: Math.floor(Math.random() * 5),
            number_of_sessions: Math.floor(Math.random() * 30),
            weekend_login: Math.round(Math.random()),
            login_frequency_last_7_days: Math.floor(Math.random() * 20),
            behavior_anomaly_score: Math.floor(Math.random() * 100)

        });

        setResult(null);

    };

    const analyze = async () => {

        const res = await api.post("/predict/pam-anomaly", form);

        setResult(res.data);

        setTimeout(() => {

            navigate("/");

        }, 2500);

    };

    return (

        <div className="min-h-screen bg-slate-950 text-white p-10">

            <h1 className="text-4xl font-bold mb-8">

                PAM Login Analyzer

            </h1>

            <div className="grid grid-cols-2 gap-5">

                <div>
                    <label>Role</label>
                    <input className="w-full p-2 rounded bg-slate-800"
                        value={form.role}
                        onChange={e => setForm({ ...form, role: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Login Hour</label>
                    <input className="w-full p-2 rounded bg-slate-800"
                        value={form.login_hour}
                        onChange={e => setForm({ ...form, login_hour: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Failed Attempts</label>
                    <input className="w-full p-2 rounded bg-slate-800"
                        value={form.failed_attempts}
                        onChange={e => setForm({ ...form, failed_attempts: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>VPN Used</label>
                    <input className="w-full p-2 rounded bg-slate-800"
                        value={form.vpn_used}
                        onChange={e => setForm({ ...form, vpn_used: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Trusted Device</label>
                    <input className="w-full p-2 rounded bg-slate-800"
                        value={form.device_trusted}
                        onChange={e => setForm({ ...form, device_trusted: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Behavior Score</label>
                    <input className="w-full p-2 rounded bg-slate-800"
                        value={form.behavior_anomaly_score}
                        onChange={e => setForm({ ...form, behavior_anomaly_score: Number(e.target.value) })}
                    />
                </div>

            </div>

            <div className="mt-8 flex gap-4">

                <button
                    onClick={randomize}
                    className="bg-blue-600 px-6 py-3 rounded hover:bg-blue-700"
                >
                    Generate Random Event
                </button>

                <button
                    onClick={analyze}
                    className="bg-red-600 px-6 py-3 rounded hover:bg-red-700"
                >
                    Analyze Login
                </button>

            </div>

            {

                result &&

                <div className="mt-10 bg-slate-800 rounded-lg p-6">

                    <h2 className="text-2xl font-bold mb-4">

                        AI Analysis Result

                    </h2>

                    <p>

                        <b>Anomaly :</b> {result.anomaly ? "Yes" : "No"}

                    </p>

                    <p>

                        <b>Threat :</b> {result.threat_level}

                    </p>

                    <p>

                        <b>Recommendation :</b> {result.recommended_action}

                    </p>

                    <p className="text-green-400 mt-4">

                        Saving incident and returning to dashboard...

                    </p>

                </div>

            }

        </div>

    );

}