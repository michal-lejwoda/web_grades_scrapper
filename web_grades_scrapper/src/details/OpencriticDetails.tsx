import React, {useEffect} from 'react';
import {useGetOpencriticDetails} from "../mutations.tsx";
import ReactLoading from "react-loading";

interface OpencriticDetailsProps {
    url: string
}
interface Review{
    reviewer: string,
    reviewer_score: string
}

const OpencriticDetails: React.FC<OpencriticDetailsProps> = props => {
    useEffect(() => {
        mutateOpencriticData({"url": props.url})
    }, [])
    const {
        data: OpencriticData,
        mutate: mutateOpencriticData,
        isSuccess,
    } = useGetOpencriticDetails()
    return (
        <>

            {isSuccess ? (
                <div className="text-white p-5 md:flex xl:flex xl:justify-center">
                    <div className="md:pr-4">
                        {OpencriticData.img ? <img src={OpencriticData.img.src} alt=""/> :
                            <img src="/no_image.jpg" alt=""/>}
                    </div>
                    <div className="py-3 md:w-700">
                        <p className="text-3xl font-bold mb-3">{OpencriticData.title}</p>
                        <div>
                            <div className="flex justify-between px-2">{OpencriticData.critic_rating_img.src &&
                                <img className="w-20"
                                     src={OpencriticData.critic_rating_img.src}
                                     alt=""/>}
                                {OpencriticData.critic_score &&
                                    <div className="min-w-48 flex flex-col items-center w-24"><p
                                        className="text-center text-2xl flex items-center">{OpencriticData.critic_score}</p>
                                        <p className="text-sm text-center">Critic score</p>
                                    </div>
                                }
                                {OpencriticData.critic_recommend && <div className="flex flex-col items-center w-24">
                                    <p
                                        className="text-center text-2xl flex items-center">{OpencriticData.critic_recommend}</p>
                                    <p className="text-sm text-center">Recommendations</p>
                                </div>
                                }
                            </div>
                            <hr/>
                        </div>
                        {OpencriticData.developers &&
                            <p className="mt-2 py-2">Developers: <span
                                className="font-semibold">{OpencriticData.developers}</span></p>
                        }
                        {OpencriticData.release_date &&
                            <p className="py-2">Release Date: <span
                                className="font-medium">{OpencriticData.release_date}</span>
                            </p>
                        }
                        {OpencriticData.reviews &&
                            <div>
                                <div>Main Reviews:</div>
                                {OpencriticData.reviews.map((element: Review, index: number) => {
                                    return (
                                        <div key={index}>
                                            <p>Newspaper: {element.reviewer}</p>
                                            <p>Score {element.reviewer_score}</p>
                                        </div>
                                    )
                                })}
                            </div>
                        }
                    </div>
                </div>
            ) : <div className="flex justify-center"><ReactLoading height={'10%'} width={'10%'}/></div>}
        </>
    );
};

export default OpencriticDetails;
