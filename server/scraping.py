import requests
from bs4 import BeautifulSoup
import re
from ast import literal_eval

class Scraping():

    def __init__(self, corrected_game_title):
        self.URL = 'https://www.metacritic.com/game/' + corrected_game_title
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
        self.CRITIC_URL = 'https://www.metacritic.com/game/' + corrected_game_title + '/critic-reviews/'
        self.USER_URL = 'https://www.metacritic.com/game/' + corrected_game_title + '/user-reviews/'
    
    def get_request(self):
        page = requests.get(self.URL, headers=self.HEADERS)
        return BeautifulSoup(page.content, "html.parser")
    
    def get_title_of_game(self):
        soup = self.get_request()
        title_elements = soup.find("div", class_="c-productHero_title")
        return title_elements.div.text.strip()
    
    def get_scores_of_game(self):
        soup = self.get_request()
        score_elements = soup.find_all("div", class_="c-siteReviewScore_background")
        scores = []
        for element in score_elements[:2]:
            scores.append(float(element.text))
        return scores 
    
    def get_critic_scores_and_data(self):
        html_text = requests.get(self.CRITIC_URL, headers=self.HEADERS).text
        count = 0
        critic_score_data = []
        columns = ['Review Number', 'Review Score']
        critic_score_data.append(columns)
        # s = score and q = text other variables, date and url link, may be used down the road
        for q, s, u, d in re.findall(r'quote:"(.*?)",.*?score:(\d+).*?url:"(.*?)",.*?date:"(.*?)"', html_text):
            rows = []
            rows.append(count)
            rows.append(s)
            critic_score_data.append(rows)
            count += 1
        return critic_score_data
    
    def get_user_scores_and_data(self):
        html_text = requests.get(self.USER_URL, headers=self.HEADERS).text
        count = 0
        user_score_data = []
        columns = ['Review Number', 'Review Score']
        user_score_data.append(columns)
        # s = score and q = text other variables, date and url link, may be used down the road
        for q, s, u, d in re.findall(r'quote:"(.*?)",.*?score:(\d+).*?url:"(.*?)",.*?date:"(.*?)"', html_text):
            rows = []
            rows.append(count)
            rows.append(s)
            user_score_data.append(rows)
            count += 1
        return user_score_data