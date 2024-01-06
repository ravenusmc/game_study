# importing supporting libraries
import numpy as np
import pandas as pd

class EXAMINECSV():

    # Setting up the data 
    def __init__(self):
        self.data = pd.read_csv('./data/Cleaned_data.csv')
    
    def get_best_single_game_by_year(self, selected_year):
        df = self.data[self.data['Year_of_Release'] == selected_year]
        highest_score_index = df['Critic_Score'].idxmax()
        game_with_highest_score = df.loc[highest_score_index, 'Name']
        critic_score_of_game = df.loc[highest_score_index, 'Critic_Score']
    
    def get_top_five_games_by_year(self):
        pass
    
    def test(self):
        print(self.data.head())


test = EXAMINECSV()
test.get_best_single_game_by_year(2008)