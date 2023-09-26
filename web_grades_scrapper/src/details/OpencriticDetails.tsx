import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
import {useGetOpencriticDetails} from "../mutations.tsx";

const OpencriticDetails = props => {
    useEffect(() => {
        mutateOpencriticData({"url": props.url})
    }, [])
    const {
        data: OpencriticData,
        mutate: mutateOpencriticData,
        isLoading: isLoadingOpencriticData
    } = useGetOpencriticDetails()

    mutateOpencriticData({"url": props.url})
    console.log("OpencriticData")
    console.log(OpencriticData)

    return (
        <div>
            Opencritic Details
        </div>
    );
};

OpencriticDetails.propTypes = {
    url: PropTypes.string,
};
export default OpencriticDetails;
