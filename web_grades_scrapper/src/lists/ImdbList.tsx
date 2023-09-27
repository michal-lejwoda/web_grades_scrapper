import {PropsList} from "../interfaces.tsx";
// import PropTypes from 'prop-types';

function ImdbList (props: PropsList){
    const list_of_imdb_elements = props.data.map((element) => <div
        onClick={() => props.handleNavigation(element.url, "imdb")}
        key={element.id}>{element.title}</div>)
    return (
        <>
            {list_of_imdb_elements}
        </>
    )
};

// ImdbList.propTypes = {
//     handleNavigation: PropTypes.func,
//     data: PropTypes.array
// };

export default ImdbList;
