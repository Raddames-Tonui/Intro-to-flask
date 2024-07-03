import React from 'react'
import { Link } from 'react-router-dom'
import { toast } from 'react-toastify'

export default function Post({post}) 
{


  return (
    <Link to={`/blog/${post.id}`} className='border p-3 bg-gray-200' >
        <div>
           <img class="rounded-t-lg w-full h-[50vh]" src="https://images.pexels.com/photos/21273536/pexels-photo-21273536/free-photo-of-beautiful-pink-blossoms-in-spring.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="" />
        </div>
        <h1 className='text-xl font-semibold'>{post.title}</h1>
        <p>{post.content}</p>
        <p>By <span className='italic'>{post.author}</span> </p>
        
  </Link>
  )
}
