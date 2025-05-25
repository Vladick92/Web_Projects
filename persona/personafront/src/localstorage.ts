export interface userLog{
   string:string
    username: string
    userpass: string
    email:string
}

export interface singleTodo{
    todo_uuid?:string
    user_uuid:string
    todo_name: string
    todo_desc?: string
    todo_urge?: string
    todo_diff?: string
    creation_date?: Date
    due_date?: Date | null
}

export interface singleBook{
    user_uuid:string
    book_uuid?:string
    book_name: string
    book_author?: string
    book_desc?: string
}

export interface singleCategory{
    cat_uuid?:string
    user_uuid:string
    cat_name: string
}

export interface singeShopItem{
    item_uuid?:string
    cat_uuid?:string
    item_name: string
    item_quantity: number
    item_price: number
}

export const useLS=(key:string)=>{
    const setItem=(value:userLog)=>{
        try{window.localStorage.setItem(key,JSON.stringify(value))}
        catch(e){throw e}
    }

    const getItem=():userLog | null=>{
        try{
            const item=window.localStorage.getItem(key)
            if(item){return JSON.parse(item) as userLog}
            return null
        }
        catch(e){throw e}
    }

    const removeItem=()=>{
        try{window.localStorage.removeItem(key)}
        catch(e){throw e}
    }

    return {setItem,getItem,removeItem}
}