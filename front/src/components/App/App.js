import React, { useState } from 'react';
import UserContext, { userContextContent } from '../../contexts/userContext';
import Home from '../../pages/Home/Home';

function App() {
  const [usersFridge, setFridge] = useState();
  return (
    <UserContext.Provider value={{ ...userContextContent, usersFridge, setFridge }}>
        <Home />
    </UserContext.Provider>
  );
}

export default App;