import React, { useContext, useState } from 'react';
import Col from 'react-bootstrap/esm/Col';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/esm/Row';
import UserContext from '../../../../contexts/userContext';
import useServer from '../../../../hooks/useServer';
import './styles.css';

function AddIngredient() {
  const [ingredient, setIngredient] = useState('');
  const userContext = useContext(UserContext);
  const {post} = useServer('/products', 'http://35.226.148.142');

  function handleChange(event) {
    setIngredient(event.target.value);
  }

  async function handleClick() {
    userContext.setFridge([...userContext.usersFridge, ingredient])
    await post({products: [...userContext.usersFridge, ingredient]}, userContext.user.uid);
    setIngredient('');
  }

  return (
    <div className="add-row">
      <Container>
        <Row>
          <Col>
            <input type="text" name="Ingredient" onChange={handleChange} placeholder={"Type a new content i.e. tomato"} value={ingredient}/>
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

