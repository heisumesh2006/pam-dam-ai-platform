import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";
import IncidentTable from "../components/IncidentTable";

export default function Dashboard(){

return(

<div className="bg-slate-950 min-h-screen">

<Navbar/>

<div className="max-w-7xl mx-auto p-8">

<div className="grid md:grid-cols-3 gap-6">

<StatsCard
title="PAM Alerts"
value="LIVE"
color="#f59e0b"
/>

<StatsCard
title="DAM Alerts"
value="LIVE"
color="#ef4444"
/>

<StatsCard
title="System"
value="ONLINE"
color="#22c55e"
/>

</div>

<IncidentTable/>

</div>

</div>

)

}