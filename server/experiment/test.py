import numpy as np
import pandas as pd
import requests
import time
import csv
from bs4 import BeautifulSoup
# import lxml
# import html5lib
# import pprint


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
# print(title)

#Getting the scores 
score_elements = soup.find_all("div", class_="c-siteReviewScore_background")
scores = []
for element in score_elements[:2]:
    scores.append(float(element.text))
print(scores)


