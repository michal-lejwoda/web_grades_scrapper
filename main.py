import os
from fastapi import FastAPI
import requests
from slugify import slugify
import bs4
import re
from dotenv import load_dotenv

from helpers import get_soup, create_url
from metacritic_helpers import list_metacritic_games

load_dotenv('.env')
app = FastAPI()
HOST = os.getenv("RAPID_API_HOST")
API_KEY = os.getenv("RAPID_API_KEY")
@app.get("/")
async def root():
    content = "red dead redemption 2"
    url_template = "https://www.metacritic.com/search/game/{}/results"
    url = create_url(url_template, content)
    soup = get_soup(url)
    return list_metacritic_games(soup)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/metacritic")
async def metacritic():
    content = "red dead redemption 2"
    url_template = "https://www.metacritic.com/search/game/{}/results"
    url = create_url(url_template, content)
    soup = get_soup(url)
    return list_metacritic_games(soup)


@app.get("/opencritic")
async def opencritic():
    content = "red dead redemption 2"
    url = "https://opencritic-api.p.rapidapi.com/game/search"
    querystring = {"criteria": content}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": HOST
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


@app.get("/imdb")
async def imdb():
    res_arr = []
    content = "red dead redemption 2"
    content_slugify = slugify(content)
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    r = session.get("https://www.imdb.com/find/?q={}&ref_=nv_sr_sm".format(content_slugify), allow_redirects=False)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
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


@app.get("/metacritic_detail")
async def metacritic_detail():
    all_platform_data = []
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    r = session.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2", allow_redirects=False)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    product_platforms = soup.select('.product_platforms')
    rest = product_platforms[0].find("span", {"class": "data"})
    rest_platforms = rest.find_all("a", href=True)
    main_container = soup.select('#main')[0]
    genres = main_container.find(name='li', attrs={"class": "product_genre"}).find_all(name="span",
                                                                                       attrs={"class": "data"})
    developers = main_container.find(name='li', attrs={"class": "developer"}).find_all(name='a')
    current_genres = []
    current_developers = []
    summary = main_container.find(name='span', attrs={"class": "blurb_expanded"}).text
    for genre in genres:
        current_genres.append(genre.text)
    for developer in developers:
        current_developers.append(developer.text)
    for platform in rest_platforms:
        response = session.get("https://www.metacritic.com{}".format(platform['href']))
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        main_container = soup.select('#main')[0]
        img_container = main_container.find("img")
        single_platform_summary = main_container.find("div", {"class": "summary_wrap"})
        try:
            critic_score = single_platform_summary.find(name="span", attrs={"itemprop": "ratingValue"}).text
            critic_based_on = single_platform_summary.find(name="span", attrs={"class": "count"}).find("a").find(
                "span").text.strip()
        except:
            critic_score = None
            critic_based_on = None
        user_score = single_platform_summary.find(name="div", attrs={"class": "user"}).text
        user_based_on = single_platform_summary.find(name="div", attrs={"class": "side_details"}).find(
            name="span", attrs={"class": "count"}).find("a").text.strip().split(" ")[0]
        img = {
            "src": img_container['src'],
            "alt": img_container['alt']
        }
        current_platform = main_container.find(name="span", attrs={"class": "platform"}).find("a").text.strip()
        all_platform_data.append({"critic_score": critic_score, "critic_based_on": critic_based_on,
                                  "user_score": user_score, "user_based_on": user_based_on,
                                  "img": img, 'platform': current_platform, })
    results = {"developers": current_developers, "genres": current_genres, "summary": summary,
               "platforms_data": all_platform_data}
    return results


@app.get("/opencritic_detail")
async def opencritic_detail():
    current_developers = []
    current_platforms = []
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    r = session.get("https://opencritic.com/game/10993/deathloop", allow_redirects=False)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    container = soup.select('app-root')[0]
    img_container = container.find(name="picture").find(name="img")
    img = {
        "src": img_container['src'],
        "alt": img_container['alt']
    }
    reviews_container = container.find(name='app-rapid-review-list').find_all(name="div",attrs={"class": "justify-content-between"})
    reviews = []
    for review in reviews_container:
        reviewer = review.find_all(name="div")[0].text.strip()
        reviewer_score = review.find_all(name="div")[1].text
        reviews.append({"reviewer":reviewer, "reviewer_score": reviewer_score})

    release_date = container.find(name="div", attrs={"class": "platforms"}).text
    platforms = container.find(name="div", attrs={"class": "platforms"}).find_all(name="span")
    developers = container.find(name="div", attrs={"class": "companies"}).find_all(name="span")
    title = container.find(name="h1").text
    scores_container = container.find(name="app-game-scores-display")
    critic_score = scores_container.find(name='div', attrs={"class": "inner-orb"}).text.strip()
    critic_recommend = scores_container.find_all(name='div', attrs={"class": "inner-orb"})[1].text.strip()
    critic_rating_img = {"src": scores_container.find('img')['src'], "alt": scores_container.find("img")['alt']}

    for developer in developers:
        current_developers.append(developer.text)
    for platform in platforms:
        current_platforms.append(platform.text)
    all_platform_data ={"developers": current_developers, "title": title, "release_date": release_date,
        "platforms": current_platforms, "img": img, "critic_score": critic_score, "critic_recommend": critic_recommend,
        "critic_rating_img": critic_rating_img, "reviews": reviews}
    return all_platform_data

