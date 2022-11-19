import React, { useContext, useEffect } from 'react';
import UserContext from '../../../../contexts/userContext';

function FridgeContent() {
  const userContext = useContext(UserContext);

  useEffect(() => {
    if (!userContext.usersFridge) {
      userContext.setFridge(['tomato', 'pasta', 'cheese']);
    }
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

