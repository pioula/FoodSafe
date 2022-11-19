import React from 'react';
import useSignIn from './components/SignIn/useSignIn';

function Home() {
    const {user, onSignIn} = useSignIn();

    return (
        <div>
            Hellow
            {
                user ?
                    <p style={{ marginBottom: 0 }}>Welcome { user }!</p> :
                    <p style={{ marginBottom: 0 }} onClick={ onSignIn }>Sign In</p>
            }
        </div>
    );
}

export default Home;