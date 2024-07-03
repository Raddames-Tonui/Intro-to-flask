import { createContext, useState } from "react"


export const EventContext = createContext()

export const EventProvider = ({ children }) => 
{
   

    // All your functions and state variables will be available to all the children components that are wrapped in the UserProvider
    const add_event = () =>{
        console.log("Registering user")
    
    }

    const contextData ={
        add_event
    }
    return (
        <EventContext.Provider value={contextData}>
            {children}
        </EventContext.Provider>
    )
}