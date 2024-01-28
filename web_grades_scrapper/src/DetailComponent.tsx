import {useEffect} from 'react';
import {useLocation, useNavigate} from "react-router-dom";
import MetacriticDetails from "./details/MetacriticDetails.tsx";
import OpencriticDetails from "./details/OpencriticDetails.tsx";
import ImdbDetails from "./details/ImdbDetails.tsx";

function DetailComponent() {
    const location = useLocation()
    const navigate = useNavigate()
    const handleNavigationtoList = () => {
        navigate("/")
    }
    useEffect(() => {
        if (location.state == null)
            return handleNavigationtoList()
    }, []);

    if (location.state !== null) {
        if (location.state.page == "metacritic")
            return (<MetacriticDetails url={location.state.url}/>)
        if (location.state.page == "opencritic")
            return (<OpencriticDetails url={location.state.url}/>)
        if (location.state.page == "imdb")
            return (<ImdbDetails url={location.state.url}/>)
    }


}

export default DetailComponent
