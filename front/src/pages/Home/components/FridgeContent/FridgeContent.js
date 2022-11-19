import React, { useContext, useEffect } from 'react';
import Col from 'react-bootstrap/esm/Col';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/esm/Row';
import UserContext from '../../../../contexts/userContext';
import './styles.css';

function FridgeContent() {
  const userContext = useContext(UserContext);

  function prepareIngredientName(ingredient) {
    ingredient = ingredient.charAt(0).toUpperCase() + ingredient.slice(1);
    if (ingredient.length > 10) {
      return ingredient.substr(0, 10) + "...";
    } else {
      return ingredient;
    }
  }

  useEffect(() => {
    if (!userContext.usersFridge) {
      userContext.setFridge(['tomatooooooooooooooooooooooooooooooooooooooooooooooooooooo', 'pasta', 'cheese']);
    }
  }, []); 

  return (<>
    { userContext.usersFridge ?
      <div class="contents">
        <div class="centerizer">
        {
            userContext.usersFridge.map((value) => 
            <div key={value} className="table-row">
              <Container>
                <Row>
                  <Col>
                    <div>IMG</div>
                  </Col>
                  <Col>
                    <p className="ingredient-name">
                      {prepareIngredientName(value)}
                    </p>
                  </Col>
                </Row>
              </Container>
            </div>
          )
          }
        <div className="add-row">
           <p className="add-button">
              Add new +
            </p>
          </div>
        </div>
      </div> : <div>Loading...</div>
    }
  </>);
}

export default FridgeContent;

