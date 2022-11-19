import React, { useContext, useEffect, useState } from 'react';
import UserContext from '../../../../contexts/userContext';

function FridgeContent() {
  const userContext = useContext(UserContext);
  const [a, setA] = useState(null);
  useEffect(() => {
    console.log(userContext.usersFridge);
    if (!userContext.usersFridge) {
      console.log("Hi!");
      userContext.setFridge(['tomato', 'pasta', 'cheese']);
    }
    setA(['xd']);
    console.log(userContext.usersFridge);
  }, []); 

  return (<>
    { userContext.usersFridge ?
      <table>
        <tbody>
          {
            userContext.usersFridge.map((value) => <tr key={value}><td>{value}</td></tr>)
          }
        </tbody>
      </table> : <div>Loading...</div>
    }
  </>);
}

export default FridgeContent;

