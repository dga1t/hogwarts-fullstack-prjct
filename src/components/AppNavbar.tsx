import React, { useState, useContext } from "react";

import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import { LinkContainer } from "react-router-bootstrap";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

//import UserContext from "../context/UserContext";

const AppNavbar = () => {
  const [ show, setShow ] = useState(false);

  return (
    <Navbar bg="dark" expand="lg">
      <Navbar.Brand href="/" className="text-white mr-auto">Hogwarts</Navbar.Brand>
      <Nav>
        <LinkContainer to="/student/add">
          <Nav.Link className="text-white">Add Student</Nav.Link>
        </LinkContainer>
        <LinkContainer to="/signup">
          <Nav.Link className="text-white">SignUp</Nav.Link>
        </LinkContainer>
        <LinkContainer to="/login">
          <Nav.Link className="text-white">LogIn</Nav.Link>
        </LinkContainer>
        <NavDropdown title="Dropdown" id="basic-nav-dropdown">
          <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
          <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
          <NavDropdown.Divider />
          <NavDropdown.Item href="#action/3.3">Separated link</NavDropdown.Item>
        </NavDropdown>
      </Nav>
    </Navbar>   
  )
}

export default AppNavbar;

