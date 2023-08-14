""" Test Opencritic list """
from dotenv import load_dotenv

from helpers import get_soup
from opencritic.opencritic_helpers_functions import get_opencritic_api_data, create_headers_and_querystring_for_api, \
    get_main_container, get_opencritic_img, get_opencritic_reviews, get_opencritic_release_date, \
    get_opencritic_platforms, get_opencritic_developers, get_opencritic_title, get_opencritic_scores_container, \
    get_opencritic_critic_score, get_opencritic_critic_recommend, get_opencritic_critic_rating_img

load_dotenv('.env')


def test_get_opencritic_api_data_with_wrong_url_template():
    url_template = "random url"
    name = 'red dead redemption 2'
    assert get_opencritic_api_data(url_template, name) == None


def test_get_opencritic_api_data_with_weird_name():
    url_template = "https://opencritic-api.p.rapidapi.com/game/search"
    name = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    get_opencritic_api_data(url_template, name)
    assert len(get_opencritic_api_data(url_template, name)) > 0


def test_create_headers_and_querystring_for_api_with_none_rapid_api_key():
    assert create_headers_and_querystring_for_api(
        "random string", None, "sadasdasdasdasd") is None


def test_create_headers_and_querystring_for_api_with_none_rapid_api_host():
    assert create_headers_and_querystring_for_api(
        "random string", "sadasdasdasdasd", None) is None


"""Opencritic detail"""


def get_opencritic_soup():
    url_template = "https://opencritic.com/game/10993/deathloop"
    soup = get_soup(url_template)
    return soup


def test_get_main_container_opencritic_soup():
    soup = None
    assert get_main_container(soup) is None


def test_get_opencritic_img_when_main_container_is_none():
    main_container = None
    assert get_opencritic_img(main_container) is None


def test_get_opencritic_reviews_when_main_container_is_none():
    main_container = None
    assert get_opencritic_reviews(main_container) is None


def test_get_opencritic_release_when_main_container_is_none():
    main_container = None
    assert get_opencritic_release_date(main_container) is None


def test_get_opencritic_platforms_when_main_container_is_none():
    main_container = None
    assert get_opencritic_platforms(main_container) is None


def test_get_opencritic_developers_when_main_container_is_none():
    main_container = None
    assert get_opencritic_developers(main_container) is None


def test_get_opencritic_title_when_main_container_is_none():
    main_container = None
    assert get_opencritic_title(main_container) is None


def test_get_opencritic_scores_container_when_main_container_is_none():
    main_container = None
    assert get_opencritic_scores_container(main_container) is None


def test_get_opencritic_critic_score_when_scores_container_is_none():
    scores_container = None
    assert get_opencritic_critic_score(scores_container) is None


def test_get_opencritic_critic_recommend_when_scores_container_is_none():
    scores_container = None
    assert get_opencritic_critic_recommend(scores_container) is None


def test_get_opencritic_critic_rating_img_when_scores_container_is_none():
    scores_container = None
    assert get_opencritic_critic_rating_img(scores_container) is None
