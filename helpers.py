import requests
import bs4
def get_soup(url: str) -> bs4.BeautifulSoup:
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    r = session.get(url, allow_redirects=False)
    return bs4.BeautifulSoup(r.text, 'lxml')

def create_url(url_template: str, name: str) -> str:
    return url_template.format(name)

def create_session():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    return session