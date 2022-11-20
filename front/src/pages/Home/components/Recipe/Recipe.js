import './styles.css';
import { useContext, useState } from "react";
import useServer from "../../../../hooks/useServer";
import UserContext from "../../../../contexts/userContext";
import useAsync from '../../../../hooks/useAsync';
import Container from 'react-bootstrap/esm/Container';
import Row from 'react-bootstrap/esm/Row';
import Col from 'react-bootstrap/esm/Col';

function Recipe() {
  const [recipe, setRecipe] = useState();
  const {get} = useServer('/recipe');
  const userContext = useContext(UserContext);

  useAsync(() => get(userContext.user.uid), (result) => {console.log(result); setRecipe(result[0])}, [], (error) => console.log(error));
  
  return (
    <>
      { recipe ?
      <div className="recipe">
        <Container >
          <Row>
            <Col md="auto">
              <div className="image-container">
                <img
                    className="recipe-image"
                    src={recipe.image}
                    alt="meal"
                />
              </div>
            </Col>
            <Col>
              <div className="recipe-title-container">
                <p className="recipe-title">
                  {recipe.title}
                </p>
              </div>
            </Col>
          </Row>
          <Row>
            <Col>
              <h1>Ingredients</h1>
              <ul>
                {
                  recipe.ingredients.map((ingredient) => <li key={ingredient}>{ingredient}</li>)
                }
              </ul>
            </Col>
          </Row>
          <Row>
            <Col>
              <a href={recipe.sourceUrl} className="credits">{recipe.creditsText}</a>
            </Col>
          </Row>
        </Container>
      </div> : <div><p className='loading'>Loading your recipe...</p></div>
      }
    </>
  );
}

export default Recipe;