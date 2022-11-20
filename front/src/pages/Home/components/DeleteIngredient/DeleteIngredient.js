import React, { useContext } from 'react';
import UserContext from '../../../../contexts/userContext';
import useServer from '../../../../hooks/useServer';
import './styles.css';
import CloseButton from 'react-bootstrap/CloseButton';

function DeleteIngredient(props) {
  const userContext = useContext(UserContext);
  const {remove} = useServer('/products');


  async function handleClick() {
    let fridge = userContext.usersFridge;
    const index = fridge.indexOf(props.ingredient);
    fridge.splice(index, 1); 
    console.log(fridge);
    userContext.setFridge([...fridge]);
    await remove({products: [props.ingredient]}, userContext.user.uid);
  }

  return (
    <div onClick={handleClick}>
      <CloseButton />
    </div>
  );
}

export default DeleteIngredient;

