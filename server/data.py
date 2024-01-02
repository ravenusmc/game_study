# importing supporting libraries
import numpy as np
import pandas as pd

class EXAMINECSV():

    def __init__(self):
        self.data = pd.read_csv('./data/Cleaned_data.csv')
    
    def test(self):
        print(self.data.head())


test = EXAMINECSV()
test.test()