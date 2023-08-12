import bs4

from . import metacritic_types
import re

def get_result_container(soup: bs4.BeautifulSoup):
    return soup.select(metacritic_types.SELECT_RESULT_CONTAINER)
def get_name(result_element):
    return result_element.find("h3", {"class": metacritic_types.TITLE}).find('a').text.strip()

def get_metascore(result_element):
    return result_element.find("span", {"class": metacritic_types.METASCORE}).text


def get_platforms(result_element):
    return result_element.find("span", {"class": metacritic_types.PLATFORM}).text


def get_img(result_element):
    return result_element.find("img")['src']


def get_year(result_element):
    return re.search(r"(\d{4})", result_element.find("p", {"class": None}).text.strip().lower()).group(1)

def get_types(result_element):
    return result_element.find("p", {"class": None}).text.strip().lower().replace(' ', '').replace('\n\n', ',').split(',')