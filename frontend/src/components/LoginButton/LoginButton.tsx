import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'
import './LoginButton.scss'
const LoginButton = () => {
    const { loginWithRedirect, isAuthenticated } = useAuth0();
    
    return (
        <>
            { !isAuthenticated &&
                <button onClick={loginWithRedirect} className='btn-light'>
                Log In
                </button>
            }
        </>
    )
}

export default LoginButton