import { Link } from "react-router-dom"
import './titleCSS.css'


export const TitlePart:React.FC=()=>{
    return(
        <>
            <div className="titleHeader">
                <div className="logo">
                   <p>persona</p>
                   <p>Your digital organizer</p>
                </div>
                <Link to='/login' className="authorise">authorise</Link>
            </div>
            <Link to='/login' className="startNow">Start now</Link>

            <div className="shortDesc">
                <div className="oneCol">
                    <h1>Stay on top of your Tasks</h1>
                    <p>
                        Create personal to-do list that helps you manage
                        your daily tasks efficiently
                    </p>
                </div>
                <div className="oneCol">
                    <h1>Keep track of your reading goals</h1>
                    <p>
                        Keep in one place list that allow you to compile 
                        and manage a personalized list of books you want
                        to read
                    </p>
                </div>
                <div className="oneCol">
                    <h1>Shopping list with categories</h1>
                    <p>
                        The shopping list feature in persona lets you 
                        create and manage shopping lists with personalized categories
                    </p>
                </div>
            </div>

            {/* <section id="additionalInfo">
                <div className="shortDesc"></div>
            </section> */}
        </>
    )
}