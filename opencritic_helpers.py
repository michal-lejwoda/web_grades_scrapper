import os
import requests
def get_opencritic_games_list_json(url_template: str, name: str) -> list:
    querystring = {"criteria": name}
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
        "X-RapidAPI-Host": os.getenv("RAPID_API_HOST")
    }
    response = requests.get(url_template, headers=headers, params=querystring)
    return response.json()