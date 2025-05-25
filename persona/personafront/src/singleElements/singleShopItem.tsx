import axios from 'axios';
import {singeShopItem} from '../localstorage'
import DeleteIcon from '@mui/icons-material/Delete';

interface dodProp extends singeShopItem{
    onDelete: ()=> void
}

export const SingleShopItem:React.FC<dodProp>=({item_name,item_price,item_quantity,cat_uuid,item_uuid,onDelete})=>{
    
    const deleteItem=async()=>{
        try{
            const resp=await axios.delete("http://127.0.0.1:8000/item/remove",{params:{item_uuid:item_uuid}})
            onDelete()
        }
        catch(e){throw e}
    }
    
    return(
        <>
            <div className="singleItem">
                <p>Item name: {item_name}</p>
                {item_price===0 ? null : (<p>Price: {item_price}</p>)}
                {item_quantity===0 ? null : (<p>Quantity: {item_quantity}</p>)}
                <DeleteIcon onClick={deleteItem}/>
            </div>
        </>
    )
}