import React from 'react';
import { Button } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import { useAuth0 } from '@auth0/auth0-react';


function CreateOutageReport() {
    const { isAuthenticated } = useAuth0();
    if  (isAuthenticated){
        return (
            <Form>
                 <Form.Group className="mb-3 mx-3" controlId="reportService">
                    <Form.Label>Affected Service</Form.Label>
                    <Form.Control type="text" placeholder="ex: Water, Electricity, Internet" />
                </Form.Group>
        
                <Form.Group className="mb-3 mx-3" controlId="reportCompany">
                    <Form.Label>Company Providing Affected Service</Form.Label>
                    <Form.Control type="text" placeholder={`ex: AAA, LUMA, AT&T`} />
                </Form.Group>
                
                <Form.Group className=" mb-3 mx-3" controlId="reportLocation">
                    <Form.Label>Location of Outage</Form.Label>
                    <Form.Control type="text" placeholder={`ex: 33.3213123,98.32561223`} />
                </Form.Group>
        
        
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
          )
    }
    else{
        return <></>
    }

}

export default CreateOutageReport