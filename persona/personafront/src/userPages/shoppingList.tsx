import axios from "axios";
import { ShoppingMenu } from "../singleElements/shoppingMenu";
import { useLS,singleCategory } from "../localstorage";
import { useEffect, useState } from "react";
import { SingleCategory } from "../singleElements/singleCategory";


export const ShoppingList:React.FC=()=>{
    const {getItem}=useLS("user")
    const userData=getItem()

    const [currCategs,setCategs]=useState<singleCategory[]>([])

    const getCategs=async()=>{
        try{
            const resp=await axios.get<singleCategory[]>("http://127.0.0.1:8000/categs/getcategs",{params:{user_uuid:'30b1ff42-8b8b-405b-9229-c7b348e17e72'}})
            setCategs(resp.data)
        }
        catch(e){console.log(e);}
    } 

    useEffect(()=>{
        const getAllCategs=async()=>{await getCategs()}
        getAllCategs()
    },[])

    return(
        <>
            <ShoppingMenu getCategs={getCategs} currCategs={currCategs}/>
            <div className="allCategories">
            {currCategs.map((elem)=>(
                <SingleCategory 
                    cat_uuid={elem.cat_uuid} 
                    cat_name={elem.cat_name} 
                    user_uuid={elem.user_uuid} 
                    onDelete={getCategs}/>
            ))}
            </div>
        </>
    )
}