import React from 'react';
import AddIngredient from './components/AddIngredient/AddIngredient';
import FridgeContent from './components/FridgeContent/FridgeContent';
import SignIn from './components/SignIn/SignIn';

function Home() {
    return (
        <>
            <SignIn />
            <AddIngredient />
            <FridgeContent />
        </>
    );
}

export default Home;