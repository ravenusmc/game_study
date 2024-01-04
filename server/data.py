# importing supporting libraries
import numpy as np
import pandas as pd

class EXAMINECSV():

    # Setting up the data 
    def __init__(self):
        self.data = pd.read_csv('./data/Cleaned_data.csv')
    
    def get_best_single_game_by_year(self):
        pass
    
    def test(self):
        print(self.data.head())


test = EXAMINECSV()
test.test()