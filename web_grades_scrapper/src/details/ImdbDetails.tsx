import React, {useEffect} from 'react';
import {useGetImdbDetails} from "../mutations.tsx";

interface ImdbDetailsProps {
    url: string
}
const ImdbDetails: React.FC<ImdbDetailsProps> = props => {
    useEffect(()=>{
        mutateImdbData({"url": props.url})
    },[])
    const {data: ImdbData, mutate: mutateImdbData,
        // isLoading: isLoadingImdbData
    } = useGetImdbDetails()
    console.log("ImdbData")
    console.log(ImdbData)
    return (
        <div>
            Imdb Details
        </div>
    );
};

export default ImdbDetails;
