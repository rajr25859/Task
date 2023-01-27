import React, { useState } from 'react'
import {useLocation} from 'react-router-dom';
function grid() {
  let data = localStorage.getItem('FormData')
  
  const location = useLocation();
  console.log(location)

  return (
    <div>
      <table>
        <tr>
          <th>Name</th>
          <th>Age</th>
          <th>Gender</th>
        </tr>
        <tr>
          <td>{location.state.name}</td>
          <td>{location.state.age}</td>
          <td>{location.state.gender}</td>
        </tr>
      
      </table>

    </div>
  )
}

export default grid