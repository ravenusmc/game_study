# This file is to test out ideas for this project. 

from MetaCriticScraper import MetaCriticScraper

urlForHorizonZeroDawn = 'https://www.metacritic.com/game/alien-isolation/'
scraper = MetaCriticScraper(urlForHorizonZeroDawn)
print("Title: " + scraper.game['title'])