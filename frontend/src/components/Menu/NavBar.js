import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
// import NavDropdown from "react-bootstrap/NavDropdown";
import jadeImg from './jadelogo.png';

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
                        <Nav.Link href="/dashboard">Dashboard</Nav.Link>
                    </Nav>
                    <Nav className="me-auto">
                        <Nav.Link href="/file">Files</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}