import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
import {useGetImdbDetails} from "../mutations.tsx";


const ImdbDetails = props => {
    useEffect(()=>{
        mutateImdbData({"url": props.url})
    },[])
    console.log("props")
    console.log(props)
    const {data: ImdbData, mutate: mutateImdbData, isLoading: isLoadingImdbData} = useGetImdbDetails()

    console.log("ImdbData")
    console.log(ImdbData)
    return (
        <div>
            Imdb Details
        </div>
    );
};
ImdbDetails.propTypes = {
    url: PropTypes.string,
};

export default ImdbDetails;
