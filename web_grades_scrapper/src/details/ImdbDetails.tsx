import React, {useEffect} from 'react';
import {useGetImdbDetails} from "../mutations.tsx";
import ReactLoading from "react-loading";
import Slider from "react-slick";

interface ImdbDetailsProps {
    url: string
}

const ImdbDetails: React.FC<ImdbDetailsProps> = props => {
    useEffect(() => {
        mutateImdbData({"url": props.url})
    }, [])

    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1
    };

    const {
        data: ImdbData,
        mutate: mutateImdbData,
        isSuccess,
    } = useGetImdbDetails()
    return (
        <>
            {isSuccess ? (
                <div className="text-white p-5 sm:flex xl:flex xl:justify-center">
                    <div className="sm:pr-4 flex justify-center sm:block">
                        {ImdbData.main_image && <img src={ImdbData.main_image} alt=""/>}
                    </div>
                    <div className="py-3 sm:w-500 xl:w-700">
                        {ImdbData.title && <p className="text-xl font-bold">{ImdbData.title}</p>}
                        <div>
                            {ImdbData.presentations && ImdbData.presentations.map((element, key) => {
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
                        {ImdbData.imdb_rating &&
                            <div>
                                <div className="flex justify-between"><p
                                    className="flex items-center">Imdb Rating</p>
                                    <div className="min-w-48"><p
                                        className="text-center pt-2">{ImdbData.imdb_rating}</p><p
                                        className="text-center text-sm">{ImdbData.imdb_rating_based_on}</p></div>
                                </div>
                                <hr/>
                            </div>}
                        {ImdbData.user_reviews_number &&
                            <div>
                                <div className="flex justify-between"><p
                                    className="flex items-center">User Reviews</p>
                                    <div className="min-w-48"><p
                                        className="text-center pt-2">{ImdbData.user_reviews_number}</p><p
                                        className="text-center text-sm">{ImdbData.critic_reviews_number}</p></div>
                                </div>
                                <hr/>
                            </div>
                        }
                        {ImdbData.metascore &&
                            <div>
                                <div className="flex justify-between py-2"><p
                                    className="flex items-center">Metascore:</p>
                                    <div className="min-w-48"><p
                                        className="text-center pt-2">{ImdbData.metascore}</p>
                                    </div>
                                </div>
                                <hr/>
                            </div>
                        }
                        {ImdbData.photos &&
                            <div>
                                <p className="text-xl pb-4">Photos:</p>
                                <Slider className="mx-3" {...settings}>
                                    {ImdbData.photos.map((element) => {
                                        return (
                                            <div>
                                                <img className="h-52 w-36"
                                                     src={element.src}
                                                     alt={element.alt}/>
                                            </div>
                                        )
                                    })}
                                </Slider>
                            </div>
                        }
                        {ImdbData.more_like_this &&
                            <div>
                                <p className="text-xl py-4">More like this</p>
                                <Slider className="mx-3" {...settings}>
                                    {ImdbData.more_like_this.map((element) => {
                                        return (
                                            <div>
                                                <img className="h-52 w-36"
                                                     src={element.more_like_this_image.src}
                                                     alt={element.more_like_this_image.alt}/>
                                                <p className="pt-4">{element.title}</p>
                                                <p>Ocena: {element.more_like_this_rating}</p>
                                            </div>
                                        )
                                    })}
                                </Slider>
                            </div>
                        }

                    </div>
                </div>
            ) : <div className="flex justify-center"><ReactLoading height={'10%'} width={'10%'}/></div>}
        </>
    );
};

export default ImdbDetails;
