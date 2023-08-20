from typing import Optional

from . import imdb_types
import bs4

"""List imdb functions"""


def get_list_container(soup: bs4.BeautifulSoup) -> Optional[bs4.element.ResultSet]:
    try:
        return soup.select(imdb_types.LIST_CONTAINER)
    except AttributeError:
        return None


def get_list_title(element: bs4.element.Tag) -> Optional[str]:
    try:
        return element.find("a", {"class": imdb_types.LIST_TITLE}).text
    except AttributeError:
        return None


def get_list_description(element: bs4.element.Tag) -> Optional[list]:
    try:
        description = []
        list_description = element.find_all("span", {"class": imdb_types.DESCRIPTION_LIST})
        for description_element in list_description:
            description.append(description_element.text)
        return description
    except (AttributeError, IndexError):
        return None


def get_list_url(element: bs4.element.Tag) -> Optional[str]:
    try:
        return ("https://www.imdb.com{}"
                .format(element.find("a", {"class": imdb_types.LIST_TITLE}, href=True)['href']))
    except AttributeError:
        return None


"""Detail imdb functions"""


def get_container(soup: bs4.BeautifulSoup) -> Optional[bs4.element.Tag]:
    try:
        return soup.find(name='main')
    except AttributeError:
        return None


def get_title(container: bs4.element.Tag) -> Optional[str]:
    try:
        return container.find(name="span", attrs={"class": imdb_types.TITLE}).text
    except AttributeError:
        return None


def get_critic_reviews_number(container: bs4.element.Tag) -> Optional[str]:
    try:
        return container.find_all(name="span", attrs={"class": imdb_types.SCORE})[1].text
    except (AttributeError, IndexError):
        return None


def get_user_reviews_number(container: bs4.element.Tag) -> Optional[str]:
    try:
        return container.find_all(name="span", attrs={"class": imdb_types.SCORE})[0].text
    except (AttributeError, IndexError):
        return None


def get_metascore(container: bs4.element.Tag) -> Optional[str]:
    try:
        return container.find(name="span", attrs={"class": imdb_types.METASCORE}).text
    except AttributeError:
        return None


def get_popularity(container: bs4.element.Tag) -> Optional[str]:
    try:
        return container.find(name="div", attrs={"data-testid": imdb_types.POPULARITY}).text
    except AttributeError:
        return None


def get_imdb_rating_based_on(container: bs4.element.Tag) -> Optional[str]:
    try:
        return container.find(name="div", attrs={"class": imdb_types.IMDB_RATING_BASED_ON}).text
    except AttributeError:
        return None


def get_imdb_rating(container: bs4.element.Tag) -> Optional[str]:
    try:
        imdb_rating_container = container.find(name="div",
                                               attrs={"data-testid": imdb_types.IMDB_RATING_CONTAINER}).find_all(
            name="span")
        return "{}{}".format(imdb_rating_container[0].text, imdb_rating_container[1].text)
    except AttributeError:
        return None


def get_data(container: bs4.element.Tag) -> Optional[list]:
    try:
        data_container = container.find(name="ul", attrs={"class": imdb_types.DATA_CONTAINER})
        data_results = data_container.find_all(name="a")
        data = []
        for data_res in data_results:
            data.append(data_res.text)
        return data
    except (AttributeError, IndexError):
        return None


def get_presentations(container: bs4.element.Tag) -> Optional[list]:
    try:
        presentations = []
        presentations_container = container.find(name="div",
                                                 attrs={"class": imdb_types.PRESENTATION_CONTAINER}).find_all(
            name="li", attrs={
                "class": imdb_types.PRESENTATION_ELEMENTS})

        for presentation in presentations_container:
            try:
                label = presentation.find(name="span", attrs={"class": imdb_types.PRESENTATION_ELEMENTS_LABEL}).text
            except AttributeError:
                label = presentation.find(name="a", attrs={"class": imdb_types.PRESENTATION_ELEMENTS_LABEL}).text
            li_presentation = presentation.find_all(name="li", attrs={"class": imdb_types.NESTED_PRESENTATION_ELEMENTS})
            li_presentation_results = []
            for li in li_presentation:
                li_presentation_results.append(li.find(name="a").text.strip())
            presentations.append({"label": label, "presentation": li_presentation_results})

        return presentations
    except (AttributeError, IndexError):
        return None


def get_more_like_this(container: bs4.element.Tag) -> Optional[list]:
    try:
        more_like_this_container = container.find_all(name="div", attrs={"class": imdb_types.MORE_LIKE_THIS_CONTAINER})
        list_more_like_this = []
        for more_like_this in more_like_this_container:
            more_like_this_title = more_like_this.find(name="span",
                                                       attrs={
                                                           "data-testid": imdb_types.MORE_LIKE_THIS_ELEMENT_TITLE}).text
            more_like_this_rating = more_like_this.find(name="div",
                                                        attrs={"class": imdb_types.MORE_LIKE_THIS_ELEMENT_RATING}).find(
                name="span").text
            more_like_this_image = {"src": more_like_this.find(name="img")["src"],
                                    "alt": more_like_this.find(name="img")["alt"]}
            list_more_like_this.append({"title": more_like_this_title, "more_like_this_rating": more_like_this_rating,
                                        "more_like_this_image": more_like_this_image})

        return list_more_like_this
    except (AttributeError, IndexError):
        return None


def get_actors(container: bs4.element.Tag) -> Optional[list]:
    try:
        actors_container = container.find_all(name="div", attrs={"class": imdb_types.ACTORS_CONTAINER})
        actors = []
        for actor in actors_container:
            if actor.find(name="img") is None:
                actor_img = {"src": None, "alt": None}
            else:
                actor_img = {"src": actor.find(name="img")['src'], "alt": actor.find(name="img")['alt']}
            actor_name = actor.find(name="a", attrs={"class": imdb_types.ACTOR_NAME}).text
            actor_character = actor.find(name="span", attrs={"class": imdb_types.ACTOR_CHARACTER}).text
            actors.append({"actor_img": actor_img, "actor_name": actor_name, "actor_character": actor_character})
        return actors
    except AttributeError:
        return None


def get_photos(container: bs4.element.Tag) -> Optional[list]:
    try:
        photos_container = container.find_all(name="div", attrs={"class": imdb_types.PHOTOS_CONTAINER})
        photos = []
        for photo in photos_container:
            temp_photo = {"src": photo.find(name="img")["src"], "alt": photo.find(name="img")["alt"]}
            photos.append(temp_photo)
        return photos
    except (AttributeError, IndexError):
        return None
