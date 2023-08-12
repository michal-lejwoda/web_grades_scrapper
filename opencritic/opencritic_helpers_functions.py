import os

import bs4
import requests

from opencritic import opencritic_types

"""Opencritic list"""


def get_opencritic_api_data(url_template: str, name: str) -> list:
    querystring = {"criteria": name}
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
        "X-RapidAPI-Host": os.getenv("RAPID_API_HOST")
    }
    response = requests.get(url_template, headers=headers, params=querystring)
    return response.json()


"""Opencritic detail"""


def get_main_container(soup: bs4.BeautifulSoup) -> bs4.element.Tag:
    return soup.select(opencritic_types.SELECT_RESULT_CONTAINER)[0]


def get_opencritic_img(main_container: bs4.element.Tag):
    img_container = main_container.find(name="picture").find(name="img")
    img = {
        "src": img_container['src'],
        "alt": img_container['alt']
    }
    return img


def get_opencritic_reviews(main_container: bs4.element.Tag):
    reviews_container = main_container.find(name=opencritic_types.REVIEW_CONTAINER).find_all(name="div", attrs={
        "class": "justify-content-between"})
    reviews = []
    for review in reviews_container:
        reviewer = review.find_all(name="div")[0].text.strip()
        reviewer_score = review.find_all(name="div")[1].text
        reviews.append({"reviewer": reviewer, "reviewer_score": reviewer_score})

    return reviews


def get_opencritic_developers(main_container: bs4.element.Tag) -> list:
    developers_list = []
    developers = main_container.find(name="div", attrs={"class": opencritic_types.COMPANIES}).find_all(name="span")
    for developer in developers:
        developers_list.append(developer.text)
    return developers_list


def get_opencritic_platforms(main_container: bs4.element.Tag) -> list:
    platform_list = []
    platforms = main_container.find(name="div", attrs={"class": opencritic_types.PLATFORMS}).find_all(name="span")
    for platform in platforms:
        platform_list.append(platform.text)
    return platform_list


def get_opencritic_release_date(main_container: bs4.element.Tag) -> str:
    return main_container.find(name="div", attrs={"class": opencritic_types.PLATFORMS}).text


def get_opencritic_title(main_container: bs4.element.Tag) -> str:
    return main_container.find(name="h1").text


def get_opencritic_scores_container(main_container: bs4.element.Tag) -> bs4.element.Tag:
    return main_container.find(name=opencritic_types.SCORES_CONTAINER)


def get_opencritic_critic_score(scores_container: bs4.element.Tag) -> str:
    return scores_container.find(name='div', attrs={"class": opencritic_types.CRITIC_DATA}).text.strip()


def get_opencritic_critic_recommend(scores_container: bs4.element.Tag) -> str:
    return scores_container.find_all(name='div', attrs={"class": opencritic_types.CRITIC_DATA})[1].text.strip()


def get_opencritic_critic_rating_img(scores_container: bs4.element.Tag) -> dict:
    return {"src": "https:{}".format(scores_container.find('img')['src']), "alt": scores_container.find("img")['alt']}
