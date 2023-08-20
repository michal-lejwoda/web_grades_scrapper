import bs4

from helpers import create_session
from .metacritic_helpers_functions import get_name, get_metascore, get_platforms, get_img, get_year, get_types, \
    get_result_container, get_rest_platforms, get_main_container, get_genres, get_developers, get_summary, \
    create_dict_without_none_objects, get_url


# create_list_elements


def list_metacritic_games(soup: bs4.BeautifulSoup) -> list:
    list_of_elements = []
    try:
        results = get_result_container(soup)
        for result_element in results:
            name = get_name(result_element)
            metascore = get_metascore(result_element)
            platforms = get_platforms(result_element)
            img = get_img(result_element)
            year = get_year(result_element)
            types = get_types(result_element)
            url = get_url(result_element)
            dict_of_elements = {"name": name, "metascore": metascore, "platforms": platforms,
                                "img": img, "year": year, "types": types, "url": url}
            list_of_elements.append(create_dict_without_none_objects(dict_of_elements))
        return list_of_elements
    except AttributeError:
        return None


def detail_metacritic_games(soup: bs4.BeautifulSoup) -> dict:
    session = create_session()
    rest_platforms = get_rest_platforms(soup, session)
    main_container = get_main_container(soup)
    genres = get_genres(main_container)
    developers = get_developers(main_container)
    summary = get_summary(main_container)
    results = {"developers": developers, "genres": genres, "summary": summary,
               "platforms_data": rest_platforms}
    return results
