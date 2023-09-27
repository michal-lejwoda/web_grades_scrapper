// import PropTypes from 'prop-types';
import {PropsList} from "../interfaces.tsx";

function MetacriticList (props: PropsList) {
    const list_of_metacritic_elements = props.data.map((element) => <div
        onClick={() => props.handleNavigation(element.url, "metacritic")} key={element.id}>{element.name}</div>)
    return (
        <>
            {list_of_metacritic_elements}
        </>
    )
};

// MetacriticList.propTypes = {
//     handleNavigation: PropTypes.func,
//     data: PropTypes.array
// };

export default MetacriticList;
