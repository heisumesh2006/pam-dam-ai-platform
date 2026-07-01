import {BrowserRouter,Routes,Route} from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import PamAnalyzer from "./pages/PamAnalyzer";
import DamAnalyzer from "./pages/DamAnalyzer";

export default function App(){

return(

<BrowserRouter>

<Routes>

<Route path="/" element={<Dashboard/>}/>

<Route path="/pam" element={<PamAnalyzer/>}/>

<Route path="/dam" element={<DamAnalyzer/>}/>

</Routes>

</BrowserRouter>

)

}