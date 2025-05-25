import AddIcon from '@mui/icons-material/Add';
import { useEffect, useState } from 'react';
import { singleCategory, useLS, singeShopItem } from '../localstorage';
import DeleteIcon from '@mui/icons-material/Delete';
import axios from 'axios';

interface dodFuncs{
    getCategs:()=> void
    currCategs: singleCategory[]
}

export const ShoppingMenu:React.FC<dodFuncs>=({getCategs,currCategs})=>{
    const {getItem}=useLS("user")
    const userData=getItem()
    const [showCreateMenu,setCreateMenu]=useState<boolean>(false)
    const [showSortMenu,setSortMenu]=useState<boolean>(false)
    const [showCatMenu,setCatMenu]=useState<boolean>(false)

    const [search,setsearch]=useState<string>("")

    const [item,setitem]=useState<string>("")
    const [itemCat,setItemCat]=useState<string>("")
    const [quantity,setquantity]=useState<number|undefined>()
    const [price,setprice]=useState<number|undefined>()
    
    const [newCat,setNewCat]=useState<string>("")

    const searchCatId=(cat_elem:singleCategory)=>{
       return itemCat=== cat_elem.cat_name ? cat_elem.cat_uuid: null
    }

    const addItem=async()=>{
        try{
            const categoryId=currCategs.find(cat=>searchCatId(cat))?.cat_uuid
            const elemToAdd:singeShopItem={
                cat_uuid: categoryId,
                item_name: item,
                item_price: price ?? 0,
                item_quantity:quantity ?? 0
            }
            console.log(elemToAdd);
            
            const resp=await axios.post("http://127.0.0.1:8000/item/post",elemToAdd)
        }
        catch (e){throw e}
    }
    
    const addCategory=async()=>{
        try{
            const categoryToAdd:singleCategory={
                user_uuid: '30b1ff42-8b8b-405b-9229-c7b348e17e72',
                cat_name: newCat
            }
            const resp=await axios.post("http://127.0.0.1:8000/categs/addcat",categoryToAdd)
            getCategs()
        }
        catch(e){throw e}
    }

    const removeCategory=async(cat_uuid:string)=>{
        try{
            const resp=await axios.delete("http://127.0.0.1:8000/categs/removecateg",{params:{categ_uuid:cat_uuid}})
            getCategs()
        }
        catch(e){throw e}
    }

    useEffect(()=>{getCategs();},[])

    return(
        <>
            <div className="listMenu">
                <button style={showCreateMenu ? {outline: "2px solid #f8f7ddce"} : {}} onClick={()=>{setCreateMenu(!showCreateMenu)}}><p>add item</p> <AddIcon /></button>
                <button onClick={()=>{setCatMenu(!showCatMenu);}}>add category <AddIcon /></button>
            </div>
            <div className="dpMenus">
                { showCreateMenu && (<div className="createMenu">
                    <input type="text" placeholder='Enter name of item' onChange={(e)=>{setitem(e.target.value)}}/>
                    <details className='diffLevels'>
                        <summary>{itemCat ? itemCat : "Choose category" }</summary>
                        {currCategs.map((elem)=>(
                            <p onClick={()=>{setItemCat(elem.cat_name)}}>{elem.cat_name}</p>
                        ))}
                        <p onClick={()=>{setItemCat("")}}>None</p>
                    </details>
                    <p>All parameters down there are optional</p>
                    <input type="number" placeholder='Enter quantity' onChange={(e)=>{setquantity(parseInt(e.target.value))}}/>
                    <input type="number" placeholder='Enter price' onChange={(e)=>{setprice(parseInt(e.target.value))}}/>
                    <button className='addElem' onClick={addItem}>Add item</button>

                </div>)}
                {showSortMenu && (<div className="sortMenu">test2</div>)}
                {showCatMenu && (<div className="createMenu">
                    <input type="text" placeholder='Enter name of category' value={newCat} onChange={(e)=>{setNewCat(e.target.value)}}/>
                    <button className='addElem' onClick={addCategory}>Add category</button>
                    <div style={{display: "flex", flexWrap: "wrap",alignItems: "center"}}>
                        {currCategs.length===0 ? <p style={{paddingBottom: "15px"}}>Category list is empty</p> : currCategs.map((elem)=>(
                            <p style={{
                                display:"flex",
                                backgroundColor: "#2b4b54",
                                alignItems: "center",
                                borderRadius: "5px", 
                                padding:"3px",
                                marginBottom: "10px"}}>
                                    {elem.cat_name} <DeleteIcon onClick={()=>{removeCategory(String(elem.cat_uuid))}}/>
                            </p> 
                    ))}
                    </div>
                </div>)}

            </div>

        </>
    )
}