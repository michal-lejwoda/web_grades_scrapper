import re
from typing import Optional

import bs4
import requests.sessions

from . import metacritic_types

"""List metacritic functions"""


def get_result_container(soup: bs4.BeautifulSoup) -> Optional[bs4.element.ResultSet]:
    try:
        return soup.select(metacritic_types.SELECT_RESULT_CONTAINER)
    except AttributeError:
        return None


def get_name(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("h3", {"class": metacritic_types.TITLE}).find('a').text.strip()
    except AttributeError:
        return None


def get_metascore(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("span", {"class": metacritic_types.METASCORE}).text
    except AttributeError:
        return None


def get_platforms(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("span", {"class": metacritic_types.PLATFORM}).text
    except:
        return None


def get_img(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("img")['src']
    except AttributeError:
        return None


def get_year(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return re.search(r"(\d{4})", result_element.find("p", {"class": None}).text.strip().lower()).group(1)
    except AttributeError:
        return None


def get_types(result_element: bs4.element.Tag) -> Optional[list]:
    try:
        return result_element.find("p", {"class": None}).text.strip().lower().replace(' ', '').replace('\n\n',
                                                                                                       ',').split(
            ',')[1]
    except (AttributeError, IndexError):
        return None


def get_url(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return ("https://www.metacritic.com{}".format
                (result_element.find("h3", {"class": metacritic_types.TITLE}).find('a', href=True)['href']))
    except (AttributeError, IndexError):
        return None

def create_dict_without_none_objects(dict_elements: dict) -> dict:
    new_dict = {}
    for single_element in dict_elements.keys():
        if dict_elements[single_element] != None:
            new_dict[single_element] = dict_elements[single_element]
    return new_dict

"""Detail metacritic functions"""


def get_main_container(soup: bs4.BeautifulSoup) -> Optional[bs4.element.Tag]:
    try:
        return soup.select(metacritic_types.SELECT_DETAIL_MAIN_CONTAINER)[0]
    except (AttributeError, IndexError):
        return None


def get_rest_platforms(soup: bs4.BeautifulSoup, session: requests.sessions.Session) -> list:
    try:
        all_platform_data = []
        product_platforms_container = soup.select(metacritic_types.SELECT_DETAIL_PLATFORMS_CONTAINER)
        rest = product_platforms_container[0].find("span", {"class": "data"})
        rest_platforms = rest.find_all("a", href=True)
        for platform in rest_platforms:
            response = session.get("https://www.metacritic.com{}".format(platform['href']))
            soup = bs4.BeautifulSoup(response.text, 'lxml')
            main_container = soup.select(metacritic_types.SELECT_DETAIL_MAIN_CONTAINER)[0]
            img_container = main_container.find("img")
            single_platform_summary = main_container.find("div", {"class": metacritic_types.SINGLE_PLATFORM_SUMMARY})
            try:
                critic_score = single_platform_summary.find(name="span",
                                                            attrs={"itemprop": metacritic_types.CRITIC_SCORE}).text
                critic_based_on = single_platform_summary.find(name="span",
                                                               attrs={"class": metacritic_types.CRITIC_BASED_ON}).find(
                    "a").find(
                    "span").text.strip()
            except:
                critic_score = None
                critic_based_on = None
            user_score = single_platform_summary.find(name="div", attrs={"class": metacritic_types.USER_SCORE}).text
            user_based_on = \
                single_platform_summary.find(name="div", attrs={"class": metacritic_types.USER_BASED_ON}).find(
                    name="span", attrs={"class": metacritic_types.CRITIC_BASED_ON}).find("a").text.strip().split(" ")[0]
            img = {
                "src": img_container['src'],
                "alt": img_container['alt']
            }
            current_platform = main_container.find(name="span", attrs={"class": metacritic_types.PLATFORM}).find(
                "a").text.strip()
            all_platform_data.append({"critic_score": critic_score, "critic_based_on": critic_based_on,
                                      "user_score": user_score, "user_based_on": user_based_on,
                                      "img": img, 'platform': current_platform, })
        return all_platform_data
    except (AttributeError, IndexError):
        return None


def get_genres(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        genres_list = []
        genres = main_container.find(name='li', attrs={"class": metacritic_types.GENRES}).find_all(
            attrs={"class": "data"}, name="span")
        for genre in genres:
            genres_list.append(genre.text)
        return genres_list
    except AttributeError:
        return None


def get_developers(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        developers_list = []
        developers = main_container.find(name='li', attrs={"class": metacritic_types.DEVELOPERS}).find_all(name='a')
        for developer in developers:
            developers_list.append(developer.text)
        return developers_list
    except AttributeError:
        return None


def get_summary(main_container: bs4.element.Tag) -> Optional[str]:
    try:
        return main_container.find(name='span', attrs={"class": metacritic_types.SUMMARY}).text
    except AttributeError:
        return None
