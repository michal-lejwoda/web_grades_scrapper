import {useNavigate} from "react-router-dom";
import OpencriticList from "./lists/OpencriticList.tsx";
import ImdbList from "./lists/ImdbList.tsx";
import MetacriticList from "./lists/MetacriticList.tsx";
// import PropTypes from "prop-types";


function ListDataComponent(props: any) {
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
    }
}
// ListDataComponent.propTypes = {
//     data: PropTypes.array,
//     page: PropTypes.string
// };

export default ListDataComponent
