from typing import Optional

import bs4
from .opencritic_helpers_functions import (get_opencritic_api_data, get_main_container, get_opencritic_img,
                                           get_opencritic_reviews, get_opencritic_developers, get_opencritic_platforms,
                                           get_opencritic_release_date,
                                           get_opencritic_title, get_opencritic_scores_container,
                                           get_opencritic_critic_score, get_opencritic_critic_recommend,
                                           get_opencritic_critic_rating_img, loop_results_and_get_more_info)


def get_opencritic_games_list_json(url_template: str, name: str) -> Optional[list]:
    return loop_results_and_get_more_info(get_opencritic_api_data(url_template, name))


def detail_opencritic_games(soup: bs4.BeautifulSoup) -> dict:
    main_container = get_main_container(soup)
    img = get_opencritic_img(main_container)
    reviews = get_opencritic_reviews(main_container)
    release_date = get_opencritic_release_date(main_container)
    platforms = get_opencritic_platforms(main_container)
    developers = get_opencritic_developers(main_container)
    title = get_opencritic_title(main_container)
    scores_container = get_opencritic_scores_container(main_container)
    critic_score = get_opencritic_critic_score(scores_container)
    critic_recommend = get_opencritic_critic_recommend(scores_container)
    critic_rating_img = get_opencritic_critic_rating_img(scores_container)
    results = {"developers": developers, "title": title, "release_date": release_date,
               "platforms": platforms, "img": img, "critic_score": critic_score,
               "critic_recommend": critic_recommend,
               "critic_rating_img": critic_rating_img,
               "reviews": reviews
               }
    return results
