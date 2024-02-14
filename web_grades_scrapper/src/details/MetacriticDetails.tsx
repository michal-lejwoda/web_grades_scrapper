import React, {useEffect} from 'react';
import {useGetMetacriticDetails} from "../mutations.tsx";
import ReactLoading from "react-loading";

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
        isSuccess,
        isLoading
    } = useGetMetacriticDetails()
    console.log("MetacriticData")
    console.log(MetacriticData)
    console.log("isLoading")
    console.log(isLoading)
    return (
        <>
            {isSuccess ? (
                <div className="text-white p-5 sm:flex xl:flex xl:justify-center">
                    <div className="sm:pr-4">
                        <img src={MetacriticData.main_image} alt=""/>
                    </div>
                    <div className="py-3 sm:w-700">
                        <p className="text-xl font-bold">{MetacriticData.title}</p>
                        <div>
                            {MetacriticData.platforms_data.map((element, key) => {
                                return (
                                    <div key={key}>
                                        <div className="flex justify-between"><p className="flex items-center">{element.platform}</p>
                                            <div className="min-w-48"><p className="text-center  pt-2">{element.critic_score}</p><p
                                                className="text-center text-sm">{element.critic_based_on}</p></div>
                                        </div>
                                        <hr/>
                                    </div>
                                )
                            })}
                        </div>
                        <div>
                            <div className="flex justify-between"><p
                                className="flex items-center">User Score</p>
                                <div className="min-w-48"><p className="text-center pt-2">{MetacriticData.user_data.user_score}</p><p
                                    className="text-center text-sm">{MetacriticData.user_data.user_based_on}</p></div>
                            </div>
                            <hr/>
                        </div>
                        <p className="mt-2 py-2">Developers: <span className="font-semibold">{MetacriticData.developers}</span></p>
                        <p className="py-2">Publisher: <span className="font-semibold">{MetacriticData.publishers}</span></p>
                        <p className="py-2">Release Date: <span className="font-medium">{MetacriticData.release_date}</span>
                        </p>
                        <p className="py-2">Genres: <span className="font-medium">{MetacriticData.genres}</span></p>
                        <p >Summary: <span className="text-sm">{MetacriticData.summary}</span></p>
                    </div>
                </div>
            ): <div className="flex justify-center"><ReactLoading height={'10%'} width={'10%'}/></div>}
        </>
    );
};

// MetacriticDetails.propTypes = {
//     url: PropTypes.string,
// };

export default MetacriticDetails;
