import os
from fastapi import FastAPI
import requests
from slugify import slugify
import bs4
import re
from dotenv import load_dotenv

from helpers import get_soup, create_url
from imdb_helpers import get_imdb_movies_list, detail_imdb_movie
from metacritic_helpers import list_metacritic_games, detail_metacritic_games
from opencritic_helpers import get_opencritic_games_list_json, detail_opencritic_games

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


@app.get("/metacritic")
async def metacritic() -> list:
    name = "red dead redemption 2"
    url_template = "https://www.metacritic.com/search/game/{}/results"
    url = create_url(url_template, name)
    soup = get_soup(url)
    return list_metacritic_games(soup)


@app.get("/opencritic")
async def opencritic()-> list:
    content = "red dead redemption 2"
    url_template = "https://opencritic-api.p.rapidapi.com/game/search"
    opencritic_games_list = get_opencritic_games_list_json(url_template, content)
    return opencritic_games_list


@app.get("/imdb")
async def imdb() -> list:
    name = "red dead redemption 2"
    name_slugify = slugify(name)
    url_template = "https://www.imdb.com/find/?q={}&ref_=nv_sr_sm"
    url = create_url(url_template, name_slugify)
    soup = get_soup(url)
    list_of_imdb_movies = get_imdb_movies_list(soup)
    return list_of_imdb_movies


@app.get("/metacritic_detail")
async def metacritic_detail():
    url_template = "https://www.metacritic.com/game/xbox-one/red-dead-redemption-2"
    soup = get_soup(url_template)
    game_detail = detail_metacritic_games(soup)
    return game_detail


@app.get("/opencritic_detail")
async def opencritic_detail():
    url_template = "https://opencritic.com/game/10993/deathloop"
    soup = get_soup(url_template)
    game_detail = detail_opencritic_games(soup)
    return game_detail

@app.get("/imdb_detail")
async def imdb_detail():
    url_template = "https://www.imdb.com/title/tt0120815/"
    soup = get_soup(url_template)
    movie_detail = detail_imdb_movie(soup)
    return movie_detail