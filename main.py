
from dotenv import load_dotenv
from fastapi import FastAPI
from slugify import slugify
from fastapi.middleware.cors import CORSMiddleware

from helpers import get_soup, create_url
from imdb.imdb_helpers import get_imdb_movies_list, detail_imdb_movie
from metacritic.metacritic_helpers import list_metacritic_games, detail_metacritic_games
from opencritic.opencritic_helpers import get_opencritic_games_list_json, detail_opencritic_games
from schemas import NameSchema, UrlOpencriticSchema, UrlMetacriticSchema, UrlImdbSchema

load_dotenv('.env')
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    url_template = "https://www.imdb.com/title/tt0120815/"
    soup = get_soup(url_template)
    movie_detail = detail_imdb_movie(soup)
    return movie_detail


@app.post("/metacritic")
async def metacritic(name_schema: NameSchema):
    name = name_schema.name
    url_template = "https://www.metacritic.com/search/game/{}/results"
    url = create_url(url_template, name)
    soup = get_soup(url)
    list_elements = list_metacritic_games(soup)
    return list_elements


@app.post("/opencritic")
async def opencritic(name_schema: NameSchema):
    name = name_schema.name
    url_template = "https://opencritic-api.p.rapidapi.com/game/search"
    opencritic_games_list = get_opencritic_games_list_json(url_template, name)
    return opencritic_games_list


@app.post("/imdb")
async def imdb(name_schema: NameSchema):
    name = name_schema.name
    name_slugify = slugify(name)
    url_template = "https://www.imdb.com/find/?q={}&ref_=nv_sr_sm"
    url = create_url(url_template, name_slugify)
    soup = get_soup(url)
    list_elements = get_imdb_movies_list(soup)
    return list_elements


@app.post("/metacritic_detail")
async def metacritic_detail(urlschema: UrlMetacriticSchema):
    url_template = urlschema.url
    soup = get_soup(url_template)
    game_detail = detail_metacritic_games(soup)
    return game_detail


@app.post("/opencritic_detail")
async def opencritic_detail(urlschema: UrlOpencriticSchema):
    url_template = urlschema.url
    soup = get_soup(url_template)
    game_detail = detail_opencritic_games(soup)
    return game_detail


@app.post("/imdb_detail")
async def imdb_detail(urlschema: UrlImdbSchema):
    url_template = urlschema.url
    soup = get_soup(url_template)
    movie_detail = detail_imdb_movie(soup)
    return movie_detail
