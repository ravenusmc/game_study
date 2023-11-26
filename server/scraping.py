import requests
from bs4 import BeautifulSoup
import re
from ast import literal_eval

# Importing files that I created 
from support import *

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
        support = Support()
        html_text = requests.get(self.CRITIC_URL, headers=self.HEADERS).text
        count = 0
        critic_score_data = []
        critic_quote_data = []
        only_critic_score_data = []
        columns = ['Review Number', 'Review Score']
        columns_two = ['Review Number', 'Quote']
        critic_score_data.append(columns)
        critic_quote_data.append(columns_two)
        # s = score and q = text other variables, date and url link, may be used down the road
        for q, s, u, d in re.findall(r'quote:"(.*?)",.*?score:(\d+).*?url:"(.*?)",.*?date:"(.*?)"', html_text):
            rows = []
            rows_2 = []
            rows.append(count)
            rows.append(float(s))
            only_critic_score_data.append(float(s))
            rows_2.append(count)
            rows_2.append(q)
            critic_score_data.append(rows)
            critic_quote_data.append(rows_2)
            count += 1
        stat_dict = {}
        data_set_length = support.data_length(only_critic_score_data)
        stat_dict['Data_set_length'] = data_set_length
        data_set_max = support.max_value(only_critic_score_data)
        stat_dict['Data_set_Max_Value'] = data_set_max
        data_set_max = support.max_value(only_critic_score_data)
        critic_score_mean = support.score_mean(only_critic_score_data)
        stat_dict['Critic_Score_Mean'] = critic_score_mean
        critic_score_mode = support.score_mode(only_critic_score_data)
        stat_dict['Critic_Score_Mode'] = critic_score_mode
        critic_score_median = support.score_median(only_critic_score_data)
        stat_dict['Critic_Score_Median'] = critic_score_median
        return critic_score_data, critic_quote_data, stat_dict
    
    def get_user_scores_and_data(self):
        support = Support()
        html_text = requests.get(self.USER_URL, headers=self.HEADERS).text
        count = 0
        user_score_data = []
        user_quote_data = []
        only_user_score_data = []
        columns = ['Review Number', 'Review Score']
        columns_two = ['Review Number', 'Quote']
        user_score_data.append(columns)
        user_quote_data.append(columns_two)
        for q, s, u, d in re.findall(r'quote:"(.*?)",.*?score:(\d+).*?url:"(.*?)",.*?date:"(.*?)"', html_text):
            rows = []
            rows_2 = []
            rows.append(count)
            rows.append(s)
            rows_2.append(count)
            rows_2.append(q)
            only_user_score_data.append(float(s))
            user_score_data.append(rows)
            user_quote_data.append(rows_2)
            count += 1
        user_stat_dict = {}
        data_set_length = support.data_length(only_user_score_data)
        user_stat_dict['Data_set_length'] = data_set_length
        data_set_max = support.max_value(only_user_score_data)
        user_stat_dict['Data_set_Max_Value'] = data_set_max
        data_set_max = support.max_value(only_user_score_data)
        critic_score_mean = support.score_mean(only_user_score_data)
        user_stat_dict['Critic_Score_Mean'] = critic_score_mean
        critic_score_mode = support.score_mode(only_user_score_data)
        user_stat_dict['Critic_Score_Mode'] = critic_score_mode
        critic_score_median = support.score_median(only_user_score_data)
        user_stat_dict['Critic_Score_Median'] = critic_score_median
        return user_score_data, user_quote_data, user_stat_dict