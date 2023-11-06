import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import csv

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
soup = BeautifulSoup(critic_review_page.content, "html.parser")
critic_review_rows = soup.find_all("div", class_="c-pageProductReviews_row")
print(critic_review_rows)
# for row in critic_review_rows:
    # score = row.find(class_="c-siteReviewScore_background")
    # print(row)
    # input()

# class="c-siteReviewPlaceholder_header"

# URL = 'https://www.metacritic.com/game/alien-isolation/critic-reviews/?platform=playstation-4'
# result = requests.get(URL, headers=headers)
# doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())
# reviews = doc.find("div", class_="c-pageProductReviews_row")
# test = doc.find_all(class_="c-siteReviewHeader_publisherLogo")
# c-siteReviewHeader_publisherLogo
# print(test)
# print('jdjdjd')

# URL = 'https://www.metacritic.com/game/alien-isolation/critic-reviews/?platform=playstation-4'
# headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
# jsonData = requests.get(URL, headers=headers).json()
# print(jsonData)



#This gets me the review score at the top of the page 
# critic_scores = critic_review_soup.find_all(class_="c-siteReviewScore")
# print(critic_scores)
# for score in critic_scores:
#     print(score.get_text())
#     input()
# test = soup.find("div", class_="c-siteReviewScore_background").text
# print(test)
# critic_review_rows = critic_review_soup.find_all("div", class_="c-siteReviewScore_background")
# print(critic_review_rows)
# for r in critic_review_rows:
#     print(r)
#     input()


# critic_review_rows = critic_review_soup.find("div", class_="c-siteReview")
# print(critic_review_rows)







