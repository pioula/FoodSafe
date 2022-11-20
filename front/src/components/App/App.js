import React, { useState } from 'react';
import UserContext, { userContextContent } from '../../contexts/userContext';
import Home from '../../pages/Home/Home';

function App() {
  const [usersFridge, setFridge] = useState();
  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{ ...userContextContent, usersFridge, setFridge, user, setUser }}>
        <Home />
    </UserContext.Provider>
  );
}

export default App;