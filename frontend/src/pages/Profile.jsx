import React, { useContext, useEffect, useState } from 'react'
import { UserContext } from '../context/UserContext'

function Profile() 
{
    const {currentUser, update_user} = useContext(UserContext)
    const [password, setPassword] = useState()
    const [repeatPassword, setRepeatPassword] = useState()
    const [name, setName] = useState()
    const [phone_number, setPhone_number] = useState()
    const [is_organizer, setIs_organizer] = useState("false")
  
    console.log( password, repeatPassword, name, phone_number, is_organizer);
    useEffect(()=>{
        setName(currentUser && currentUser.name)
        setPhone_number(currentUser && currentUser.phone_number)
        setPassword(currentUser && currentUser.password)
        setIs_organizer(currentUser && currentUser.is_organizer)
    },[currentUser])




    function handleSubmit(e){
      e.preventDefault()
  
      if(password !== repeatPassword){
        toast.error("Passwords do not match")
        return
      }
  
      update_user(name, phone_number,is_organizer, password)
      setEmail("")
      setPassword("")
      setRepeatPassword("")
      setName("")
      setPhone_number("")
      is_organizer("false")
    }
  return (
    <div class="flex flex-col justify-center items-center h-[100vh]">
    <div class="relative flex flex-col items-center rounded-[20px] w-[400px] mx-auto p-4 bg-white bg-clip-border shadow-3xl shadow-shadow-500 dark:!bg-navy-800 dark:text-white dark:!shadow-none">
        <div class="relative flex h-32 w-full justify-center rounded-xl bg-cover" >
            <img src='https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/banner.ef572d78f29b0fee0a09.png' class="absolute flex h-32 w-full justify-center rounded-xl bg-cover" /> 
            <div class="absolute -bottom-12 flex h-[87px] w-[87px] items-center justify-center rounded-full border-[4px] border-white bg-green-400 dark:!border-navy-700">
                <img class="h-full w-full rounded-full" src='https://horizon-tailwind-react-git-tailwind-components-horizon-ui.vercel.app/static/media/avatar11.1060b63041fdffa5f8ef.png' alt="" />
            </div>
        </div> 
        <div class="mt-16 flex flex-col items-center">
            <h4 class="text-xl font-bold text-navy-700 dark:text-white">
               {currentUser && currentUser.name}
            </h4>
            <p class="text-base font-normal text-gray-600">{currentUser && currentUser.email}</p>

            {

                currentUser && currentUser.is_admin?
                <p class="bg-green-800 text-base font-normal text-white p-2 rounded-lg my-4">Admin</p>
                :
                currentUser && currentUser.is_organizer?
                <p class="bg-green-800 text-base font-normal text-white p-2 rounded-lg my-4">Organizer</p>
                :
                <p class="bg-green-800 text-base font-normal text-white p-2 rounded-lg my-4">Attendee</p>
            }
        </div> 
        <div class="mt-6 mb-3 ">
            <div className='flex flex-row  gap-4 justify-between'>
                <h5>Phone Number</h5>
                <p>{currentUser && currentUser.phone_number}</p>
            </div>
        </div>


        <div className=' border rounded-xl bg-gray-200'>
            <h4 className='font-bold tex-2xl text-center'>Update Your Account</h4>
            <form onSubmit={handleSubmit}>
   
            <div className="mb-5">
                <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                <input type="text" value={name || ""} onChange={(e)=> setName(e.target.value)} className="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" placeholder="John Doe" required />
            </div>
            <div className="mb-5">
                <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone Number</label>
                <input type="text" value={phone_number || ""} onChange={(e)=> setPhone_number(e.target.value)} className="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" placeholder="07123456789" required />
            </div>
            <div className="mb-5">
                <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
                <input type="password" value={password || ""} onChange={(e)=> setPassword(e.target.value)}  className="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" required />
            </div>
            <div className="mb-5">
                <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Repeat password</label>
                <input type="password" value={repeatPassword || ""} onChange={(e)=> setRepeatPassword(e.target.value)} className="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light" required />
            </div>

            <div className="mb-5">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Register as</label>
            <select onChange={ e => setIs_organizer(e.target.value)} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option selected value="false">User</option>
              <option value="true">Organizer</option>
            </select>
            </div>

            <button type="submit" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Update
            </button>
            </form>
        </div>


    </div>  
</div>
  )
} 

export default Profile