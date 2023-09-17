import React from 'react';
import {useNavigate} from "react-router-dom";
import DetailComponent from "./DetailComponent.tsx";


function ListDataComponent(props) {
    console.log("props.data")
    console.log(props.data)
    const handleNavigation = () =>{
        // useNavigate(<DetailComponent />)
    }
    if (props.page == "metacritic"){
        const list_of_metacritic_elements = props.data.map((element)=> <div key={element.id}>{element.title}</div>)
        return(
            list_of_metacritic_elements
        )
    }else if (props.page == "imdb"){
        const list_of_imdb_elements = props.data.map((element)=> <div key={element.id}>{element.title}</div>)
        return(
            <>
            <button ></button>
            {list_of_imdb_elements}
            </>
        )
    }else {
        const list_of_opencritic_elements = props.data.map((element)=> <div key={element.id}>{element.name}</div>)
        return(
            list_of_opencritic_elements
        )
    }

}

export default ListDataComponent
