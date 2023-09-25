import React from 'react';
import PropTypes from 'prop-types';


function OpencriticList(props) {
    const list_of_opencritic_elements = props.data.map((element) => <div
        onClick={() => props.handleNavigation(element.url, "opencritic")} key={element.id}>{element.name}</div>)
    return (
        <>
            {list_of_opencritic_elements}
        </>
    )
}

OpencriticList.propTypes = {
    handleNavigation: PropTypes.func,
    data: PropTypes.array
};
export default OpencriticList;