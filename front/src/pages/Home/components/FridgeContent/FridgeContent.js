import React, { useContext } from 'react';
import Col from 'react-bootstrap/esm/Col';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/esm/Row';
import UserContext from '../../../../contexts/userContext';
import useAsync from '../../../../hooks/useAsync';
import useServer from '../../../../hooks/useServer';
import AddIngredient from '../AddIngredient/AddIngredient';
import DeleteIngredient from '../DeleteIngredient/DeleteIngredient';
import './styles.css';

function FridgeContent() {
  const {get} = useServer('/products', 'http://35.226.148.142');
  const userContext = useContext(UserContext);

  function prepareIngredientName(ingredient) {
    ingredient = ingredient.charAt(0).toUpperCase() + ingredient.slice(1);
    if (ingredient.length > 10) {
      return ingredient.substr(0, 10) + "...";
    } else {
      return ingredient;
    }
  }

  useAsync(() => get(userContext.user.uid), (result) => userContext.setFridge(result.products), [], (error) => console.log(error));

  return (<>
  <div className="fridge-title-container">
    <p className="fridge-title">Fridge contents</p>
  </div>
    { userContext.usersFridge || userContext.usersFridge === [] ?
      <div className="contents">
        <div className="centerizer">
        {
            userContext.usersFridge.map((value) => 
            <div key={value} className="table-row">
              <Container>
                <Row>
                  <Col>
                    <DeleteIngredient ingredient={value} />
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
        <AddIngredient />
        </div>
      </div> : <div><p className="loading">Loading your fridge contents...</p></div>
    }
  </>);
}

export default FridgeContent;

