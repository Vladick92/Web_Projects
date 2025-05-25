import AddIcon from '@mui/icons-material/Add';
import SearchIcon from '@mui/icons-material/Search';
import ViewComfyIcon from '@mui/icons-material/ViewComfy';
import { useEffect, useState } from "react"
import { singleBook,useLS } from '../localstorage';
import axios from 'axios';

interface DodProp{
    onAdd: ()=> void
    changeLayout:()=>void
    allBooks: singleBook[]
    setBookS: (books:singleBook[])=>void
}

export const BookMenu:React.FC<DodProp>=({changeLayout,onAdd,allBooks,setBookS})=>{
    const [showCreateMenu,setCreateMenu]=useState<boolean>(false)
    const [showSortMenu,setSortMenu]=useState<boolean>(false)

    const [search,setsearch]=useState<string>("")
    const [name,setname]=useState<string>("")
    const [author,setauthor]=useState<string>("")
    const [desc,setdesc]=useState<string>("")

    const {getItem}=useLS("user")
    const userData=getItem()

    const addBook=async()=>{
        try{
            const elemToAdd:singleBook={
                user_uuid: '30b1ff42-8b8b-405b-9229-c7b348e17e72',
                book_name: name,
                book_desc: desc,
                book_author:author
            }
            const resp=await axios.post("http://127.0.0.1:8000/book/addbook",elemToAdd)
            onAdd()
        }
        catch (e){throw e}
    }

    useEffect(()=>{
        if(search){
            const filtered=allBooks.filter(elem=>elem.book_name.startsWith(search.toLowerCase()))
            setBookS(filtered)
        }
        else{setBookS(allBooks)}
    },[search])

    return(
        <>
            <div className="listMenu">
                <button style={showCreateMenu ? {outline: "2px solid #f8f7ddce"} : {}} onClick={()=>{setCreateMenu(!showCreateMenu)}}><p>add book</p> <AddIcon /></button>
                <div>
                    <input style={search ? {outline: "2px solid #f8f7ddce"} : {}} type="text" placeholder="search" onChange={(e)=>{setsearch(e.target.value)}}/>
                    <SearchIcon />
                </div>
                <button onClick={changeLayout}><p>layout</p> <ViewComfyIcon/></button>
            </div>
            <div className="dpMenus">
                { showCreateMenu && (<div className="createMenu">
                    <input type="text" placeholder='Enter name of the book' onChange={(e)=>{setname(e.target.value)}}/>
                    <p>All parameters down there are optional</p>
                    <input type="text" placeholder='Enter author`s name' onChange={(e)=>{setauthor(e.target.value)}}/>
                    <p>Description for this book</p>
                    <textarea className='todoDesc'onChange={(e)=>{setdesc(e.target.value)}}/>
                    <button className='addElem' onClick={addBook}>Add book to list</button>
                </div>)}
                {showSortMenu && (<div className="sortMenu">test2</div>)}
            </div>
        </>
    )
}