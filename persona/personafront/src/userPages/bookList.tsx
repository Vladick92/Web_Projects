import { useLS,singleBook } from "../localstorage";
import { BookMenu } from "../singleElements/bookMenu";
import { useEffect, useState } from "react";
import axios from "axios";
import { SingleBook } from "../singleElements/singleBook";

export const BookList:React.FC=()=>{
    const {getItem}=useLS("user")
    const userData=getItem()
    const [bookItems,setBook]=useState<singleBook[]>([])
    const [userId,setUserId]=useState<string>('30b1ff42-8b8b-405b-9229-c7b348e17e72')

    const [resB,setRes]=useState<singleBook[]>([])
    const [typeOfLayout,setLayout]=useState<string>("fullWidth")

    const setDiffLayout=()=>{
        setLayout(typeOfLayout==="fullWidth" ? "plate" : "fullWidth")
    }

    const getBooks=async()=>{
        try{
            const resp=await axios.get<singleBook[]>("http://127.0.0.1:8000/book/getbooks",{params:{user_uuid:'30b1ff42-8b8b-405b-9229-c7b348e17e72'}})
            setBook(resp.data)
        }
        catch (e){}
    }

    useEffect(()=>{getBooks()},[])

    const switchList=resB.length>0 ? resB : bookItems

    return(
        <>
            <BookMenu onAdd={getBooks} changeLayout={setDiffLayout} allBooks={bookItems} setBookS={setRes}/>
            <div className="singleList">
                {bookItems.length===0 ?  <p></p> : switchList.map((elem)=>(
                    <SingleBook
                        book_uuid={elem.book_uuid}
                        book_name={elem.book_name}
                        user_uuid={elem.user_uuid}
                        book_desc={elem.book_desc}
                        layout={typeOfLayout}
                        onDelete={getBooks}
                        book_author={elem.book_author}
                        desc={typeOfLayout==='plate' ? 'descP' : "descF"}
                    />
                ))}
            </div>
        </>
    )
}