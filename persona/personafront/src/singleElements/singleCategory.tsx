import { useEffect, useState } from "react"
import { SingleShopItem } from "./singleShopItem"
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import { singeShopItem, singleCategory } from "../localstorage";
import axios from "axios";

interface CatProps{
    cat_uuid?:string
    cat_name:string
    user_uuid:string
    onDelete: ()=> void
}


export const SingleCategory:React.FC<CatProps>=({cat_uuid,cat_name,user_uuid,onDelete})=>{
    const [show,setshow]=useState<boolean>(false)
    const [items,setitems]=useState<singeShopItem[]>([])
    const [editCat,setEdit]=useState<boolean>(false)
    const [newName,setNew]=useState<string>("")

    const getItems=async()=>{
        try{
            const resp=await axios.get("http://127.0.0.1:8000/item/get",{params:{cat_uuid:cat_uuid}})
            setitems(resp.data)
        }
        catch(e){throw e}
    }

    const deleteCategory=async()=>{
        try{
            const resp=await axios.delete("http://127.0.0.1:8000/categs/removecateg",{params:{categ_uuid:cat_uuid}})
            onDelete()
        }
        catch(e){throw e}
    }

    const editCategory=async()=>{
        try{
            const elemToAdd:singleCategory={
                cat_uuid: cat_uuid,
                cat_name: newName,
                user_uuid: '30b1ff42-8b8b-405b-9229-c7b348e17e72'
            }
            const resp=await axios.patch("http://127.0.0.1:8000/categs/editcateg",elemToAdd)
            onDelete()
        }
        catch(e){throw e}
    }

    useEffect(()=>{getItems()},[])

    return(
        <>
            <div className="singleCategory">
                <p>{editCat ? <input type="text" placeholder="Enter new category name" onChange={(e)=>{setNew(e.target.value)}}/> : `Category: ${cat_name}` }
                <div className="catBtns">
                    {show ? (<ExpandLessIcon onClick={()=>{setshow(!show)}}/>) : <ExpandMoreIcon onClick={()=>{setshow(!show)}}/>}
                    <DeleteIcon onClick={deleteCategory}/>
                    {editCat ? <button onClick={()=>{editCategory();setEdit(false)}}>save changes</button> : (<EditIcon onClick={()=>{setEdit(true)}}/>)}
                    
                </div>
                </p>
                {show && (
                    items.length===0 ?
                    "List is empty" :
                    <>
                        {items.map((elem)=>(
                            <SingleShopItem
                                item_uuid={elem.item_uuid}
                                item_name={elem.item_name} 
                                item_price={elem.item_price} 
                                item_quantity={elem.item_quantity}
                                onDelete={getItems}/>
                        ))}
                    </>
                )}
            </div>
        </>
    )
}