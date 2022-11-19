import React from "react";

import { getAuth, GoogleAuthProvider,  signInWithPopup } from "firebase/auth";
// Import the functions you need from the SDKs you need

import { initializeApp } from "firebase/app";

const firebaseConfig = {
    apiKey: "AIzaSyDS9vekRqTOZlyRFjK9n00ay43Q9H6ZOsY",
    authDomain: "fridgefront-a501e.firebaseapp.com",
    projectId: "fridgefront-a501e",
    storageBucket: "fridgefront-a501e.appspot.com",
    messagingSenderId: "26561374030",
    appId: "1:26561374030:web:c31ef8c4b0a04794f4201f"
};

initializeApp(firebaseConfig);

const provider = new GoogleAuthProvider();
const auth = getAuth();

function signInUser() {
    return signInWithPopup(auth, provider)
        .then((result) => result.user)
        .catch((error) => {
            console.log(error);
            return null
        });
}

export let userContextContent = {
    auth,
    provider,
    signInUser
}

const UserContext = React.createContext(userContextContent);

export default UserContext;