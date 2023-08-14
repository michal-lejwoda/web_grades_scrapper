from slugify import slugify

from helpers import create_url, get_soup
from imdb.imdb_helpers_functions import get_list_container, get_list_title, get_list_description, get_container, \
    get_title, get_critic_reviews_number, get_user_reviews_number, get_metascore, get_photos, get_actors, \
    get_more_like_this, get_presentations, get_data, get_imdb_rating, get_imdb_rating_based_on, get_popularity


def get_imdb_rdr2_soup():
    name = "red dead redemption 2"
    name_slugify = slugify(name)
    url_template = "https://www.imdb.com/find/?q={}&ref_=nv_sr_sm"
    url = create_url(url_template, name_slugify)
    return get_soup(url)


"""List imdb functions"""

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





