import React from 'react';
import {useLocation} from "react-router-dom";

function DetailComponent() {
    const location = useLocation()
    console.log("location")
    console.log(location)
    return (
        <h1>
            Detail Component
        </h1>
    )

}

export default DetailComponent
