import React, {useEffect} from 'react';
import {useGetOpencriticDetails} from "../mutations.tsx";

interface OpencriticDetailsProps {
    url: string
}

const OpencriticDetails: React.FC<OpencriticDetailsProps> = props => {
    useEffect(() => {
        mutateOpencriticData({"url": props.url})
    }, [])
    const {
        data: OpencriticData,
        mutate: mutateOpencriticData,
        // isLoading: isLoadingOpencriticData
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

export default OpencriticDetails;
