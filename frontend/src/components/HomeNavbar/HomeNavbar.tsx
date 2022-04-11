import React from 'react'
import Container from 'react-bootstrap/esm/Container'
import Nav from 'react-bootstrap/esm/Nav'
import Navbar from 'react-bootstrap/esm/Navbar'
import NavDropdown from 'react-bootstrap/esm/NavDropdown'
import LoginButton from '../LoginButton/LoginButton'
import LogoutButton from '../LogoutButton/LogoutButton'
import './HomeNavbar.scss'
function HomeNavbar() {
    const isEmployee = false; //placeholder for when we do employee authentication
    let title;
    if (isEmployee){
        title = <Navbar.Brand href="/">Outage Tracker - Employee</Navbar.Brand>
    } else{
        title = <Navbar.Brand href="/">Outage Tracker</Navbar.Brand>
    }
    return (
        <Navbar bg="dark" expand="lg" variant="dark">
        <Container>
            {title}
            <Navbar.Toggle aria-controls="basic-navbar-nav" className="btn-light"/>
            <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
                <LoginButton />
                <LogoutButton />
                <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                    <NavDropdown.Item href="/">Report Outage</NavDropdown.Item>
                    <NavDropdown.Item href="/map">Outage Map</NavDropdown.Item>
                    <NavDropdown.Item href="/table">Outage Table</NavDropdown.Item>
                    <NavDropdown.Item href="/contact">Contact Us</NavDropdown.Item>   
                </NavDropdown>
            </Nav>
            </Navbar.Collapse>
        </Container>
        </Navbar>
    )
}

    export default HomeNavbar