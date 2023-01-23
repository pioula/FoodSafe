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
  const {post} = useServer('/recipe', 'http://localhost:8000');
  const userContext = useContext(UserContext);

  async function refreshRecipe() {
    setRecipe(null);
    await post({ products: ["carrot", "apple"] })
    .then((result) => result["data"].then(
      (returned_recipes) => setRecipe(returned_recipes[0])))
  }

  // useAsync(() => get(userContext.user.uid), (result) => setRecipe(result[0]), [], (error) => console.log(error));
  useAsync(async () => await post({ products: ["tomato", "pineapple"] }),
   (result) => result["data"].then(
    (returned_recipes) => setRecipe(returned_recipes[0])), [], 
    (error) => console.log(error));
  
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
            <Col>
              <div onClick={refreshRecipe}>
                <p className="refresh">⟳</p>
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