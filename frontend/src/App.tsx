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

function App() {
    const { isLoading } = useAuth0();
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
                    </Routes>
                    
                </BrowserRouter>
                </header>
            </div>
        );
    }
}

export default App;
