from . import imdb_types
import bs4
"""List imdb functions"""
def get_description(element):
    description = []
    list_description = element.find_all("span", {"class": imdb_types.DESCRIPTION_LIST})
    for description_element in list_description:
        description.append(description_element.text)
    return description



"""Detail imdb functions"""

def get_container(soup: bs4.BeautifulSoup) -> bs4.element.Tag:
    return soup.find(name='main')

def get_title(container: bs4.element.Tag) -> str:
    return container.find(name="span", attrs={"class": imdb_types.TITLE}).text

def get_critic_reviews_number(container: bs4.element.Tag) -> str:
    return container.find_all(name="span", attrs={"class": imdb_types.SCORE})[1].text

def get_user_reviews_number(container: bs4.element.Tag) -> str:
    return container.find_all(name="span", attrs={"class": imdb_types.SCORE})[0].text

def get_metascore(container: bs4.element.Tag) -> str:
    return container.find(name="span", attrs={"class": imdb_types.METASCORE}).text

def get_popularity(container: bs4.element.Tag) -> str:
    return container.find(name="div", attrs={"data-testid": imdb_types.POPULARITY}).text

def get_imdb_rating_based_on(container: bs4.element.Tag) -> str:
    return container.find(name="div", attrs={"class": imdb_types.IMDB_RATING_BASED_ON}).text

def get_imdb_rating(container: bs4.element.Tag) -> str:
    imdb_rating_container = container.find(name="div",
                                           attrs={"data-testid": imdb_types.IMDB_RATING_CONTAINER}).find_all(
        name="span")
    return "{}{}".format(imdb_rating_container[0].text, imdb_rating_container[1].text)

def get_data(container: bs4.element.Tag) -> list:
    data_container = container.find(name="ul", attrs={"class": imdb_types.DATA_CONTAINER})
    data_results = data_container.find_all(name="a")
    data = []
    for data_res in data_results:
        data.append(data_res.text)
    return data

def get_presentations(container: bs4.element.Tag) -> list:
    presentations = []
    presentations_container = container.find(name="div", attrs={"class": imdb_types.PRESENTATION_CONTAINER}).find_all(
        name="li", attrs={
            "class": imdb_types.PRESENTATION_ELEMENTS})

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

    return presentations

def get_more_like_this(container: bs4.element.Tag) -> list:
    more_like_this_container = container.find_all(name="div", attrs={"class": imdb_types.MORE_LIKE_THIS_CONTAINER})
    list_more_like_this = []
    for more_like_this in more_like_this_container:
        more_like_this_title = more_like_this.find(name="span",
                                                   attrs={"data-testid": imdb_types.MORE_LIKE_THIS_ELEMENT_TITLE}).text
        more_like_this_rating = more_like_this.find(name="div",
                                                    attrs={"class": imdb_types.MORE_LIKE_THIS_ELEMENT_RATING}).find(
            name="span").text
        more_like_this_image = {"src": more_like_this.find(name="img")["src"],
                                "alt": more_like_this.find(name="img")["alt"]}
        list_more_like_this.append({"title": more_like_this_title, "more_like_this_rating": more_like_this_rating,
                                    "more_like_this_image": more_like_this_image})

    return list_more_like_this

def get_actors(container: bs4.element.Tag) -> list:
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
    return actors

def get_photos(container: bs4.element.Tag) -> list:
    photos_container = container.find_all(name="div", attrs={"class": imdb_types.PHOTOS_CONTAINER})
    photos = []
    for photo in photos_container:
        temp_photo = {"src": photo.find(name="img")["src"], "alt": photo.find(name="img")["alt"]}
        photos.append(temp_photo)
    return photos
