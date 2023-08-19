import os
from typing import Optional

import bs4
import requests
from slugify import slugify

from helpers import get_soup
from opencritic import opencritic_types

"""Opencritic list"""


def get_opencritic_api_data(url_template: str, name: str) -> Optional[list]:
    api_headers = create_headers_and_querystring_for_api(name, os.getenv("RAPID_API_KEY"), os.getenv("RAPID_API_HOST"))
    if api_headers is None:
        return None
    try:
        response = requests.get(url_template, headers=api_headers['headers'], params=api_headers['querystring'])
        return response.json()
    except requests.exceptions.MissingSchema:
        return None


def create_headers_and_querystring_for_api(name: str, rapid_api_key: str, rapid_api_host: str) -> Optional[dict]:
    if rapid_api_key is None or rapid_api_host is None:
        return None
    querystring = {"criteria": name}
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": rapid_api_host
    }
    return {
        "querystring": querystring,
        "headers": headers
    }


def loop_results_and_get_more_info(api_results: list) -> list:
    opencritic_list_of_elements = []
    for result in api_results:
        url = get_opencritic_url(result['id'], slugify(result['name']))
        soup = get_soup(url)
        main_container = get_main_container(soup)
        img = get_opencritic_img(main_container)
        scores_container = get_opencritic_scores_container(main_container)
        critic_score = get_opencritic_critic_score(scores_container)
        opencritic_list_of_elements.append({"url": url, "id": result['id'],
                                            "name": result['name'], 'img': img,
                                            "critic_score": critic_score,
                                            })
    return opencritic_list_of_elements
def get_opencritic_url(id: int, name: str) -> Optional[str]:
    return "https://opencritic.com/game/{}/{}".format(id,name)




"""Opencritic detail"""


def get_main_container(soup: bs4.BeautifulSoup) -> Optional[bs4.element.Tag]:
    try:
        return soup.select(opencritic_types.SELECT_RESULT_CONTAINER)[0]
    except AttributeError:
        return None


def get_opencritic_img(main_container: bs4.element.Tag) -> Optional[dict]:
    try:
        img_container = main_container.find(name="picture").find(name="img")
        img = {
            "src": img_container['src'],
            "alt": img_container['alt']
        }
        return img
    except AttributeError:
        return None


def get_opencritic_reviews(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        reviews_container = main_container.find(name=opencritic_types.REVIEW_CONTAINER).find_all(name="div", attrs={
            "class": "justify-content-between"})
        reviews = []
        for review in reviews_container:
            reviewer = review.find_all(name="div")[0].text.strip()
            reviewer_score = review.find_all(name="div")[1].text
            reviews.append({"reviewer": reviewer, "reviewer_score": reviewer_score})

        return reviews
    except AttributeError:
        return None


def get_opencritic_developers(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        developers_list = []
        developers = main_container.find(name="div", attrs={"class": opencritic_types.COMPANIES}).find_all(name="span")
        for developer in developers:
            developers_list.append(developer.text)
        return developers_list
    except AttributeError:
        return None


def get_opencritic_platforms(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        platform_list = []
        platforms = main_container.find(name="div", attrs={"class": opencritic_types.PLATFORMS}).find_all(name="span")
        for platform in platforms:
            platform_list.append(platform.text)
        return platform_list
    except AttributeError:
        return None


def get_opencritic_release_date(main_container: bs4.element.Tag) -> Optional[str]:
    try:
        return main_container.find(name="div", attrs={"class": opencritic_types.PLATFORMS}).text
    except AttributeError:
        return None


def get_opencritic_title(main_container: bs4.element.Tag) -> Optional[str]:
    try:
        return main_container.find(name="h1").text
    except AttributeError:
        return None


def get_opencritic_scores_container(main_container: bs4.element.Tag) -> Optional[bs4.element.Tag]:
    try:
        return main_container.find(name=opencritic_types.SCORES_CONTAINER)
    except AttributeError:
        return None


def get_opencritic_critic_score(scores_container: bs4.element.Tag) -> Optional[str]:
    try:
        return scores_container.find(name='div', attrs={"class": opencritic_types.CRITIC_DATA}).text.strip()
    except AttributeError:
        return None


def get_opencritic_critic_recommend(scores_container: bs4.element.Tag) -> Optional[str]:
    try:
        return scores_container.find_all(name='div', attrs={"class": opencritic_types.CRITIC_DATA})[1].text.strip()
    except AttributeError:
        return None


def get_opencritic_critic_rating_img(scores_container: bs4.element.Tag) -> Optional[dict]:
    try:
        return {"src": "https:{}".format(scores_container.find('img')['src']),
                "alt": scores_container.find("img")['alt']}
    except AttributeError:
        return None
