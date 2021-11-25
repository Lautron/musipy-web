import requests
from bs4 import BeautifulSoup

def get_soup_obj(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")

