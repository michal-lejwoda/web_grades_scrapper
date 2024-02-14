import React, {useEffect} from 'react';
import {useGetImdbDetails} from "../mutations.tsx";

interface ImdbDetailsProps {
    url: string
}

const ImdbDetails: React.FC<ImdbDetailsProps> = props => {
    useEffect(() => {
        mutateImdbData({"url": props.url})
    }, [])
    const {
        data: ImdbData,
        mutate: mutateImdbData,
        isSuccess
        // isLoading: isLoadingImdbData
    } = useGetImdbDetails()
    console.log("ImdbData")
    console.log(ImdbData)
    return (
        <>
            {isSuccess && (
                <div className="text-white p-5 sm:flex xl:flex xl:justify-center">
                    <div className="sm:pr-4">
                        <img src={ImdbData.main_image} alt=""/>
                    </div>
                    <div className="py-3 sm:w-700">
                        <p className="text-xl font-bold">{ImdbData.title}</p>
                        <div>
                            {ImdbData.presentations.map((element, key) => {
                                return (
                                    <div key={key}>
                                        <div className="flex justify-between"><p
                                            className="flex items-center">{element.label}</p>
                                            <div className="min-w-48"><p
                                                className="text-center  pt-2">{element.presentation.join(", ")}</p>
                                            </div>
                                        </div>
                                        <hr/>
                                    </div>
                                )
                            })}
                        </div>
                        <div>
                            <div className="flex justify-between"><p
                                className="flex items-center">Imdb Rating</p>
                                <div className="min-w-48"><p
                                    className="text-center pt-2">{ImdbData.imdb_rating}</p><p
                                    className="text-center text-sm">{ImdbData.imdb_rating_based_on}</p></div>
                            </div>
                            <hr/>
                        </div>
                        <div>
                            <div className="flex justify-between"><p
                                className="flex items-center">User Reviews</p>
                                <div className="min-w-48"><p
                                    className="text-center pt-2">{ImdbData.user_reviews_number}</p><p
                                    className="text-center text-sm">{ImdbData.critic_reviews_number}</p></div>
                            </div>
                            <hr/>
                        </div>
                        <p className="mt-2 py-2">Metascore:
                            <span className="font-semibold">{ImdbData.metascore}</span></p>
                        <div>
                            <p>actors</p>
                        </div>
                        <div>
                            <p>More like this</p>
                            {ImdbData.more_like_this.map((element) => {
                                return (
                                    <div>
                                        <img src={element.more_like_this_image.src}
                                             alt={element.more_like_this_image.alt}/>
                                        <p>{element.title}</p>
                                        <p>{element.more_like_this_rating}</p>
                                    </div>
                                )
                            })}
                        </div>
                        <div>
                            <p>Photos</p>
                            {ImdbData.photos.map((element) => {
                                return (
                                    <div>
                                        <img src={element.src}
                                             alt={element.alt}/>
                                    </div>
                                )
                            })}
                        </div>
                    </div>
                </div>
            )}
        </>
    );
};

export default ImdbDetails;
