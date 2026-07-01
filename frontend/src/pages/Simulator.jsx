import { useState } from "react";
import api from "../services/api";

export default function Simulator() {

const [result,setResult]=useState("");

const analyze=async()=>{

const data={

role:0,
department:0,
login_hour:2,
device_type:0,
device_trusted:0,
country:1,
vpn_used:1,
failed_attempts:8,
mfa_enabled:1,
login_success:1,
session_duration_minutes:120,
privileged_account:1,
critical_system_access:1,
previous_risk_score:90,
jit_requests_last_30_days:7,
number_of_alerts:4,
number_of_sessions:20,
weekend_login:1,
login_frequency_last_7_days:15,
behavior_anomaly_score:95

};

const res=await api.post("/predict/pam-anomaly",data);

if(res.data.anomaly){

setResult(
"🚨 HIGH RISK\n\nReason:\n• Multiple failed logins\n• Untrusted Device\n• Login at 2 AM\n\nRecommendation:\nTerminate Session"
);

}else{

setResult(
"✅ Normal Login Activity"
);

}

window.location.reload();

}

return(

<div className="bg-slate-800 rounded-xl p-6 mt-8 text-white">

<h2 className="text-2xl font-bold mb-6">

AI Login Security Analyzer

</h2>

<div className="grid grid-cols-2 gap-5">

<input value="Admin" readOnly className="p-3 rounded bg-slate-700"/>

<input value="02:00 AM" readOnly className="p-3 rounded bg-slate-700"/>

<input value="8 Failed Attempts" readOnly className="p-3 rounded bg-slate-700"/>

<input value="VPN Enabled" readOnly className="p-3 rounded bg-slate-700"/>

<input value="Device Untrusted" readOnly className="p-3 rounded bg-slate-700"/>

<input value="Privileged Account" readOnly className="p-3 rounded bg-slate-700"/>

</div>

<button

onClick={analyze}

className="bg-red-600 hover:bg-red-700 mt-6 px-8 py-3 rounded font-bold"

>

Analyze Login

</button>

<pre className="mt-6 whitespace-pre-wrap text-green-400">

{result}

</pre>

</div>

)

}