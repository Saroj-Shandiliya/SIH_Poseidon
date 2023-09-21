import React from 'react'
import { FaUserCircle } from 'react-icons/fa'
import {useState} from 'react';
import ProfileList from './ProfileList';

function Navbar() {
    const [openProfile, setOpenProfile] = useState(false)
  return (
      <div className="navbar">
      {
          openProfile && <ProfileList />
      }
        <div className="profile" onClick={()=> setOpenProfile((prev)=>!prev)}>
            <div className="profile_img">
                <FaUserCircle />
            </div>
        </div>

    </div>
  )
}

export default Navbar
