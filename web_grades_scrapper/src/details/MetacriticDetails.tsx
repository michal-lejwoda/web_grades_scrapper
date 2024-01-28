import React, {useEffect} from 'react';
import {useGetMetacriticDetails} from "../mutations.tsx";

interface MetacriticDetailsProps {
    url: string

}

const MetacriticDetails: React.FC<MetacriticDetailsProps> = props => {
    useEffect(() => {
        mutateMetacriticData({"url": props.url})
    }, [])
    const {
        data: MetacriticData,
        mutate: mutateMetacriticData,
        // isLoading: isLoadingMetacriticData
    } = useGetMetacriticDetails()
    console.log("MetacriticData")
    console.log(MetacriticData)
    return (
        <div>
            Metacritic Details
        </div>
    );
};

// MetacriticDetails.propTypes = {
//     url: PropTypes.string,
// };

export default MetacriticDetails;
