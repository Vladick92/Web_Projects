import { useState } from 'react'
import './userCSS.css'
import { Outlet,Link } from 'react-router-dom'
import { useLS } from '../localstorage'

export const UserHeader:React.FC=()=>{
    const [selectedList,setList]=useState<string>("")
    const {removeItem}=useLS("user")

    return(
        <>
            <div className="userHeader">
                <p className="smallLogo">persona</p>
                <div className='listChooser'>
                    <p>Choose type of list:</p>
                    <div className="lists">
                        <Link to={'todo_list'} className={selectedList === 'todo_list' ? 'selectedList' : ''}  onClick={()=>{setList("todo_list")}}>to-do</Link>
                        <Link to={'book_list'} className={selectedList === 'book_list' ? 'selectedList' : ''}  onClick={()=>{setList("book_list")}}>book</Link>
                        <Link to={'shopping_list'} className={selectedList === 'shopping_list' ? 'selectedList' : ''}  onClick={()=>{setList("shopping_list")}}>shopping list</Link>
                    </div>
                </div>
                <Link to={'/'} className='logOut' onClick={removeItem}>Log out</Link>
            </div>
            <Outlet/>
        </>
    )
}