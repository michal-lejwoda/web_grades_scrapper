// import PropTypes from 'prop-types';
import {PropsList} from "../interfaces.tsx";


function OpencriticList(props: PropsList) {
    const list_of_opencritic_elements = props.data.map((element) => <div
        onClick={() => props.handleNavigation(element.url, "opencritic")} key={element.id}>{element.name}</div>)
    return (
        <>
            {list_of_opencritic_elements}
        </>
    )
}

// OpencriticList.propTypes = {
//     handleNavigation: PropTypes.func,
//     data: PropTypes.array
// };
export default OpencriticList;