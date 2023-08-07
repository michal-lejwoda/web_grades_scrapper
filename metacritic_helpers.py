import array
import bs4
import re

def list_metacritic_games(soup: bs4.BeautifulSoup) -> array:
    list_of_games = []
    all_results = soup.select('.result')
    for number, i in enumerate(all_results):
        name = i.find("h3", {"class": "product_title"}).find('a').text.strip()
        result = i.find("span", {"class": "metascore_w"}).text
        platforms = i.find("span", {"class": "platform"}).text
        img = i.find("img")['src']
        year = re.search(r"(\d{4})", i.find("p", {"class": None}).text.strip().lower()).group(1)
        temp_list = i.find("p", {"class": None}).text.strip().lower().replace(' ', '').replace('\n\n', ',').split(',')
        temp_obj = {"platforms": platforms, "img": img, "year": year, "metascore": result, "type": temp_list[1],
                    "name": name}
        list_of_games.append(temp_obj)
    return list_of_games