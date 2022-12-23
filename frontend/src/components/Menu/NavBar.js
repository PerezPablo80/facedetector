import React from "react";
import axios from "axios";

import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
// import NavDropdown from "react-bootstrap/NavDropdown";
import jadeImg from './jadelogo.png';
function exitRPi(){
    let url=process.env.REACT_APP_SERVER_PYTHON||'http://192.168.1.155:2999/';
    url=url+'shutdown'
    axios.get(url).then((res)=>{
        //Update only if necessary
        console.log(res.data);
    }).catch((e)=>{
        console.log(url)
        console.log('ERROR did mount::',e)
    })
}
export default function Menu(){
    
    return(
        <Navbar bg="light" expand="lg">
            <Container>
                <Navbar.Brand href="#">
                    <img src={jadeImg} width="30" height={30} className=" d-inline-block align-top" alt="logo"/>
                </Navbar.Brand>
                <Navbar.Brand href="/">Jade Informática</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link href="/dashboard">Dashboard(in progress)</Nav.Link>
                    </Nav>
                    <Nav className="me-auto">
                        <Nav.Link href="/file">Files</Nav.Link>
                    </Nav>
                    <Nav className="me-auto">
                        <Nav.Link href="#" onClick={()=>{exitRPi()}}>Apagar servidor</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}