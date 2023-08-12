import bs4
from . import imdb_types
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

def detail_imdb_movie(soup: bs4.BeautifulSoup) -> dict:
    container = soup.find(name='main')
    title = container.find(name="span", attrs={"class": imdb_types.TITLE}).text
    data_container = container.find(name="ul", attrs={"class": imdb_types.DATA_CONTAINER})
    data_results = data_container.find_all(name="a")
    data = []
    for data_res in data_results:
        data.append(data_res.text)
    imdb_rating_container = container.find(name="div",
                                           attrs={"data-testid": imdb_types.IMDB_RATING_CONTAINER}).find_all(
        name="span")
    imdb_rating = "{}{}".format(imdb_rating_container[0].text, imdb_rating_container[1].text)
    imdb_rating_based_on = container.find(name="div", attrs={"class": imdb_types.IMDB_RATING_BASED_ON}).text
    # Nie zawsze jest
    popularity = container.find(name="div", attrs={"data-testid": imdb_types.POPULARITY}).text
    presentations_container = container.find(name="div", attrs={"class": imdb_types.PRESENTATION_CONTAINER}).find_all(name="li", attrs={
        "class": "ipc-metadata-list__item"})
    presentations = []
    for presentation in presentations_container:
        try:
            label = presentation.find(name="span", attrs={"class": imdb_types.PRESENTATION_ELEMENTS_LABEL}).text
        except:
            label = presentation.find(name="a", attrs={"class": imdb_types.PRESENTATION_ELEMENTS_LABEL}).text
        li_presentation = presentation.find_all(name="li", attrs={"class": imdb_types.NESTED_PRESENTATION_ELEMENTS})
        li_presentation_results = []
        for li in li_presentation:
            li_presentation_results.append(li.find(name="a").text.strip())
        presentations.append({"label": label, "presentation": li_presentation_results})
    metascore = container.find(name="span", attrs={"class": imdb_types.METASCORE}).text
    user_reviews_number = container.find_all(name="span", attrs={"class": imdb_types.SCORE})[0].text
    critic_reviews_number = container.find_all(name="span", attrs={"class": imdb_types.SCORE})[1].text
    photos_container = container.find_all(name="div", attrs={"class": imdb_types.PHOTOS_CONTAINER})
    photos = []
    for photo in photos_container:
        temp_photo = {"src": photo.find(name="img")["src"], "alt": photo.find(name="img")["alt"]}
        photos.append(temp_photo)
    actors_container = container.find_all(name="div", attrs={"class": imdb_types.ACTORS_CONTAINER})
    actors = []
    for actor in actors_container:
        if actor.find(name="img") == None:
            actor_img = {"src": None, "alt": None}
        else:
            actor_img = {"src": actor.find(name="img")['src'], "alt": actor.find(name="img")['alt']}
        actor_name = actor.find(name="a", attrs={"class": imdb_types.ACTOR_NAME}).text
        actor_character = actor.find(name="span", attrs={"class": imdb_types.ACTOR_CHARACTER}).text
        actors.append({"actor_img": actor_img, "actor_name": actor_name, "actor_character": actor_character})
    more_like_this_container = container.find_all(name="div", attrs={"class": imdb_types.MORE_LIKE_THIS_CONTAINER})
    more_like_this_arr = []
    for more_like_this in more_like_this_container:
        more_like_this_title = more_like_this.find(name="span", attrs={"data-testid": imdb_types.MORE_LIKE_THIS_ELEMENT_TITLE}).text
        more_like_this_rating = more_like_this.find(name="div", attrs={"class": imdb_types.MORE_LIKE_THIS_ELEMENT_RATING}).find(
            name="span").text
        more_like_this_image = {"src": more_like_this.find(name="img")["src"],
                                "alt": more_like_this.find(name="img")["alt"]}
        more_like_this_arr.append({"title": more_like_this_title, "more_like_this_rating": more_like_this_rating,
                                   "more_like_this_image": more_like_this_image})
    return {"data": data, "title": title, "presentations": presentations,
            "imdb_rating": imdb_rating, "imdb_rating_based_on": imdb_rating_based_on,
            "popularity": popularity, "metascore": metascore, "user_reviews_number": user_reviews_number,
            "critic_reviews_number": critic_reviews_number, "actors": actors, "more_like_this": more_like_this_arr}