@app.get("/imdb_detail")
async def imdb_detail():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    r = session.get("https://www.imdb.com/title/tt0120815/", allow_redirects=False)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    container = soup.find(name='main')
    title = container.find(name="span", attrs={"class": "sc-afe43def-1"}).text
    data_container = container.find(name="ul", attrs={"class": "sc-afe43def-4"})
    data_results = data_container.find_all(name="a")
    data = []
    for data_res in data_results:
        data.append(data_res.text)
    imdb_rating_container = container.find(name="div", attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"}).find_all(name="span")
    imdb_rating = "{}{}".format(imdb_rating_container[0].text, imdb_rating_container[1].text)
    imdb_rating_based_on = container.find(name="div", attrs={"class":"bjjENQ"}).text
    #Nie zawsze jest
    popularity = container.find(name="div", attrs={"data-testid": "hero-rating-bar__popularity__score"}).text
    presentations_container = container.find(name="div", attrs={"class": "hKIseD"}).find_all(name="li", attrs={"class": "ipc-metadata-list__item"})
    presentations = []
    for presentation in presentations_container:
        try:
            label = presentation.find(name="span", attrs={"class": "ipc-metadata-list-item__label"}).text
        except:
            label = presentation.find(name="a", attrs={"class": "ipc-metadata-list-item__label"}).text
        li_presentation = presentation.find_all(name="li", attrs={"class": "ipc-inline-list__item"})
        li_presentation_results = []
        for li in li_presentation:
            li_presentation_results.append(li.find(name="a").text.strip())
        presentations.append({"label": label, "presentation": li_presentation_results})
    metascore = container.find(name="span", attrs={"class": "score-meta"}).text
    user_reviews_number = container.find_all(name="span", attrs={"class": "score"})[0].text
    critic_reviews_number = container.find_all(name="span", attrs={"class": "score"})[1].text
    photos_container = container.find_all(name="div", attrs={"class": "ipc-media ipc-media--photo"})
    photos = []
    for photo in photos_container:
        temp_photo = {"src": photo.find(name="img")["src"], "alt": photo.find(name="img")["alt"]}
        photos.append(temp_photo)
    actors_container = container.find_all(name="div", attrs={"class": "kUzsHJ"})
    actors = []
    for actor in actors_container:
        if actor.find(name="img") == None:
            actor_img = {"src": None, "alt": None}
        else:
            actor_img = {"src": actor.find(name="img")['src'], "alt": actor.find(name="img")['alt']}
        actor_name = actor.find(name="a", attrs={"class": "fUguci"}).text
        actor_character = actor.find(name="span", attrs={"class": "llsTve"}).text
        actors.append({"actor_img": actor_img, "actor_name": actor_name, "actor_character": actor_character})
    more_like_this_container = container.find_all(name="div", attrs={"class": "ipc-poster-card"})
    more_like_this_arr = []
    for more_like_this in more_like_this_container:
        more_like_this_title = more_like_this.find(name="span", attrs={"data-testid": "title"}).text
        more_like_this_rating = more_like_this.find(name="div", attrs={"class": "ipc-rating-star-group"}).find(name="span").text
        more_like_this_image = {"src": more_like_this.find(name="img")["src"], "alt": more_like_this.find(name="img")["alt"]}
        more_like_this_arr.append({"title": more_like_this_title, "more_like_this_rating": more_like_this_rating, "more_like_this_image": more_like_this_image})
    return {"data": data, "title": title, "presentations": presentations,
            "imdb_rating": imdb_rating, "imdb_rating_based_on": imdb_rating_based_on,
            "popularity": popularity, "metascore": metascore, "user_reviews_number": user_reviews_number,
            "critic_reviews_number": critic_reviews_number, "actors": actors, "more_like_this": more_like_this_arr}