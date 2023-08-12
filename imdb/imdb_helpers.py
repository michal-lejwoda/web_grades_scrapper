import bs4
from . import imdb_types
from .imdb_helpers_functions import get_description, get_container, get_title, get_data, get_imdb_rating, \
    get_imdb_rating_based_on, get_popularity, get_presentations, get_metascore, get_user_reviews_number, \
    get_critic_reviews_number, get_photos, get_actors, get_more_like_this


def get_imdb_movies_list(soup: bs4.BeautifulSoup) -> list:
    results = []
    list_container = soup.select(imdb_types.LIST_CONTAINER)
    for element in list_container:
        title = element.find("a", {"class": imdb_types.LIST_TITLE}).text
        description = get_description(element)
        temp_obj = {"title": title, "description": description}
        results.append(temp_obj)
    return results


def detail_imdb_movie(soup: bs4.BeautifulSoup) -> dict:
    container = get_container(soup)
    title = get_title(container)
    data = get_data(container)
    imdb_rating = get_imdb_rating(container)
    imdb_rating_based_on = get_imdb_rating_based_on(container)
    # Nie zawsze jest
    popularity = get_popularity(container)
    presentations = get_presentations(container)
    metascore = get_metascore(container)
    user_reviews_number = get_user_reviews_number(container)
    critic_reviews_number = get_critic_reviews_number(container)
    photos = get_photos(container)
    actors = get_actors(container)
    more_like_this = get_more_like_this(container)
    return {"data": data, "title": title, "presentations": presentations,
            "imdb_rating": imdb_rating, "imdb_rating_based_on": imdb_rating_based_on,
            "popularity": popularity, "metascore": metascore, "user_reviews_number": user_reviews_number,
            "critic_reviews_number": critic_reviews_number,
            "actors": actors,
            "more_like_this": more_like_this,
            "photos": photos
            }






