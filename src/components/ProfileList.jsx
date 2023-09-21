import React from 'react'
import { Link } from 'react-router-dom'
function ProfileList() {
  return (
    <div className='flex flex-col dropDownProfile'>
      <ul className='flex flex-col gap-4'>
        <li>Profile</li>
        <li>Settings</li>
        <Link to="http://127.0.0.1:8000/console/console-login/"><li>Logout</li></Link>
      </ul>
    </div>
  )
}

export default ProfileList
