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
    
    def get_standard_deviation(self, score_data):
        return float("{:.2f}".format(np.std(score_data)))

    # The middle value 
    def score_median(self, score_data):
        length_of_list = len(score_data)
        score_data.sort()
        if length_of_list % 2 == 0: 
            midpoint = (length_of_list // 2) - 1
            return (score_data[midpoint] + score_data[midpoint+1]) / 2
        else:
            element_index = length_of_list // 2 
            return score_data[element_index]
    
    def interquartile_range(self, score_data):
        data = np.array(score_data)
        #calculate interquartile range 
        q3, q1 = np.percentile(data, [75,25])
        lower_qualtile = q1 
        upper_qualtile = q3
        iqr = q3 - q1
        return iqr, lower_qualtile, upper_qualtile
    
    def create_histogram(self, score_data):
        data_in_hist = {}
        data_in_hist['0-10'] = 0
        data_in_hist['11-20'] = 0
        data_in_hist['21-30'] = 0
        data_in_hist['31-40'] = 0
        data_in_hist['41-50'] = 0
        data_in_hist['51-60'] = 0
        data_in_hist['61-70'] = 0
        data_in_hist['71-80'] = 0
        data_in_hist['81-90'] = 0
        data_in_hist['91-100'] = 0
        for data in score_data:
            if data <= 10:
                count = data_in_hist['0-10']
                count += 1 
                data_in_hist['0-10'] = count
            if data >= 11 and data <= 20:
                count = data_in_hist['11-20']
                count += 1 
                data_in_hist['11-20'] = count
            if data >= 21 and data <= 30:
                count = data_in_hist['21-30']
                count += 1 
                data_in_hist['21-30'] = count
            if data >= 31 and data <= 40:
                count = data_in_hist['31-40']
                count += 1 
                data_in_hist['31-40'] = count
            if data >= 41 and data <= 50:
                count = data_in_hist['41-50']
                count += 1 
                data_in_hist['41-50'] = count
            if data >=51 and data <= 60:
                count = data_in_hist['51-60']
                count += 1 
                data_in_hist['51-60'] = count
            if data >= 61 and data <= 70:
                count = data_in_hist['61-70']
                count += 1 
                data_in_hist['61-70'] = count
            if data >= 71 and data <= 80:
                count = data_in_hist['71-80']
                count += 1 
                data_in_hist['71-80'] = count
            if data >= 81 and data <= 90:
                count = data_in_hist['81-90']
                count += 1 
                data_in_hist['81-90'] = count
            if data >= 91 and data <= 100:
                count = data_in_hist['91-100']
                count += 1 
                data_in_hist['91-100'] = count
        return data_in_hist

    def create_histogram_user(self, score_data):
        data_in_hist = {}
        data_in_hist['1'] = 0
        data_in_hist['2'] = 0
        data_in_hist['3'] = 0
        data_in_hist['4'] = 0
        data_in_hist['5'] = 0
        data_in_hist['6'] = 0
        data_in_hist['7'] = 0
        data_in_hist['8'] = 0
        data_in_hist['9'] = 0
        data_in_hist['10'] = 0
        for data in score_data:
            if data == 1:
                count = data_in_hist['1']
                count += 1 
                data_in_hist['1'] = count
            if data == 2:
                count = data_in_hist['2']
                count += 1 
                data_in_hist['2'] = count
            if data == 3:
                count = data_in_hist['3']
                count += 1 
                data_in_hist['3'] = count
            if data == 4:
                count = data_in_hist['4']
                count += 1 
                data_in_hist['4'] = count
            if data == 5:
                count = data_in_hist['5']
                count += 1 
                data_in_hist['5'] = count
            if data == 6:
                count = data_in_hist['6']
                count += 1 
                data_in_hist['6'] = count
            if data == 7:
                count = data_in_hist['7']
                count += 1 
                data_in_hist['7'] = count
            if data == 8:
                count = data_in_hist['8']
                count += 1 
                data_in_hist['8'] = count
            if data == 9:
                count = data_in_hist['9']
                count += 1 
                data_in_hist['9'] = count
            if data == 10:
                count = data_in_hist['10']
                count += 1 
                data_in_hist['10'] = count
        return data_in_hist


