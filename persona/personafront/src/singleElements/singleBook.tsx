import { useState } from "react"
import { singleBook } from "../localstorage"
import axios from "axios"
import DeleteIcon from '@mui/icons-material/Delete';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

interface DodProp extends singleBook{
    onDelete: ()=> void
    layout: string
    desc: string
}

export const SingleBook:React.FC<DodProp>=({book_name,desc,layout,onDelete,user_uuid,book_author,book_desc,book_uuid})=>{
    const [showDesc,setShowDesc]=useState<boolean>(false)

    const deleteElem=async()=>{
        try{
            const resp=await axios.delete("http://127.0.0.1:8000/book/removebook",{params:{book_uuid:book_uuid}})
            onDelete()
        }
        catch(e){throw e}
    }


    return(
        <>
            <div className="singleElement">
                <div className={layout}>
                    <p>Book name: {book_name}</p>
                    {book_author && (<p>Author: {book_author}</p>)}
                    <div className="elementBtns fullWBtns">
                        {book_desc ? <ExpandMoreIcon onClick={()=>{setShowDesc(!showDesc)}}/> : ""}
                        <DeleteIcon  onClick={deleteElem}/>
                    </div>
                </div>
                <div className={desc}>
                    {showDesc && (<p>{book_desc}</p>)}
                </div>
            </div>
        </>
    )
}