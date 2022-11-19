import useSignIn from "./useSignIn";

function SignIn() {
    const { user, onSignIn } = useSignIn();

    return (
        <div>
            {
                user ?
                    <p style={{ marginBottom: 0 }}>Welcome { user }!</p> :
                    <p style={{ marginBottom: 0 }} onClick={ onSignIn }>Sign In</p>
            }
        </div>
    );
}

export default SignIn;