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

html_text = requests.get(url, headers=headers).text

for q, s, u, d in re.findall(
    r'quote:"(.*?)",.*?score:(\d+).*?url:"(.*?)",.*?date:"(.*?)"', html_text
):
    print(s)
    print(q)
    # print(literal_eval(f'"{u}"')) # Link I don't believe I need this
    # print(d) Date - Don't need this
    print("-" * 80)

# Define the URL
# URL = 'https://www.metacritic.com/game/alien-isolation/critic-reviews/?platform=playstation-4'
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
#            'AppleWebKit/537.36 (KHTML, like Gecko) '\
#            'Chrome/75.0.3770.80 Safari/537.36'}
# Send an HTTP request to the URL
# response = requests.get(URL, headers=headers)
# Check if the request was successful (status code 200)
# if response.status_code == 200:

	# Parse the HTML content of the page using BeautifulSoup
	# soup = BeautifulSoup(response.text, 'html.parser')
	# review_blocks = soup.find_all(class_='review_body')
	# print(review_blocks)

	# Find the review score and review text elements
	# score_elements = soup.find_all(class_='metascore_w')
	# review_elements = soup.find_all(class_='review_body')

	# Iterate through the elements and print the scores and review text
	# for score, review in zip(score_elements, review_elements):
	# 		print(f'Score: {score.text.strip()}')
	# 		print(f'Review Text: {review.text.strip()}\n')
# else:
#     print(f"Failed to retrieve the web page. Status code: {response.status_code}")
