from pydantic import BaseModel


class NameSchema(BaseModel):
    name: str


class UrlSchema(BaseModel):
    url: str
