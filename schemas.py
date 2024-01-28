from pydantic import BaseModel


class NameSchema(BaseModel):
    name: str


class UrlOpencriticSchema(BaseModel):
    url: str = "https://opencritic.com/game/10993/deathloop"


class UrlMetacriticSchema(BaseModel):
    url: str = "https://www.metacritic.com/game/xbox-one/red-dead-redemption-2"


class UrlImdbSchema(BaseModel):
    url: str = "https://www.imdb.com/title/tt0120815/"
