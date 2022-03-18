import React from 'react'
import Container from 'react-bootstrap/esm/Container'
import Nav from 'react-bootstrap/esm/Nav'
import Navbar from 'react-bootstrap/esm/Navbar'
import NavDropdown from 'react-bootstrap/esm/NavDropdown'
import LoginButton from '../login/LoginButton'
import LogoutButton from '../logout/LogoutButton'
import './HomeNavbar.scss'
function HomeNavbar() {
  return (
    <Navbar bg="dark" expand="lg">
    <Container>
        <Navbar.Brand href="#home">Outage Tracker</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" className="btn-light"/>
        <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
            <LoginButton />
            <LogoutButton />
            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
            </NavDropdown>
        </Nav>
        </Navbar.Collapse>
    </Container>
    </Navbar>
  )
}

export default HomeNavbar