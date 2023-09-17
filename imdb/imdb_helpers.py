import bs4

from .imdb_helpers_functions import get_container, get_title, get_data, get_imdb_rating, \
    get_imdb_rating_based_on, get_popularity, get_presentations, get_metascore, get_user_reviews_number, \
    get_critic_reviews_number, get_photos, get_actors, get_more_like_this, get_list_title, get_list_description, \
    get_list_container, get_list_url


def get_imdb_movies_list(soup: bs4.BeautifulSoup) -> list:
    results = []
    list_container = get_list_container(soup)
    for element_id, element in enumerate(list_container):
        title = get_list_title(element)
        description = get_list_description(element)
        url = get_list_url(element)
        temp_obj = {"id": element_id, "title": title, "description": description, 'url': url}
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
