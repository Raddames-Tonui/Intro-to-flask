import React, { useContext, useState } from 'react'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'
import { UserContext } from '../context/UserContext';
import { EventContext } from '../context/EventContext';


export default function AddEvent() 
{

  const {currentUser} = useContext(UserContext)
  const {add_event} = useContext(EventContext)

  const nav = useNavigate()
  const [event_name, setEventname] = useState()
  const [location, setLocation] = useState()
  const [event_date, setEventdate] = useState()
  const [description, setDescription] = useState()

  function handleSubmit(e){
    e.preventDefault()
     add_event(event_name, location, event_date, description)


  }
  return (
    <div>
    { currentUser && currentUser.is_organizer?
    <div className='grid grid-cols-2 h-[80vh] mt-6'>
      <div className='bg-gray-800 text-white flex justify-center items-center'>
        <h1 className='text-6xl font-bold'>Add New vent </h1>
      </div>
      <div className='p-6 '>
        <h1 className='text-center font-semibold text-2xl'>Add Event</h1>
        
        <form onSubmit={handleSubmit} class="max-w-md mx-auto">
          <div class="mb-5">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Event name</label>
            <input value={event_name} onChange={(e)=> setEventname(e.target.value)} type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  required />
          </div>

          <div class="mb-5">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Event Location</label>
            <input value={location} onChange={(e)=> setLocation(e.target.value)} type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  required />
          </div>

          <div class="mb-5">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">description</label>
            <textarea value={description} onChange={(e)=> setDescription(e.target.value)} type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  required >
              </textarea>
          </div>
          <div class="mb-5">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Event date</label>
            <input value={event_date} onChange={(e)=> setEventdate(e.target.value)} type="datetime-local" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  required />
          </div>
          <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
            Save Post
          </button>

        </form>



      </div>
    </div>
    :
    <div>
      <h1 className='text-3xl text-center'>You are not eventdateized to view this page</h1>
    </div>
}

  </div>
  )
}
