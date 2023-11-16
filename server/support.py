# importing supporting libraries
import numpy as np
import pandas as pd

class Support():

    def lower_case_all_letters(self, post_data):
        return post_data['GameName'].lower()

    def add_dash_to_game_titles(self, game_title_lowercase):
        return "-".join(game_title_lowercase.split())
    
    def score_average(self, score_data):
        pass
