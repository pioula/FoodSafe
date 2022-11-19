import React, { useContext, useState } from 'react';
import UserContext from '../../../../contexts/userContext';

function AddIngredient() {
  const userContext = useContext(UserContext);
  const [ingredient, setIngredient] = useState('');

  function handleChange(event) {
    console.log("hi");
    setIngredient(event.target.value);
  }

  function handleClick() {
    console.log(ingredient);
    userContext.setFridge([...userContext.usersFridge, ingredient])
  }

  return (
    <div>
      <input type="text" name="Ingredient" onChange={handleChange} />
      <div onClick={handleClick}>Add</div>
    </div>
  );
}

export default AddIngredient;

