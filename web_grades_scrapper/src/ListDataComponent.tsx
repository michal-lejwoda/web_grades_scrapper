import React from 'react';
import {useNavigate} from "react-router-dom";
import DetailComponent from "./DetailComponent.tsx";


function ListDataComponent(props) {
    const navigate = useNavigate()
    const handleNavigation = (url) =>{
        console.log("url")
        console.log(url)
        navigate("/detail", {
            state: {
                "test": "test",
                "url": url
            }
        })
    }
    if (props.page == "metacritic"){
        const list_of_metacritic_elements = props.data.map((element)=> <div onClick={()=>handleNavigation(element.url)} key={element.id}>{element.title}</div>)
        return(
            list_of_metacritic_elements
        )
    }else if (props.page == "imdb"){
        const list_of_imdb_elements = props.data.map((element)=> <div onClick={()=>handleNavigation(element.url)} key={element.id}>{element.title}</div>)
        return(
            <>
            {list_of_imdb_elements}
            </>
        )
    }else {
        const list_of_opencritic_elements = props.data.map((element)=> <div onClick={()=>handleNavigation(element.url)} key={element.id}>{element.name}</div>)
        return(
            list_of_opencritic_elements
        )
    }

}

export default ListDataComponent
