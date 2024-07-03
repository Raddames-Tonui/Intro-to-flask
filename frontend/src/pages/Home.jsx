import React, { useContext, useEffect, useState } from 'react'
import Landing from '../components/Landing'
import { v4 as uuidv4 } from 'uuid';
import ReactPaginate from 'react-paginate';
import { UserContext } from '../context/UserContext';

export default function Home() 
{
    const {currentUser, register_user} = useContext(UserContext)


  register_user()


  
  return (
    <div>
    <Landing />

 {currentUser}
    </div>
  )
}


