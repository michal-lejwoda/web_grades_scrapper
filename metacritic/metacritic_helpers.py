import bs4
import requests

from helpers import create_session
from . import metacritic_types
from .metacritic_helpers_functions import get_name, get_metascore, get_platforms, get_img, get_year, get_types, \
    get_result_container


def list_metacritic_games(soup: bs4.BeautifulSoup) -> list:
    list_of_elements = []
    results = get_result_container(soup)
    for result_element in results:
        name = get_name(result_element)
        result = get_metascore(result_element)
        platforms = get_platforms(result_element)
        img = get_img(result_element)
        year = get_year(result_element)
        types = get_types(result_element)
        list_element = {"platforms": platforms, "img": img, "year": year, "metascore": result, "type": types[1],
                    "name": name}
        list_of_elements.append(list_element)
    return list_of_elements

def detail_metacritic_games(soup: bs4.BeautifulSoup) -> list:
    all_platform_data = []
    session = create_session()
    # session = requests.Session()
    # session.headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    product_platforms = soup.select(metacritic_types.SELECT_DETAIL_PLATFORMS_CONTAINER)
    rest = product_platforms[0].find("span", {"class": "data"})
    rest_platforms = rest.find_all("a", href=True)
    main_container = soup.select(metacritic_types.SELECT_DETAIL_MAIN_CONTAINER)[0]
    genres = main_container.find(name='li', attrs={"class": metacritic_types.GENRES}).find_all(name="span",
                                                                                               attrs={"class": "data"})
    developers = main_container.find(name='li', attrs={"class": metacritic_types.DEVELOPERS}).find_all(name='a')
    current_genres = []
    current_developers = []
    summary = main_container.find(name='span', attrs={"class": metacritic_types.SUMMARY}).text
    for genre in genres:
        current_genres.append(genre.text)
    for developer in developers:
        current_developers.append(developer.text)
    for platform in rest_platforms:
        response = session.get("https://www.metacritic.com{}".format(platform['href']))
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        main_container = soup.select(metacritic_types.SELECT_DETAIL_MAIN_CONTAINER)[0]
        img_container = main_container.find("img")
        single_platform_summary = main_container.find("div", {"class": metacritic_types.SINGLE_PLATFORM_SUMMARY})
        try:
            critic_score = single_platform_summary.find(name="span", attrs={"itemprop": metacritic_types.CRITIC_SCORE}).text
            critic_based_on = single_platform_summary.find(name="span", attrs={"class": metacritic_types.CRITIC_BASED_ON}).find("a").find(
                "span").text.strip()
        except:
            critic_score = None
            critic_based_on = None
        user_score = single_platform_summary.find(name="div", attrs={"class": metacritic_types.USER_SCORE}).text
        user_based_on = single_platform_summary.find(name="div", attrs={"class": metacritic_types.USER_BASED_ON}).find(
            name="span", attrs={"class": metacritic_types.CRITIC_BASED_ON}).find("a").text.strip().split(" ")[0]
        img = {
            "src": img_container['src'],
            "alt": img_container['alt']
        }
        current_platform = main_container.find(name="span", attrs={"class": metacritic_types.PLATFORM}).find("a").text.strip()
        all_platform_data.append({"critic_score": critic_score, "critic_based_on": critic_based_on,
                                  "user_score": user_score, "user_based_on": user_based_on,
                                  "img": img, 'platform': current_platform, })
    results = {"developers": current_developers, "genres": current_genres, "summary": summary,
               "platforms_data": all_platform_data}
    return results