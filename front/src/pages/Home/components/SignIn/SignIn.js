import useSignIn from "./useSignIn";
import './styles.css';
import { useEffect } from "react";

function SignIn() {
    const { user, onSignIn } = useSignIn();

    useEffect(() => {
        console.log(user);
    }, []);
    
    return (
        <div className="greeting">
            {
                user ?
                    <>
                        <p className='welcome'>Welcome { user.name.split(' ')[0] }!</p>
                        <p className='catchphrase'>Make use out of your good stuff!</p>
                    </> :
                    <p className='welcome' onClick={ onSignIn }>Sign In</p>
            }
        </div>
    );
}

export default SignIn;