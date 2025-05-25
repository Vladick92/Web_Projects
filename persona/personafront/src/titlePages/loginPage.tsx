import { useState } from "react"
import { Link } from "react-router-dom"
import axios, { AxiosError } from "axios"
import FormatListNumberedIcon from '@mui/icons-material/FormatListNumbered';
import AutoStoriesIcon from '@mui/icons-material/AutoStories';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import { useNavigate } from "react-router-dom";
import { useLS, userLog } from "../localstorage";

export const LoginPart:React.FC=()=>{
    const [username,setusername]=useState<string>('')
    const [password,setpassword]=useState<string>('')
    const [err,seterr]=useState<string>("")
    const [isLogged,setLogged]=useState<boolean>(false)
    const {setItem}=useLS("user")
    const nav=useNavigate()

    const logUser=async()=>{
        if (username === '' || password === '') {
            seterr(username === '' && password === '' ? "Enter username and password" : username === '' ? "Enter username" : "Enter password");
            return;
        }
        try{
            const resp=await axios.get<userLog>("http://127.0.0.1:8000/user/log/",{params:{username,password}})
            setItem(resp.data)
            setLogged(true)
        }
        catch(e){
            const axiosErr = e as AxiosError;
            const errorMessage = typeof axiosErr.response?.data === 'object'
                ? (axiosErr.response?.data as any).detail
                : axiosErr.response?.data as string;
            seterr(errorMessage || "An error occurred");
        }        
    }
    if(isLogged){nav('/user')}
    return(
        <>
            <div className="wholeAuthorise">
                <div className="leftPart">
                    <div className="loginHeader">
                        <p className="smallLogo">persona</p>
                        <Link to={'/'}>back</Link>
                    </div>
                   <p>Log into account</p>
                    <div className="inputFields">
                        <p>Your username</p>
                        <input type="text" onChange={(e)=>{setusername(e.target.value)}}/>
                        <p>Password</p>
                        <input type="password" onChange={(e)=>{setpassword(e.target.value)}}/>
                        <button className="submit" onClick={logUser}>submit</button>
                        {err && (<p className="titleError">{err}</p>)}
                        <Link to='/signup'>I dont have an account</Link>
                    </div>
                </div>
                <div className="rightPart">
                    <p>keep everything in one place</p>
                    <p>tasks <FormatListNumberedIcon/></p>
                    <p>books <AutoStoriesIcon/></p>
                    <p>shopping list <ShoppingCartIcon/></p>
                    <p>with persona</p>
                </div>
            </div>
        </>
    )
}