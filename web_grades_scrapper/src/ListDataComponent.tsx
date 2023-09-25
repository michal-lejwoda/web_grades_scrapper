import React from 'react';
import {useNavigate} from "react-router-dom";
import DetailComponent from "./DetailComponent.tsx";
import OpencriticList from "./lists/OpencriticList.tsx";
import ImdbList from "./lists/ImdbList.tsx";
import MetacriticList from "./lists/MetacriticList.tsx";


function ListDataComponent(props) {
    const navigate = useNavigate()
    const handleNavigation = (url: string, page: string) => {
        navigate("/detail", {
            state: {
                "url": url,
                "page": page
            }
        })
    }
    if (props.page == "metacritic") {
        return (
            <MetacriticList data={props.data} handleNavigation={handleNavigation}/>
        )
    } else if (props.page == "imdb") {
        return (
            <ImdbList data={props.data} handleNavigation={handleNavigation}/>
        )
    } else {
        return (
            <OpencriticList data={props.data} handleNavigation={handleNavigation}/>
        )
        // const list_of_opencritic_elements = props.data.map((element) => <div
        //     onClick={() => handleNavigation(element.url)} key={element.id}>{element.name}</div>)
        // return (
        //     <>
        //         {list_of_opencritic_elements}
        //     </>
        // )
    }

}

export default ListDataComponent
