import FormatListNumberedIcon from '@mui/icons-material/FormatListNumbered';
import AutoStoriesIcon from '@mui/icons-material/AutoStories';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios, { AxiosError } from 'axios';
import { useLS,userLog } from '../localstorage';

export const SignupPart:React.FC=()=>{
    const {setItem}=useLS("user")
    const [username,setusername]=useState<string>('')
    const [password,setpassword]=useState<string>('')
    const [email,setemail]=useState<string>('')
    const [repeat,setrepeat]=useState<string>('')
    const [err,seterr]=useState<string>("")
    const [isSigned,setSigned]=useState<boolean>(false)
    const nav=useNavigate()

    
    const signUser=async()=>{
        try{
            const resp=await axios.get("http://127.0.0.1:8000/user/check",{params:{nameToCheck:username}})
            if(resp.data!==null){
                seterr("Username already taken")
            }
            else{seterr("")}
        }
        catch(e){throw e}
        if(password!==repeat){seterr(err+" Passwords dont match");return}
        try{
            const UserToLog={
                username:username,
                user_pass:password,
                email:email
            }
            const resp=await axios.post<userLog>("http://127.0.0.1:8000/user/sign",UserToLog)
            setItem(resp.data)
            setSigned(true)
        }
        catch(e){
            const axiosErr= e as AxiosError
            const errorMessage=typeof axiosErr.response?.data==="object"
                ? (axiosErr.response?.data as any).detail
                : axiosErr.response?.data as string
            seterr(errorMessage || "An error occured")
        }
    }
    if(isSigned){nav('/user')}
    return(
        <>
        <div className="wholeAuthorise">
            <div className="leftPart">
            <div className="loginHeader">
                        <p className="smallLogo">persona</p>
                        <Link to={'/'}>back</Link>
            </div>
                   <p>Create new account</p>
                    <div className="signInput inputFields">
                        <p>Unique username</p>
                        <input type="text" onChange={(e)=>{setusername(e.target.value)}}/>
                        <p>Password</p>
                        <input type="password" onChange={(e)=>{setpassword(e.target.value)}}/>
                        <p>Repeat password</p>
                        <input type="password" onChange={(e)=>{setrepeat(e.target.value)}}/>
                        <p>Email</p>
                        <input type="text" onChange={(e)=>{setemail(e.target.value)}}/>
                        <button className="submit" onClick={signUser}>submit</button>
                        {err && (<p className="titleError">{err}</p>)}
                        <Link to='/login'>I already have an account</Link>
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