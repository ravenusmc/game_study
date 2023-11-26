# importing supporting libraries
import numpy as np
import pandas as pd

class Support():

    def lower_case_all_letters(self, post_data):
        return post_data['GameName'].lower()

    def add_dash_to_game_titles(self, game_title_lowercase):
        return "-".join(game_title_lowercase.split())
    
    def data_length(self, score_data):
        return len(score_data)

    def max_value(self, score_data):
        return max(score_data)

    def min_value(self, score_data):
        return min(score_data)

    def score_mean(self, score_data):
        return round(np.mean(score_data), 2)

    def score_mode(self, score_data):
        return max(set(score_data), key=score_data.count)

    # The middle value 
    def score_median(self, score_data):
        length_of_list = len(score_data)
        score_data.sort()
        print(score_data)
        if length_of_list % 2 == 0: 
            midpoint = (length_of_list // 2) - 1
            return (score_data[midpoint] + score_data[midpoint+1]) / 2
        else:
            element_index = N // 2 
            return score_data[element_index]
