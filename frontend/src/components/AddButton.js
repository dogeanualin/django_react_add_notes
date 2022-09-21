import React from 'react'
import { Link } from 'react-router-dom'
import {ReactComponent as AddButtonNote} from '../assets/add.svg';

const AddButton = () => {
  return (
    <Link to= '/note/new' className='floating-button'>
        <AddButtonNote></AddButtonNote>
    </Link>
  )
}

export default AddButton