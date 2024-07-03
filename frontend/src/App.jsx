import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home"
import Layout from "./Layout";
import NoPage from './pages/NoPage';
import AddEvent from './pages/AddEvent';
import Event from './pages/Event';
import UpdateEvent from './pages/UpdateEvent';
import EventRegistration from './pages/EventRegistration';
import Login from './pages/Login';
import Register from './pages/Register';
import { UserProvider } from './context/UserContext';
import { EventProvider } from './context/EventContext';
import Profile from './pages/Profile';
import Dashboard from './pages/Dashboard';

function App() {

  return (     
     <BrowserRouter>
    <UserProvider>
      <EventProvider>

      <Routes>
        <Route path='/' element={<Layout/>}>
          <Route path='/' element={<Home />} />
          <Route path='/dashboard' element={<Dashboard />} />

          <Route path='/event/register' element={<EventRegistration />} />
          <Route path='/addevent' element={<AddEvent />} />
          <Route path='/event/:id' element={<Event />} />
          <Route path='/update/:event_id' element={<UpdateEvent />} />

          <Route path='/register' element={<Register />} />
          <Route path='/login' element={<Login />} />
          <Route path='/profile' element={<Profile />} />

          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
      
      </EventProvider>
    </UserProvider>
    </BrowserRouter>
  )
}

export default App
