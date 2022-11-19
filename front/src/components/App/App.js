import React from 'react';
import UserContext, { userContextContent } from '../../contexts/userContext';
import Home from '../../pages/Home/Home';

function App() {
  return (
    <UserContext.Provider value={{ ...userContextContent }}>
        <Home />
    </UserContext.Provider>
  );
}

export default App;