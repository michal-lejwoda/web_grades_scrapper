import React from 'react';

function ListDataComponent(props) {

    if (props.page == "metacritic"){
        const list_of_metacritic_elements = props.data.map((element)=> <div>{element.title}</div>)
        return(
            list_of_metacritic_elements
        )
    }else if (props.page == "imdb"){
        const list_of_imdb_elements = props.data.map((element)=> <div>{element.title}</div>)
        return(
            list_of_imdb_elements
        )
    }else {
        const list_of_opencritic_elements = props.data.map((element)=> <div>{element.name}</div>)
        return(
            list_of_opencritic_elements
        )
    }

}

export default ListDataComponent
