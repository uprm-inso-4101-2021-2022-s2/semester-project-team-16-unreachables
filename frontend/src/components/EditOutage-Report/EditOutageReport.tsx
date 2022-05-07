import React from 'react';
import { Button } from 'react-bootstrap';
import Form from 'react-bootstrap/Form';
import ViewOutageReport from '../viewOutageReport/ViewOutageReport';
const loginStyle = { display: "flex",
    alignSelf: "center",
    alignText: "center",
}
function EditOutageReport(props: { isEmployee: boolean; }) {
    const isEmployee = props.isEmployee;

    if  (isEmployee){
        return (
            <Form>
                <h1>Editing Report</h1>
                 <Form.Group className="mb-3 mx-3" controlId="reportService">
                    <Form.Label>Affected Service</Form.Label>
                    <Form.Control type="text" placeholder="ex: Water, Electricity, Internet" />
                </Form.Group>
        
                <Form.Group className="mb-3 mx-3" controlId="reportCompany">
                    <Form.Label>Company Providing Affected Service</Form.Label>
                    <Form.Control type="text" placeholder={`ex: AAA, LUMA, AT&T`} />
                </Form.Group>
                <Form.Group className=" mb-3 mx-3" controlId="title">
                    <Form.Label>Title</Form.Label>
                    <Form.Control type="text" placeholder={`Brief summary of situation`} />
                </Form.Group>

                <Form.Group className=" mb-3 mx-3" controlId="description">
                    <Form.Label>Description</Form.Label>
                    <Form.Control type="text" placeholder={`Any additional information about outage`} />
                </Form.Group>
                
                <Form.Group className=" mb-3 mx-3" controlId="reportLocation">
                    <Form.Label>Location of Outage</Form.Label>
                    <Form.Control type="text" placeholder={`ex: 33.3213123,98.32561223`} />
                </Form.Group>

                <Form.Group className=" mb-3 mx-3" controlId="reportLocation">
                    <Form.Label>Cause</Form.Label>
                    <Form.Control type="text" placeholder={`ex: 33.3213123,98.32561223`} />
                </Form.Group>

                <Form.Group className=" mb-3 mx-3" controlId="reportLocation">
                    <Form.Label>Status</Form.Label>
                    <Form.Control type="text" placeholder={`ex: 33.3213123,98.32561223`} />
                </Form.Group>

        
        
                <Button variant="primary" type="submit">
                    Update
                </Button>
            </Form>
          )
    }
    else{
        return <ViewOutageReport />
    }

}

export default EditOutageReport