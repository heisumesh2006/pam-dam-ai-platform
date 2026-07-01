import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";
import IncidentTable from "../components/IncidentTable";
import { Link } from "react-router-dom";

export default function Dashboard() {

    return (

        <div className="bg-slate-950 min-h-screen">

            <Navbar />

            <div className="max-w-7xl mx-auto p-8">

                <h1 className="text-4xl font-bold text-white mb-8">

                    Security Operations Dashboard

                </h1>

                <div className="grid md:grid-cols-3 gap-6">

                    <StatsCard
                        title="PAM Monitoring"
                        value="ACTIVE"
                        color="#f59e0b"
                    />

                    <StatsCard
                        title="DAM Monitoring"
                        value="ACTIVE"
                        color="#ef4444"
                    />

                    <StatsCard
                        title="System Status"
                        value="ONLINE"
                        color="#22c55e"
                    />

                </div>

                <div className="flex gap-5 mt-10 mb-10">

                    <Link to="/pam">

                        <button className="bg-orange-500 hover:bg-orange-600 text-white px-8 py-3 rounded-lg font-bold">

                            🔐 PAM Login Analyzer

                        </button>

                    </Link>

                    <Link to="/dam">

                        <button className="bg-red-600 hover:bg-red-700 text-white px-8 py-3 rounded-lg font-bold">

                            🗄️ DAM Query Analyzer

                        </button>

                    </Link>

                </div>

                <IncidentTable />

            </div>

        </div>

    );

}