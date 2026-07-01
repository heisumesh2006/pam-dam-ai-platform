import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

export default function DamAnalyzer() {

    const navigate = useNavigate();

    const [form, setForm] = useState({
        role: 0,
        department: 0,
        database_name: 0,
        table_name: 0,
        query_type: 0,
        rows_accessed: 5000,
        execution_time_ms: 1500,
        hour: 2,
        weekend_access: 1,
        country: 0,
        device_type: 0,
        sensitive_table: 1,
        download_size_mb: 250,
        failed_query_attempts: 5,
        query_frequency_last_hour: 40,
        database_sensitivity: 2,
        privileged_user: 1,
        behavior_anomaly_score: 95
    });

    const [result, setResult] = useState(null);

    const randomize = () => {

        setForm({

            role: Math.floor(Math.random() * 5),
            department: Math.floor(Math.random() * 5),
            database_name: Math.floor(Math.random() * 5),
            table_name: Math.floor(Math.random() * 5),
            query_type: Math.floor(Math.random() * 4),
            rows_accessed: Math.floor(Math.random() * 10000),
            execution_time_ms: Math.floor(Math.random() * 3000),
            hour: Math.floor(Math.random() * 24),
            weekend_access: Math.round(Math.random()),
            country: Math.floor(Math.random() * 3),
            device_type: Math.floor(Math.random() * 3),
            sensitive_table: Math.round(Math.random()),
            download_size_mb: Math.floor(Math.random() * 500),
            failed_query_attempts: Math.floor(Math.random() * 10),
            query_frequency_last_hour: Math.floor(Math.random() * 60),
            database_sensitivity: Math.floor(Math.random() * 3),
            privileged_user: Math.round(Math.random()),
            behavior_anomaly_score: Math.floor(Math.random() * 100)

        });

        setResult(null);

    };

    const analyze = async () => {

        const res = await api.post("/predict/dam-anomaly", form);

        setResult(res.data);

        setTimeout(() => {

            navigate("/");

        }, 2500);

    };

    return (

        <div className="min-h-screen bg-slate-950 text-white p-10">

            <h1 className="text-4xl font-bold mb-8">

                DAM Query Analyzer

            </h1>

            <div className="grid grid-cols-2 gap-5">

                <div>
                    <label>Rows Accessed</label>
                    <input
                        className="w-full p-2 rounded bg-slate-800"
                        value={form.rows_accessed}
                        onChange={e => setForm({ ...form, rows_accessed: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Execution Time (ms)</label>
                    <input
                        className="w-full p-2 rounded bg-slate-800"
                        value={form.execution_time_ms}
                        onChange={e => setForm({ ...form, execution_time_ms: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Hour</label>
                    <input
                        className="w-full p-2 rounded bg-slate-800"
                        value={form.hour}
                        onChange={e => setForm({ ...form, hour: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Download Size (MB)</label>
                    <input
                        className="w-full p-2 rounded bg-slate-800"
                        value={form.download_size_mb}
                        onChange={e => setForm({ ...form, download_size_mb: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Failed Queries</label>
                    <input
                        className="w-full p-2 rounded bg-slate-800"
                        value={form.failed_query_attempts}
                        onChange={e => setForm({ ...form, failed_query_attempts: Number(e.target.value) })}
                    />
                </div>

                <div>
                    <label>Behavior Score</label>
                    <input
                        className="w-full p-2 rounded bg-slate-800"
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
                    Generate Random Query
                </button>

                <button
                    onClick={analyze}
                    className="bg-red-600 px-6 py-3 rounded hover:bg-red-700"
                >
                    Analyze Query
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