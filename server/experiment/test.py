import numpy as np
import pandas as pd
import requests
import time
import csv
from bs4 import BeautifulSoup
# import lxml
# import html5lib
# import pprint

#Getting title of game
URL = 'https://www.metacritic.com/game/alien-isolation/'
#URL = 'https://www.metacritic.com/game/sea-of-stars/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
#Searching for the title 
title_elements = soup.find("div", class_="c-productHero_title")
title = title_elements.div.text.strip()


#Getting the scores 
score_elements = soup.find_all("div", class_="c-siteReviewScore_background")
scores = []
for element in score_elements[:2]:
    scores.append(float(element.text))

#Getting the critic reviews
critic_review_elements = soup.find("a", class_="c-sectionHeader_urlLink")
url_Critic_Reviews = critic_review_elements.get("href", None)
main_url = 'https://www.metacritic.com'
full_url_critic_reviews =  main_url + url_Critic_Reviews
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}
critic_review_page = requests.get(full_url_critic_reviews, headers=headers)
critic_review_soup = BeautifulSoup(critic_review_page.content, "html.parser")
critic_review_rows = critic_review_soup.find("div", class_="c-pageProductReviews_row")
print(critic_review_rows)
# for row in critic_review_rows:
#     score = row.find("div", class_="c-siteReviewScore_background")
#     print(score)
#     input()









