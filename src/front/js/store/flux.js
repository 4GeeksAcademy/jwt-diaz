import Signup from "../pages/signup";

const getState = ({ getStore, getActions, setStore }) => {
    return {
        store: {
            token: null,
        },
        actions: {
            Signup: async (user) => {
                try {
                    const response = await fetch(`${process.env.BACKEND_URL}/api/signup`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(user)
                    });
                    
                    const data = await response.json();
                    
                    if (data.token) {
                        setStore({ token: data.token });
                    }
                } catch (error) {
                    console.error("Error during signup:", error);
                }
            },
            Login: async (user) => {
                try {
                    const response = await fetch(`${process.env.BACKEND_URL}/api/login`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(user)
                    });

                    const data = await response.json();
                    
                    if (data.token) {
                        setStore({ token: data.token });
                    }
                } catch (error) {
                    console.error("Error during login:", error);
                }
            },
            Logout: () => {
                setStore({ token: null });
            }
        }
    };
};

export default getState;
