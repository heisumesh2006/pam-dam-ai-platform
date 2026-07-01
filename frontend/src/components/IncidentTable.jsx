import {useEffect,useState} from "react";
import api from "../services/api";

export default function IncidentTable(){

const [incidents,setIncidents]=useState([]);

const load=()=>{

api.get("/incidents/")
.then(res=>{
console.log(res.data);
setIncidents(res.data);

});

}

useEffect(()=>{

load();

const timer=setInterval(load,5000);

return ()=>clearInterval(timer);

},[]);

return(

<div className="bg-slate-800 rounded-xl shadow-lg mt-8 p-6">

<h2 className="text-2xl text-white mb-4">

Recent Incidents

</h2>

<table className="w-full text-white">

<thead>

<tr className="border-b border-slate-600">

<th>ID</th>

<th>Source</th>

<th>Threat</th>

<th>Anomaly</th>

<th>Action</th>

</tr>

</thead>

<tbody>

{

incidents.map((i)=>(

<tr
key={i.id}
className="text-center border-b border-slate-700"
>

<td>{i.id}</td>

<td>{i.source}</td>

<td>{i.threat_level}</td>

<td>

{i.anomaly?

"🔴"

:

"🟢"

}

</td>

<td>{i.recommended_action}</td>

</tr>

))

}

</tbody>

</table>

</div>

)

}