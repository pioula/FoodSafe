import { useContext, useState } from "react";
import UserContext from "../../../../contexts/userContext";

function useSignIn() {
    const userContext = useContext(UserContext);

    function onSignIn() {
        userContext.signInUser()
            .then((res) => {
                if (res != null) {
                    userContext.setUser({name: res.displayName, uid: res.uid});
                }
                else {
                    return [];
                }
            })
            .catch((err) => console.log(err));
    }

    return { user: userContext.user , onSignIn };
}

export default useSignIn;