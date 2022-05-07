import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import CreateOutageReport from './components/createOutageReport/CreateOutageReport';
import HomeNavbar from './components/HomeNavbar/HomeNavbar';
import OutageReportTable from './components/OutageReportTable/OutageReportTable';
import {
    BrowserRouter as Router,
    Routes,
    Route,
    BrowserRouter
  } from "react-router-dom";
import { ViewOutageReport } from './components/viewOutageReport/ViewOutageReport';
import EditOutageReport from './components/EditOutage-Report/EditOutageReport';
function App() {
    const { isLoading } = useAuth0();
    const props = {isEmployee:true};
    if (isLoading){
        return <div>Loading...</div>
    } else{
        return (
            <div className="App" >

                <header className="App-header">
                <BrowserRouter>
                <HomeNavbar />
                    <Routes>
                        <Route path='/' element={<CreateOutageReport />}/>
                        <Route path='/table' element={<OutageReportTable />}/>
                        <Route path='/view' element={<EditOutageReport isEmployee={true} />}/>
                    </Routes>
                    
                </BrowserRouter>
                </header>
            </div>
        );
    }
}

export default App;
