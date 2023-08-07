import os

import bs4
import requests
def get_opencritic_games_list_json(url_template: str, name: str) -> list:
    querystring = {"criteria": name}
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
        "X-RapidAPI-Host": os.getenv("RAPID_API_HOST")
    }
    response = requests.get(url_template, headers=headers, params=querystring)
    return response.json()

def detail_opencritic_games(soup: bs4.BeautifulSoup) -> dict:
    current_developers = []
    current_platforms = []
    container = soup.select('app-root')[0]
    img_container = container.find(name="picture").find(name="img")
    img = {
        "src": img_container['src'],
        "alt": img_container['alt']
    }
    reviews_container = container.find(name='app-rapid-review-list').find_all(name="div", attrs={
        "class": "justify-content-between"})
    reviews = []
    for review in reviews_container:
        reviewer = review.find_all(name="div")[0].text.strip()
        reviewer_score = review.find_all(name="div")[1].text
        reviews.append({"reviewer": reviewer, "reviewer_score": reviewer_score})

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
    all_platform_data = {"developers": current_developers, "title": title, "release_date": release_date,
                         "platforms": current_platforms, "img": img, "critic_score": critic_score,
                         "critic_recommend": critic_recommend,
                         "critic_rating_img": critic_rating_img, "reviews": reviews}
    return all_platform_data