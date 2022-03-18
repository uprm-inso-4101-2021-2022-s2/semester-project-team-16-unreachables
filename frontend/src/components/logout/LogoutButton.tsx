import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'

function LogoutButton() {
    const { logout, isAuthenticated } = useAuth0();
    if (isAuthenticated){
        return (
            <button onClick={()=>logout()} className="btn-light">
                Log Out
            </button>
        )
    } else{
        return <div></div>
    }
}

export default LogoutButton