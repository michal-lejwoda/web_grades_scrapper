import React, {useEffect} from 'react';
import PropTypes from "prop-types";
import {useGetMetacriticDetails} from "../mutations.tsx";

const MetacriticDetails = props => {
    useEffect(() => {
        mutateMetacriticData({"url": props.url})
    }, [])
    const {
        data: MetacriticData,
        mutate: mutateMetacriticData,
        isLoading: isLoadingMetacriticData
    } = useGetMetacriticDetails()
    console.log("MetacriticData")
    console.log(MetacriticData)
    return (
        <div>
            Metacritic Details
        </div>
    );
};
MetacriticDetails.propTypes = {
    url: PropTypes.string,
};

export default MetacriticDetails;
