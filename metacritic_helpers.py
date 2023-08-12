import array
import bs4
import re
from metacritic_types import *
import requests


def list_metacritic_games(soup: bs4.BeautifulSoup) -> list:
    list_of_games = []
    all_results = soup.select(SELECT_RESULT_CONTAINER)
    for number, i in enumerate(all_results):
        name = i.find("h3", {"class": TITLE}).find('a').text.strip()
        result = i.find("span", {"class": METASCORE}).text
        platforms = i.find("span", {"class": PLATFORM}).text
        img = i.find("img")['src']
        year = re.search(r"(\d{4})", i.find("p", {"class": None}).text.strip().lower()).group(1)
        temp_list = i.find("p", {"class": None}).text.strip().lower().replace(' ', '').replace('\n\n', ',').split(',')
        temp_obj = {"platforms": platforms, "img": img, "year": year, "metascore": result, "type": temp_list[1],
                    "name": name}
        list_of_games.append(temp_obj)
    return list_of_games

def detail_metacritic_games(soup: bs4.BeautifulSoup) -> list:
    all_platform_data = []
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    product_platforms = soup.select(SELECT_DETAIL_PLATFORMS_CONTAINER)
    rest = product_platforms[0].find("span", {"class": "data"})
    rest_platforms = rest.find_all("a", href=True)
    main_container = soup.select(SELECT_DETAIL_MAIN_CONTAINER)[0]
    genres = main_container.find(name='li', attrs={"class": GENRES}).find_all(name="span",
                                                                                       attrs={"class": "data"})
    developers = main_container.find(name='li', attrs={"class": DEVELOPERS}).find_all(name='a')
    current_genres = []
    current_developers = []
    summary = main_container.find(name='span', attrs={"class": SUMMARY}).text
    for genre in genres:
        current_genres.append(genre.text)
    for developer in developers:
        current_developers.append(developer.text)
    for platform in rest_platforms:
        response = session.get("https://www.metacritic.com{}".format(platform['href']))
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        main_container = soup.select(SELECT_DETAIL_MAIN_CONTAINER)[0]
        img_container = main_container.find("img")
        single_platform_summary = main_container.find("div", {"class": SINGLE_PLATFORM_SUMMARY})
        try:
            critic_score = single_platform_summary.find(name="span", attrs={"itemprop": CRITIC_SCORE}).text
            critic_based_on = single_platform_summary.find(name="span", attrs={"class": CRITIC_BASED_ON}).find("a").find(
                "span").text.strip()
        except:
            critic_score = None
            critic_based_on = None
        user_score = single_platform_summary.find(name="div", attrs={"class": USER_SCORE}).text
        user_based_on = single_platform_summary.find(name="div", attrs={"class": USER_BASED_ON}).find(
            name="span", attrs={"class": CRITIC_BASED_ON}).find("a").text.strip().split(" ")[0]
        img = {
            "src": img_container['src'],
            "alt": img_container['alt']
        }
        current_platform = main_container.find(name="span", attrs={"class": PLATFORM}).find("a").text.strip()
        all_platform_data.append({"critic_score": critic_score, "critic_based_on": critic_based_on,
                                  "user_score": user_score, "user_based_on": user_based_on,
                                  "img": img, 'platform': current_platform, })
    results = {"developers": current_developers, "genres": current_genres, "summary": summary,
               "platforms_data": all_platform_data}
    return results