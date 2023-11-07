import requests
from bs4 import BeautifulSoup

class Scraping():

    def __init__(self, corrected_game_title):
        self.URL = 'https://www.metacritic.com/game/' + corrected_game_title
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
    
    def get_title_of_game(self):
        page = requests.get(self.URL, headers=self.HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")
        title_elements = soup.find("div", class_="c-productHero_title")
        return title_elements.div.text.strip()
