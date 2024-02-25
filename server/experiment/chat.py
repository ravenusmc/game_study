import requests
from bs4 import BeautifulSoup
import re
from ast import literal_eval


# url = 'https://fandom-prod.apigee.net/v1/xapi/reviews/metacritic/critic/games/alien-isolation/platform/playstation-4/web?apiKey=1MOZgmNFxvmljaQR1X9KAij9Mo4xAY3u&offset=0&limit=50&sort=score&componentType=ReviewList'
# print(requests.get(url).json())


# url = "https://www.metacritic.com/game/sea-of-stars/critic-reviews/"
url = "https://www.metacritic.com/game/sea-of-stars/user-reviews/"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

# 'publicationName'
html_text = requests.get(url, headers=headers).text
print(html_text)
# for q, s, u, d in re.findall(r'quote:"(.*?)",.*?score:(\d+).*?url:"(.*?)",.*?date:"(.*?)"', html_text):
#     print(s) #This is the score
#     print(q) # This is the quote
#     # print(t)
#     # print(literal_eval(f'"{u}"')) # Link I don't believe I need this
#     # print(d) Date - Don't need this
#     print("-" * 80)

# for q, s, u, d, t in re.findall(
#     r'quote:"(.*?)",.*?publicationName:(\t+),.*?score:(\d+).*?url:"(.*?)",.*?date:"(.*?)"', html_text):
#     print(s)
#     print(q)
#     print(t)
#     # print(literal_eval(f'"{u}"')) # Link I don't believe I need this
#     # print(d) Date - Don't need this
#     print("-" * 80)


c
