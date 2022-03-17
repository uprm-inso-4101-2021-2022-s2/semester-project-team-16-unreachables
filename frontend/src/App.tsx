import React from 'react';
import logo from './logo.svg';
import LoginButton from './components/login/LoginButton';
import LogoutButton from './components/logout/LogoutButton';
import { useAuth0 } from '@auth0/auth0-react';
import './App.css';

function App() {
    const { isLoading } = useAuth0();
    if (isLoading){
        return <div>Loading...</div>
    } else{
        return (
            <div className="App">
                <header className="App-header">
                    <LoginButton />
                    <LogoutButton />
                    <img src={logo} className="App-logo" alt="logo" />
                    <p>
                        Edit <code>src/App.tsx</code> and save to reload.
                    </p>
                    <a
                        className="App-link"
                        href="https://reactjs.org"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Learn React
                    </a>
                </header>
            </div>
        );
    }
}

export default App;
