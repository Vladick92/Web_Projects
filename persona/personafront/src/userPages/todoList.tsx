import { SingleTodo } from "../singleElements/singleTodo"
import { useEffect, useState } from "react"
import axios from "axios"
import { useLS,singleTodo } from "../localstorage";
import { TodoMenu } from "../singleElements/todoMenu"

export const TodoList:React.FC=()=>{
    const {getItem}=useLS("user")
    const userData=getItem()
    const [todoItems,setTodo]=useState<singleTodo[]>([])
    const [userId,setUserId]=useState<string>('30b1ff42-8b8b-405b-9229-c7b348e17e72')
    const [searchRes,setRes]=useState<singleTodo[]>([])
    const [typeOfLayout,setLayout]=useState<string>("fullWidth")

    const setDiffLayout=()=>{setLayout(typeOfLayout==="fullWidth" ? "plate" : "fullWidth")}

    const getTodos=async()=>{
        try{
            const resp=await axios.get<singleTodo[]>("http://127.0.0.1:8000/todo/gettodos",{params: {user_uuid:'30b1ff42-8b8b-405b-9229-c7b348e17e72'}})
            setTodo(resp.data)
            console.log(resp.data);
        }
        catch (e){}
    }

    useEffect(()=>{getTodos()},[])

    const todosToDisplay=searchRes.length>0 ? searchRes : todoItems

    return(
        <>
            <TodoMenu onAdd={getTodos} changeLayout={setDiffLayout} setRes={setRes}/>
            <div className="singleList">
                {todoItems.length===0 ? <p></p> : todosToDisplay.map((elem)=>(
                    <SingleTodo 
                    todo_name={elem.todo_name} 
                    user_uuid={elem.user_uuid} 
                    creation_date={elem.creation_date}
                    due_date={elem.due_date}
                    todo_desc={elem.todo_desc}
                    todo_diff={elem.todo_diff}
                    todo_uuid={elem.todo_uuid}
                    todo_urge={elem.todo_urge}
                    onDelete={getTodos}
                    layout={typeOfLayout}
                    desc={typeOfLayout==='plate' ? 'descP' : "descF"}
                />
                )) }
                
            </div>
        </>
    )
}