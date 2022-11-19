import React from 'react';
import AddIngredient from './components/AddIngredient/AddIngredient';
import FridgeContent from './components/FridgeContent/FridgeContent';
import SignIn from './components/SignIn/SignIn';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import './styles.css';
function Home() {
    return (
        <div className="main-content">
            <Container>
                <Row>
                    <Col><SignIn /></Col>
                </Row>
                <Row>
                    <Col><AddIngredient /></Col>
                </Row>
                <Row>
                    <Col><FridgeContent /></Col>
                </Row>
            </Container>
        </div>
    );
}

export default Home;