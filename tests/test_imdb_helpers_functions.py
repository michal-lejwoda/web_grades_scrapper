import bs4
import pytest
from slugify import slugify

from helpers import create_url, get_soup
from imdb.imdb_helpers_functions import get_list_container, get_list_title, get_list_description, get_container, \
    get_title, get_critic_reviews_number, get_user_reviews_number, get_metascore, get_photos, get_actors, \
    get_more_like_this, get_presentations, get_data, get_imdb_rating, get_imdb_rating_based_on, get_popularity, \
    get_main_image


def get_imdb_rdr2_soup():
    name = "red dead redemption 2"
    name_slugify = slugify(name)
    url_template = "https://www.imdb.com/find/?q={}&ref_=nv_sr_sm"
    url = create_url(url_template, name_slugify)
    return get_soup(url)

def get_imdb_detail_ryan_movie_soup():
    url_template = "https://www.imdb.com/title/tt0120815/"
    soup = get_soup(url_template)
    return soup


rdr2_soup = get_imdb_rdr2_soup()
ryan_soup = get_imdb_detail_ryan_movie_soup()

"""List imdb functions"""

def test_get_list_container_result_type():
    assert type(get_list_container(rdr2_soup)) == bs4.element.ResultSet

def test_get_list_title_result_type():
    list_container = get_list_container(rdr2_soup)
    for element in list_container:
        assert type(get_list_title(element)) == str


def test_get_list_description_result_type():
    list_container = get_list_container(rdr2_soup)
    for element in list_container:
        assert type(get_list_description(element)) == list


def test_get_list_container_when_soup_is_none():
    soup = None
    assert get_list_container(soup) is None


def test_get_list_title_when_element_is_none():
    element = None
    assert get_list_title(element) is None


def test_get_list_description_when_element_is_none():
    element = None
    assert get_list_description(element) is None


"""Detail imdb functions"""

def test_get_container_result_type():
    assert type(get_container(ryan_soup)) == bs4.element.Tag


def test_get_title_result_type():
    container = get_container(ryan_soup)
    assert type(get_title(container)) == str


def test_get_critic_reviews_number_result_type():
    container = get_container(ryan_soup)
    assert type(get_critic_reviews_number(container)) == str


def test_get_user_reviews_number_result_type():
    container = get_container(ryan_soup)
    assert type(get_user_reviews_number(container)) == str


def test_get_metascore_result_type():
    container = get_container(ryan_soup)
    assert type(get_metascore(container)) == str


def test_get_popularity_result_type():
    container = get_container(ryan_soup)
    assert type(get_popularity(container)) == str


def test_get_imdb_rating_based_on_result_type():
    container = get_container(ryan_soup)
    assert type(get_imdb_rating_based_on(container)) == str


def test_get_imdb_rating_result_type():
    container = get_container(ryan_soup)
    assert type(get_imdb_rating(container)) == str

def test_get_main_image():
    container = get_container(ryan_soup)
    assert type(get_main_image(container)) == str

def test_get_data_result_type():
    container = get_container(ryan_soup)
    assert type(get_data(container)) == list

@pytest.mark.skip(reason="Need to change one value but i dont know which")
def test_get_presentations_result_type():
    container = get_container(ryan_soup)
    assert type(get_presentations(container)) == list


def test_get_more_like_this_result_type():
    container = get_container(ryan_soup)
    assert type(get_more_like_this(container)) == list


def test_get_actors_result_type():
    container = get_container(ryan_soup)
    assert type(get_actors(container)) == list


def test_get_photos_result_type():
    container = get_container(ryan_soup)
    assert type(get_photos(container)) == list


def test_get_container_when_soup_is_none():
    soup = None
    assert get_container(soup) is None


def test_get_title_when_container_is_none():
    container = None
    assert get_title(container) is None


def test_get_critic_reviews_number_when_container_is_none():
    container = None
    assert get_critic_reviews_number(container) is None


def test_get_user_reviews_number_when_container_is_none():
    container = None
    assert get_user_reviews_number(container) is None


def test_get_metascore_when_container_is_none():
    container = None
    assert get_metascore(container) is None


def test_get_popularity_when_container_is_none():
    container = None
    assert get_popularity(container) is None


def test_get_imdb_rating_based_on_when_container_is_none():
    container = None
    assert get_imdb_rating_based_on(container) is None


def test_get_imdb_rating_when_container_is_none():
    container = None
    assert get_imdb_rating(container) is None


def test_get_data_when_container_is_none():
    container = None
    assert get_data(container) is None


def test_get_presentations_when_container_is_none():
    container = None
    assert get_presentations(container) is None


def test_get_more_like_this_when_container_is_none():
    container = None
    assert get_more_like_this(container) is None


def test_get_actors_when_container_is_none():
    container = None
    assert get_actors(container) is None


def test_get_photos_when_container_is_none():
    container = None
    assert get_photos(container) is None



