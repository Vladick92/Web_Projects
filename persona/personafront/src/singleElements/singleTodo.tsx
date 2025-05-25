import { useState } from 'react'
import { singleTodo } from '../localstorage';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import axios from 'axios';

interface DodProp extends singleTodo{
    onDelete: ()=> void
    layout: string
    desc: string
}

export const SingleTodo:React.FC<DodProp>=({todo_name,user_uuid,creation_date,due_date,todo_desc,todo_diff,todo_uuid,todo_urge,onDelete,layout,desc})=>{
    const [showDesc,setShow]=useState<boolean>(false)
    const [edit,setEdit]=useState<boolean>(false)

    const [newName,setName]=useState<string>('')
    const [newurge,setUrge]=useState<string>('')
    const [newDiff,setDiff]=useState<string>('')
    const [newDue,setDue]=useState<string>('')
    const [newDesc,setDesc]=useState<string>('')

    const deleteElem=async()=>{
        try{
            const resp=await axios.delete("http://127.0.0.1:8000/todo/removetodo",{params:{todo_uuid:todo_uuid}})
            onDelete()
        }
        catch(e){throw e}
    }

    const editItem=async()=>{
        try{
            const ElemToUpd:singleTodo={
                todo_name: newName,
                user_uuid:'30b1ff42-8b8b-405b-9229-c7b348e17e72',
                creation_date:creation_date,
                due_date:  new Date(newDue),
                todo_desc: newDesc,
                todo_diff:  newDiff,
                todo_uuid: todo_uuid,
                todo_urge: newurge
            }
            const resp=await axios.patch("http://127.0.0.1:8000/todo/edittodo",ElemToUpd)
            onDelete()
        }
        catch(e){throw e}
    }

    return(
        <>
            <div className="singleElement">
                <div className={layout}>
                        {edit ? <input type="text" onChange={(e)=>{setName(e.target.value)}} placeholder='Enter new name of to do'/> : (<p>To do: {todo_name}</p>)}
                        {edit ? <>
                            <details className='diffLevels'>
                                <summary>{newDiff ? newDiff : "Choose difficulty" }</summary>
                                <p onClick={()=>{setDiff('easy')}}>easy</p>
                                <p onClick={()=>{setDiff('medium')}}>medium</p>
                                <p onClick={()=>{setDiff('hard')}}>hard</p>
                                <p onClick={()=>{setDiff('extra')}}>extra</p>
                                <p onClick={()=>{setDiff('')}}>none</p>
                            </details>
                        </> : (todo_urge && (<p>Urgency: {todo_urge}</p>))}
                        {edit ? <>
                            <details className='urgeLevels'>
                                <summary>{newurge ? newurge : "Choose urgency" }</summary>
                                <p onClick={()=>{setUrge('low')}}>low</p>
                                <p onClick={()=>{setUrge('medium')}}>medium</p>
                                <p onClick={()=>{setUrge('high')}}>high</p>
                                <p onClick={()=>{setUrge('critical')}}>critical</p>
                                <p onClick={()=>{setUrge('')}}>none</p>
                            </details>
                        </> : (todo_diff &&(<p>Difficulty: {todo_diff}</p>))}

                        {creation_date && (edit ? <input type="date" onChange={(e)=>{setDue(e.target.value)}}/> : (<p>Creation date: {creation_date ? new Date(creation_date).toISOString().split('T')[0] : 'N/A'}</p>))
                            }
                        {due_date && (<p>Due date: {due_date ? new Date(due_date).toISOString().split('T')[0] : 'N/A'}</p>)}
                        <div className="elementBtns fullWBtns">
                            {todo_desc ? <ExpandMoreIcon onClick={()=>{setShow(!showDesc)}}/> : ""}
                            {edit ? <button className='todoEditBtn' onClick={()=>{editItem();setEdit(false)}}>save changes</button> : (<EditIcon onClick={()=>{setEdit(true)}}/>)}
                            <DeleteIcon  onClick={deleteElem}/>
                        </div>
                </div>
                    <div className={desc}>
                        {edit ? <textarea className='todoDesc' onChange={(e)=>{setDesc(e.target.value)}}/>: (showDesc && (<p>{todo_desc}</p>))}
                    </div>
            </div>
        </>
    )  
}