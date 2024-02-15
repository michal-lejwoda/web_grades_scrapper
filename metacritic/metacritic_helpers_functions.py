from typing import Optional

import bs4
from slugify import slugify

from metacritic import metacritic_types
from metacritic.metacritic_types import DETAIL_TITLE

"""List metacritic functions"""


def get_result_container(soup: bs4.BeautifulSoup) -> Optional[bs4.element.ResultSet]:
    try:
        select_container = soup.select(metacritic_types.SELECT_CONTAINER)
        result = select_container[0].find_all(attrs={"class": "u-grid-columns"}, name="div")
        return result
    except AttributeError:
        return None


def get_name(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("p", {"class": metacritic_types.TITLE}).text.strip()
    except AttributeError:
        return None


def get_metascore(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("div", {"class": metacritic_types.METASCORE}).find("span").text
    except AttributeError:
        return None


def get_platforms(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("div", {"class": metacritic_types.PLATFORM}).find("span",
                                                                                     {"class": None}).text.strip()
    except AttributeError:
        return None


def get_img(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("img", {"class": 'g-container-rounded-small'})['src']
    except (AttributeError, TypeError):
        return None


def get_year(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("span", {'class': 'u-text-uppercase'}).text.strip().lower()
    except AttributeError:
        return None


def get_types(result_element: bs4.element.Tag) -> Optional[str]:
    try:
        return result_element.find("span", {"class": "c-tagList_button"}).text.lower()
    except (AttributeError, IndexError):
        return None


def get_url(name: str, type_of_result: str) -> Optional[str]:
    try:
        return ("https://www.metacritic.com/{}/{}".format
                (slugify(type_of_result), slugify(name)))
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


def get_rest_platforms(soup: bs4.BeautifulSoup) -> list:
    try:
        all_platform_data = []
        product_platforms_container = soup.select(".c-gamePlatformsSection_list")
        list_of_platforms_containers = product_platforms_container[0].find_all(name="a",
                                                                               attrs={"class": "c-gamePlatformTile"})
        for platform in list_of_platforms_containers:
            platform_name = get_platform_name(platform)
            critic_based_on = get_critic_based_on_text(platform)
            critic_score = get_critic_score(platform)
            all_platform_data.append({"critic_score": critic_score, "critic_based_on": critic_based_on,
                                      'platform': platform_name})
        return all_platform_data
    except (AttributeError, IndexError):
        return None


def get_genres(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        genres = main_container.find_all(name='li', attrs={"class": 'c-genreList_item'})
        list_of_genres = []
        for genre in genres:
            list_of_genres.append(genre.text.strip())
            return list_of_genres
    except AttributeError:
        return None


def get_developers(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        return_developers = []
        developers = main_container.find(name='div', attrs={"class": "c-gameDetails_Developer"}).find_all(name="li",
                                                                                                          attrs={
                                                                                                              "class": "c-gameDetails_listItem"})
        for developer in developers:
            return_developers.append(developer.text.strip())
        return ", ".join(return_developers)
    except AttributeError:
        return None

def get_main_image(main_container: bs4.element.Tag):
    main_image = main_container.find_all(name='picture')[0].find(name='img')['src']
    return main_image

def get_title(main_container: bs4.element.Tag) -> str:
    title = main_container.find(name='div', attrs={"class": DETAIL_TITLE}).text.strip()
    return title
def get_publishers(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        return_publishers = []
        developers = main_container.find(name='div', attrs={"class": "c-gameDetails_Distributor"}).find_all(
            name="span")[1:]
        for developer in developers:
            return_publishers.append(developer.text.strip())
        return ", ".join(return_publishers)
    except AttributeError:
        return None


def get_release_date(main_container: bs4.element.Tag) -> Optional[list]:
    try:
        release_date = main_container.find(name='div', attrs={"class": "c-gameDetails_ReleaseDate"}).find_all(
            name="span")[1].text
        return release_date
    except AttributeError:
        return None


def get_summary(main_container: bs4.element.Tag) -> Optional[str]:
    try:
        return main_container.find(name='span', attrs={"class": metacritic_types.SUMMARY}).text
    except AttributeError:
        return None


def get_platform_name(platform):
    try:
        return platform.find(name="title", attrs={"class": None}).text
    except AttributeError:
        return None


def get_critic_based_on_text(platform):
    try:
        return platform.find(name="p", attrs={"class": "g-text-xsmall"}).text.strip()
    except AttributeError:
        return None


def get_critic_score(platform):
    try:
        return platform.find(name="span", attrs={"class": None}).text.strip()
    except AttributeError:
        return None


def get_user_data(main_container: bs4.element.Tag) -> Optional[str]:
    try:
        user_reviews_container = main_container.find(name="div", attrs={"class": "c-reviewsSection_userReviews"}).find(name="div", attrs={"class": "c-reviewsSummaryHeader"})
        user_score_sentiment = get_user_score_sentiment(user_reviews_container)
        user_score = get_user_score(user_reviews_container)
        user_based_on = get_user_based_on(user_reviews_container)
        return {"user_score_sentiment": user_score_sentiment, "user_score": user_score, "user_based_on": user_based_on}
    except:
        return None


def get_user_score_sentiment(user_reviews_container: bs4.element.Tag) -> Optional[str]:
    try:
        return user_reviews_container.find(name="span",
                                           attrs={"class": "c-ScoreCard_scoreSentiment"}).text.strip()

    except AttributeError:
        return None


def get_user_score(user_reviews_container: bs4.element.Tag) -> Optional[str]:
    try:
        return user_reviews_container.find(name="div",
                                           attrs={"class": "c-siteReviewScore"}).text
    except AttributeError:
        return None


def get_user_based_on(user_reviews_container: bs4.element.Tag) -> Optional[str]:
    try:
        return user_reviews_container.find(name="span", attrs={"class": "c-ScoreCard_reviewsTotal"}).text
    except AttributeError:
        return None
