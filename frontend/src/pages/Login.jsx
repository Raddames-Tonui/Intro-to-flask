import React, { useContext, useState } from 'react'
import { UserContext } from '../context/UserContext'

export default function Login() 
{
    const {login_user} = useContext(UserContext)

    const [email, setEmail] = useState()
    const [password, setPassword] = useState()


    function handleSubmit(e){
        e.preventDefault()

        login_user(email, password)


        setEmail("")
        setPassword("")
    }

  return (
    <div className='grid grid-cols-3'>
        <div></div>


        <div className="flex flex-col justify-center h-[70vh]">
        <div className='p-3 border rounded-xl bg-gray-200'>
            <h4 className='font-bold tex-2xl text-center'>Login</h4>
            <form onSubmit={handleSubmit}>
            <div className="mb-5">
                <label for="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                <input type="email" value={email || ""} onChange={(e)=> setEmail(e.target.value)} className="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" placeholder="name@flowbite.com" required />
            </div>
            <div className="mb-5">
                <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
                <input type="password" value={password || ""} onChange={(e)=> setPassword(e.target.value)}  className="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" required />
            </div>

            <button type="submit" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Login
            </button>
            </form>
        </div>
        </div>

        <div></div>
        
    </div>
  )
}
