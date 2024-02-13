import bs4

from helpers import create_session
from .metacritic_helpers_functions import get_name, get_metascore, get_platforms, get_img, get_year, get_types, \
    get_result_container, get_rest_platforms, get_main_container, get_genres, get_developers, get_summary, \
    create_dict_without_none_objects, get_url, get_publishers, get_release_date, get_user_data, get_main_image


# create_list_elements

def list_metacritic_games(soup: bs4.BeautifulSoup) -> list:
    list_of_elements = []
    results = get_result_container(soup)
    for result_element in results:
        name = get_name(result_element)
        metascore = get_metascore(result_element)
        img = get_img(result_element)
        year = get_year(result_element)
        type_of_result = get_types(result_element)
        url = get_url(name, type_of_result)
        platforms = get_platforms(result_element)
        dict_of_elements = {"name": name, "metascore": metascore, "platforms": platforms,
                            "img": img, "year": year, "types": type_of_result, "url": url}
        list_of_elements.append(create_dict_without_none_objects(dict_of_elements))
    return list_of_elements


def detail_metacritic_games(soup: bs4.BeautifulSoup) -> dict:
    rest_platforms = get_rest_platforms(soup)
    main_container = get_main_container(soup)
    main_image = get_main_image(main_container)
    genres = get_genres(main_container)
    developers = get_developers(main_container)
    publishers = get_publishers(main_container)
    user_data = get_user_data(main_container)
    release_date = get_release_date(main_container)
    summary = get_summary(main_container)

    results = {"developers": developers,
               "main_image": main_image,
               "genres": genres,
               "summary": summary,
               "platforms_data": rest_platforms,
               "release_date": release_date,
               "publishers": publishers,
               "user_data": user_data}
    return results
