from types import NoneType

import bs4.element

from helpers import create_url, get_soup, create_session
from metacritic.metacritic_helpers_functions import get_result_container, get_name, get_metascore, get_platforms, \
    get_img, get_types, get_main_container, get_rest_platforms, get_genres, get_developers, get_summary, get_year, \
    get_url, get_main_image, get_title

"""List metacritic tests"""


def get_test_rdr2_metacritic_soup():
    name = "red dead redemption 2"
    url_template = "https://www.metacritic.com/search/{}/"
    url = create_url(url_template, name)
    return get_soup(url)


def test_get_result_container_result_type():
    soup = get_test_rdr2_metacritic_soup()
    assert type(get_result_container(soup)) == bs4.element.ResultSet


def test_get_name_result_type():
    soup = get_test_rdr2_metacritic_soup()
    results = get_result_container(soup)
    for result_element in results:
        assert type(get_name(result_element)) == str


def test_get_metascore_result_type():
    soup = get_test_rdr2_metacritic_soup()
    results = get_result_container(soup)
    for result_element in results:
        assert type(get_metascore(result_element)) == str


def test_get_platforms_result_type():
    soup = get_test_rdr2_metacritic_soup()
    results = get_result_container(soup)
    for result_element in results:
        type_of_result = get_types(result_element)
        if type_of_result == "game":
            assert type(get_platforms(result_element)) is str
        else:
            assert type(get_platforms(result_element)) is NoneType


def test_get_img_result_type():
    soup = get_test_rdr2_metacritic_soup()
    results = get_result_container(soup)
    for result_element in results:
        assert type(get_img(result_element)) == str


def test_get_year_result_type():
    soup = get_test_rdr2_metacritic_soup()
    results = get_result_container(soup)
    for result_element in results:
        assert type(get_year(result_element)) == str


def test_get_types_result_type():
    soup = get_test_rdr2_metacritic_soup()
    results = get_result_container(soup)
    for result_element in results:
        assert type(get_types(result_element)) == str


def test_get_url_result_type():
    soup = get_test_rdr2_metacritic_soup()
    results = get_result_container(soup)
    for result_element in results:
        name = get_name(result_element)
        type_of_result = get_types(result_element)
        assert type(get_url(name, type_of_result)) is str


def test_get_result_container_when_soup_is_none():
    soup = None
    assert get_result_container(soup) == None


def test_get_name_when_result_element_is_none():
    result_element = None
    assert get_name(result_element) == None


def test_get_metascore_when_result_element_is_none():
    result_element = None
    assert get_metascore(result_element) == None


def test_get_platforms_when_result_element_is_none():
    result_element = None
    assert get_platforms(result_element) == None


def test_get_img_when_result_element_is_none():
    result_element = None
    assert get_img(result_element) == None


def test_get_year_when_result_element_is_none():
    result_element = None
    assert get_year(result_element) == None


def test_get_types_when_result_element_is_none():
    result_element = None
    assert get_types(result_element) == None


# def test_get_name_when_soup_is_none():
#     soup = None
#     for result_element in results:
#         name = get_name(result_element)
#     assert get_rest_platforms(soup, session) == None


"""Detail metacritic tests"""


def get_test_rdr2_detail_metacritic_soup():
    url_template = "https://www.metacritic.com/game/red-dead-redemption-2/"
    return get_soup(url_template)


def test_get_main_container_result_type():
    soup = get_test_rdr2_detail_metacritic_soup()
    assert type(get_main_container(soup)) == bs4.element.Tag


def test_get_rest_platforms_result_type():
    soup = get_test_rdr2_detail_metacritic_soup()
    assert type(get_rest_platforms(soup)) == list


def test_get_genres_result_type():
    soup = get_test_rdr2_detail_metacritic_soup()
    main_container = get_main_container(soup)
    assert type(get_genres(main_container)) == list



def test_get_developers_result_type():
    soup = get_test_rdr2_detail_metacritic_soup()
    main_container = get_main_container(soup)
    assert type(get_developers(main_container)) == str


def test_get_title():
    soup = get_test_rdr2_detail_metacritic_soup()
    main_container = get_main_container(soup)
    assert type(get_title(main_container)) == str
def test_get_main_image():
    soup = get_test_rdr2_detail_metacritic_soup()
    main_container = get_main_container(soup)
    assert type(get_main_image(main_container)) == str

def test_get_summary_result_type():
    soup = get_test_rdr2_detail_metacritic_soup()
    main_container = get_main_container(soup)
    assert type(get_summary(main_container)) == str


def test_get_main_container_when_soup_is_none():
    soup = None
    assert get_main_container(soup) == None


def test_get_rest_platforms_when_soup_is_none():
    soup = None
    assert get_rest_platforms(soup) == None


def test_get_genres_when_main_container_is_none():
    main_container = None
    assert get_genres(main_container) == None


def test_get_developers_when_main_container_is_none():
    main_container = None
    assert get_developers(main_container) == None


def test_get_summary_when_main_container_is_none():
    main_container = None
    assert get_summary(main_container) == None
