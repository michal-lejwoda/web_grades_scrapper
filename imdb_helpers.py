import bs4
def get_imdb_movies_list(soup: bs4.BeautifulSoup) -> list:
    res_arr = []
    all_results = soup.select('.ipc-metadata-list-summary-item')
    for result in all_results:
        title = result.find("a", {"class": "ipc-metadata-list-summary-item__t"}).text
        finded_all = result.find_all("span", {"class": "ipc-metadata-list-summary-item__li"})
        description_arr = []
        for i in finded_all:
            description_arr.append(i.text)
        temp_obj = {"title": title, "description_arr": description_arr}
        res_arr.append(temp_obj)
    return res_arr