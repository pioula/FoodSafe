import useSignIn from "./useSignIn";
import './styles.css';

function SignIn() {
    const { user, onSignIn } = useSignIn();
    
    return (
        <div className="greeting">
            {
                user ?
                    <>
                        <p className='welcome'>Welcome { user.name.split(' ')[0] }!</p>
                        <p className='catchphrase'>Make a use out of your good stuff!</p>
                    </> :
                    <>
                        <p className='welcome' onClick={ onSignIn }>Sign In</p>
                        <p className='catchphrase'>Cleaning fridge time!</p>
                    </>
            }
        </div>
    );
}

export default SignIn;