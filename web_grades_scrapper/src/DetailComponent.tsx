import React from 'react';
import {useLocation} from "react-router-dom";
import MetacriticDetails from "./details/MetacriticDetails.tsx";
import OpencriticDetails from "./details/OpencriticDetails.tsx";
import ImdbDetails from "./details/ImdbDetails.tsx";

function DetailComponent() {
    const location = useLocation()
    if(location.state.page == "metacritic")
        return (<MetacriticDetails />)
    if(location.state.page == "opencritic")
        return (<OpencriticDetails />)
    if(location.state.page == "imdb")
        return (<ImdbDetails />)

}

export default DetailComponent
