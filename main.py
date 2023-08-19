from typing import Optional

from fastapi import FastAPI
from slugify import slugify
from dotenv import load_dotenv

from helpers import get_soup, create_url
from imdb.imdb_helpers import get_imdb_movies_list, detail_imdb_movie
from metacritic.metacritic_helpers import list_metacritic_games, detail_metacritic_games
from opencritic.opencritic_helpers import get_opencritic_games_list_json, detail_opencritic_games
from schemas import NameSchema, UrlSchema

load_dotenv('.env')
app = FastAPI()


@app.get("/")
async def root():
    url_template = "https://www.imdb.com/title/tt0120815/"
    soup = get_soup(url_template)
    movie_detail = detail_imdb_movie(soup)
    return movie_detail


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/metacritic")
async def metacritic(name_schema: NameSchema) -> list:
    name = name_schema.name
    url_template = "https://www.metacritic.com/search/game/{}/results"
    url = create_url(url_template, name)
    soup = get_soup(url)
    return list_metacritic_games(soup)


@app.post("/opencritic")
async def opencritic(name_schema: NameSchema) -> Optional[list]:
    #TODO: GET More Data and add url
    name = name_schema.name
    url_template = "https://opencritic-api.p.rapidapi.com/game/search"
    opencritic_games_list = get_opencritic_games_list_json(url_template, name)
    if opencritic_games_list == None:
        return "Can't get data. :("
    return opencritic_games_list


@app.post("/imdb")
async def imdb(name_schema: NameSchema) -> list:
    name = name_schema.name
    name_slugify = slugify(name)
    url_template = "https://www.imdb.com/find/?q={}&ref_=nv_sr_sm"
    url = create_url(url_template, name_slugify)
    soup = get_soup(url)
    return get_imdb_movies_list(soup)


@app.post("/metacritic_detail")
async def metacritic_detail(urlschema: UrlSchema):
    url_template = urlschema.url
    # url_template = "https://www.metacritic.com/game/xbox-one/red-dead-redemption-2"
    soup = get_soup(url_template)
    game_detail = detail_metacritic_games(soup)
    return game_detail


@app.post("/opencritic_detail")
async def opencritic_detail(urlschema: UrlSchema):
    url_template = urlschema.url
    url_template = "https://opencritic.com/game/10993/deathloop"
    soup = get_soup(url_template)
    game_detail = detail_opencritic_games(soup)
    return game_detail


@app.post("/imdb_detail")
async def imdb_detail(urlschema: UrlSchema):
    url_template = urlschema.url
    # url_template = "https://www.imdb.com/title/tt0120815/"
    soup = get_soup(url_template)
    movie_detail = detail_imdb_movie(soup)
    return movie_detail
