import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import CreateOutageReport from './components/createOutageReport/CreateOutageReport';
import HomeNavbar from './components/HomeNavbar/HomeNavbar';

function App() {
    const { isLoading } = useAuth0();
    if (isLoading){
        return <div>Loading...</div>
    } else{
        return (
            <div className="App" >
                <header className="App-header">
                    <HomeNavbar />
                    <CreateOutageReport />
                </header>
            </div>
        );
    }
}

export default App;
