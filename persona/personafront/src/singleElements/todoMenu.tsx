import AddIcon from '@mui/icons-material/Add';
import SearchIcon from '@mui/icons-material/Search';
import ViewComfyIcon from '@mui/icons-material/ViewComfy';
import { useEffect, useState } from 'react';
import { useLS,singleTodo,userLog } from '../localstorage';
import axios from 'axios';

interface DodProp{
    onAdd: ()=> void 
    changeLayout: ()=> void
    setRes: (todos:singleTodo[])=>void
}

export const TodoMenu:React.FC<DodProp>=({onAdd,changeLayout,setRes})=>{
    const [showCreateMenu,setCreateMenu]=useState<boolean>(false)
    const [showSortMenu,setSortMenu]=useState<boolean>(false)
    const [allTodos,setAllTodos]=useState<singleTodo[]>([])
    const [search,setsearch]=useState<string>("")


    const [name,setname]=useState<string>("")
    const [diff,setdiff]=useState<string>("")
    const [urge,setugre]=useState<string>("")
    const [date,setdate]=useState<boolean>(false)
    const [desc,setdesc]=useState<string>('')
    const [creation,setcreation]=useState<string>(new Date().toISOString().split('T')[0])
    const [due,setdue]=useState<string>("")

    const {getItem}=useLS("user")
    const userData:userLog|null=getItem()

    // const createTodo=()=>{
    //     const userData: userLog = {
    //         uuid: "123e4567-e89b-12d3-a456-426614174000",
    //         username: "JohnDoe",
    //         userpass: "securepass",
    //         email: "johndoe@example.com"
    //     };
        
    //     console.log(userData); // Full object
    //     console.log(userData?.uuid); // Valid UUID
    //     console.log(userData?.username); // Username
    // }

    const createTodo=async()=>{
        try{           
            const elemToAdd:singleTodo={
                user_uuid: '30b1ff42-8b8b-405b-9229-c7b348e17e72',
                todo_name: name,
                todo_desc: desc,
                todo_urge: urge,
                todo_diff: diff,
                creation_date: new Date(creation),
                due_date: due ? new Date(due) : null
            }
            const resp=await axios.post("http://127.0.0.1:8000/todo/addtodo",elemToAdd)
            onAdd()
        }
        catch(e){throw e}
    }

    const getTodos=async()=>{
        try{
            const resp=await axios.get<singleTodo[]>("http://127.0.0.1:8000/todo/gettodos",{params:{user_uuid:'30b1ff42-8b8b-405b-9229-c7b348e17e72'}})
            setAllTodos(resp.data)
        }
        catch(e){}
    }

    useEffect(()=>{getTodos()},[])

    useEffect(()=>{
        if(search){
            const filtered=allTodos.filter(item=>item.todo_name.toLowerCase().startsWith(search.toLowerCase()))
            setRes(filtered)
        }
        else{setRes(allTodos)}
      },[search])

    return (
        <>
            <div className="listMenu">
                <button style={showCreateMenu ? {outline: "2px solid #f8f7ddce"} : {}} onClick={()=>{setCreateMenu(!showCreateMenu)}}><p>create to-do</p> <AddIcon /></button>
                <div>
                    <input style={search ? {outline: "2px solid #f8f7ddce"} : {}} type="text" placeholder="search" onChange={(e)=>{setsearch(e.target.value)}}/>
                    <SearchIcon />
                </div>
                <button onClick={changeLayout}><p>layout</p> <ViewComfyIcon/></button>
            </div>
            <div className="dpMenus">
                { showCreateMenu && (<div className="createMenu">
                    <input type="text" placeholder='Enter name of to-do' onChange={(e)=>{setname(e.target.value)}}/>
                    <p>All parameters down there are optional</p>
                    <details className='diffLevels'>
                        <summary>{diff ? diff : "Choose difficulty" }</summary>
                        <p onClick={()=>{setdiff('easy')}}>easy</p>
                        <p onClick={()=>{setdiff('medium')}}>medium</p>
                        <p onClick={()=>{setdiff('hard')}}>hard</p>
                        <p onClick={()=>{setdiff('extra')}}>extra</p>
                        <p onClick={()=>{setdiff('')}}>none</p>
                    </details>
                    <details className='urgeLevels'>
                        <summary>{urge ? urge : "Choose urgency" }</summary>
                        <p onClick={()=>{setugre('low')}}>low</p>
                        <p onClick={()=>{setugre('medium')}}>medium</p>
                        <p onClick={()=>{setugre('high')}}>high</p>
                        <p onClick={()=>{setugre('critical')}}>critical</p>
                        <p onClick={()=>{setugre('')}}>none</p>
                    </details>
                    <div className='dateChooser'>
                        <p>Add date for this task</p>
                        <div className="switchBody" onClick={()=>{setdate(!date)}}><div className={date ? 'switchRound switchTrue' : 'switchRound'}></div></div>
                    </div>
                    {date && (<input type="date" onChange={(e)=>{setdue(e.target.value)}}/>)}
                    <p>Description for this task</p>
                    <textarea className='todoDesc' onChange={(e)=>{setdesc(e.target.value)}}/>
                    <button className='addElem' onClick={createTodo}>Add task to list</button>
                </div>)}
                {showSortMenu && (<div className="sortMenu">test2</div>)}
            </div>
            
        </>
    )
}