import React ,{useState,useEffect}from 'react'
import { Link, useParams,useNavigate  } from 'react-router-dom';
import {ReactComponent as ArrowLeft} from '../assets/arrow-left.svg';

const NotePage = () => {
    let navigate = useNavigate();
    let { id } = useParams();
    let [note,setNote] =useState(null)
    useEffect(() => {
     getNote()
    },[id])
    let getNote = async ()=>{
        if (id === 'new') return

        let response = fetch(`/api/notes/${id}/`)
        let data = await (await response).json()
        setNote(data)
    }
    let updateNote = async() =>{
        fetch(`/api/notes/${note.id}/update/`,{
            method:'PUT',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(note)
        }).then(()=>{
            navigate("/");
        })
    }
    let createNote = async() =>{
        fetch('/api/note/create',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(note)
        }).then(()=>{
            navigate("/");
        })
    }
    let deleteNote = async() =>{
        fetch(`/api/notes/${note.id}/delete/`,{
            method:'DELETE',
            headers:{
                'Content-Type':'application/json'
            }
        }).then(()=>{
            navigate("/");
        })
    }
    let handleSubmit = ()=>{
        console.log(id)
        if (id !== 'new' && !note.body){
            deleteNote()
        }else if (id === 'new'){
                createNote()
            
        }else if (id !==' new'){
            updateNote()
        }
    }
  return (
    <div className='note'>
        <div className='note-header'>
            <h3>
                <Link to= '/' >
                    <ArrowLeft onClick = {handleSubmit}> </ArrowLeft>
                    
                </Link>
            </h3>
            {id !=='new' ? (

                <button onClick={deleteNote}>Delete</button>         
            ):(
                <button onClick={createNote}>Done</button>        

            )}
            
        </div>
        <textarea defaultValue={note?.body} onInput={(e) =>
        {
            setNote({...note,'body':e.target.value})
        }
            }></textarea>
    </div>
  )
}

export default NotePage