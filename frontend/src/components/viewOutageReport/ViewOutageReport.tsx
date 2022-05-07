import React, { Component } from 'react'
import Form from 'react-bootstrap/Form';
export class ViewOutageReport extends Component {
  render() {
    return (
        <div>
            <h1>
                Viewing Specific Report
            </h1>
            <h3>
            Affected Service: <b>Electricity</b>
            </h3>
            <h3>
            Company Providing Affected Service: <b>LUMA</b>
            </h3>
            <h3>
            Title: <b>Outage in San Juan</b>
            </h3>
            <h3>
            Description:
            </h3>
            <p>
            The outage happened after a large noise ocurred near 
            Winston Churchill Avenue. We called to report after the light
            didn't return for 15 minutes.
            </p>
            <h3>
            Cause: <b>Substation damaged</b>
            </h3>
            <h3>
            Location: 123.34313214,43.3123123123
            </h3>
            <h3>
            Date: July / 11 / 2022
            </h3>
            <h3>
            Time: 10:22pm AST
            </h3>
            <button ref='/table'> Return to Reports Table</button>

            
        </div>
    )
  }
}

export default ViewOutageReport
