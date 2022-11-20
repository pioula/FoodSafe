import React, { useContext, useRef, useState } from 'react';
import Col from 'react-bootstrap/esm/Col';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/esm/Row';
import UserContext from '../../../../contexts/userContext';
import './styles.css';

function AddIngredient() {
  const [ingredient, setIngredient] = useState('');
  const [mode, setMode] = useState(true); // true - add button

  const addInput = useRef(null);

  function handleChange(event) {
    setIngredient(event.target.value);
  }

  // function handleClick() {
  //   userContext.setFridge([...userContext.usersFridge, ingredient])
  // }
  function handleClick() {

  }

  return (
    <div className="add-row">
      <Container>
        <Row>
          <Col>
            <input type="text" name="Ingredient" onChange={handleChange} ref={addInput} />
          </Col>
          <Col md="auto">
            <div className="accept-button" onClick={handleClick}>
              <p className="accept-content">+</p>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default AddIngredient;

