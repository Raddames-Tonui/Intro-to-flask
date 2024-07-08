import { createContext, useContext, useEffect, useState } from "react"
import { UserContext } from "./UserContext"
import { toast } from 'react-toastify'
import { useNavigate } from "react-router-dom"


export const EventContext = createContext()

export const EventProvider = ({ children }) => 
{
   const nav = useNavigate()
   const {auth_token} = useContext(UserContext)

   const [events, setEvents] = useState([])





    // All your functions and state variables will be available to all the children components that are wrapped in the UserProvider
    const add_event = (event_name, location, event_date, description) =>{
        fetch('http://localhost:5000/events', {
            method: 'POST',
            body: JSON.stringify({
                event_name, location, event_date, description
                
            }),
            headers: {
              'Content-type': 'application/json',
              "Authorization": `Bearer ${auth_token}`
            },
          })
        .then((response) => response.json())
        .then((res) =>{
            console.log(res)
         if(res.success)
            {
                toast.success(res.success)
                nav("/dashboard")
            }
            else if(res.error)
            {
                toast.error(res.error)
            }
            else {
                toast.error("An error occured")
            }

        });
    
    }

    // Register to attend an event
    const register_for_an_event = (event_id) =>{
        fetch('http://localhost:5000/registrations', {
            method: 'POST',
            body: JSON.stringify({
                event_id: event_id,
                
            }),
            headers: {
              'Content-type': 'application/json',
              "Authorization": `Bearer ${auth_token}`
            },
          })
        .then((response) => response.json())
        .then((res) =>{
            console.log(res)
         if(res.success)
            {
                toast.success(res.success)
            }
            else if(res.error)
            {
                toast.error(res.error)
            }
            else {
                toast.error("An error occured")
            }

        });
    
    }

    //    Fetch all events

    useEffect(()=>{
        if(auth_token)
        {
        fetch('http://localhost:5000/events', {
            method: 'GET',
            headers: {
              'Content-type': 'application/json',
              'Authorization': `Bearer ${auth_token}`
            }})
            .then((response) => response.json())
            .then((res) =>{
                setEvents(res)
            });
        }
    }, [auth_token])


    const contextData ={
        add_event,
        events,
        register_for_an_event
    }
    return (
        <EventContext.Provider value={contextData}>
            {children}
        </EventContext.Provider>
    )
}