# importing supporting libraries
import numpy as np
import pandas as pd

class EXAMINECSV():

    def __init__(self):
        self.data = pd.read_csv('./data/Cleaned_data.csv')
    
    def get_best_single_game_by_year(self, selected_year):
        df = self.data[self.data['Year_of_Release'] == selected_year]
        highest_score_index = df['Critic_Score'].idxmax()
        game_with_highest_score = df.loc[highest_score_index, 'Name']
        critic_score_of_game = int(df.loc[highest_score_index, 'Critic_Score'])
        return game_with_highest_score, critic_score_of_game
    
    def get_best_single_game_by_year_and_genre(self, selected_year, genre):
        best_game_by_genre_and_year = []
        filtered_df = self.data[(self.data['Year_of_Release'] == selected_year) & (self.data['Genre'] ==genre)]
        highest_score_index = filtered_df['Critic_Score'].idxmax()
        game_with_highest_score = filtered_df.loc[highest_score_index, 'Name']
        critic_score_of_game = int(filtered_df.loc[highest_score_index, 'Critic_Score'])
        best_game_by_genre_and_year.append(game_with_highest_score)
        best_game_by_genre_and_year.append(critic_score_of_game)
        return best_game_by_genre_and_year
 
    def get_top_five_games_by_year(self, year):
        year_data = self.data[self.data['Year_of_Release'] == year]
        top_games = year_data.sort_values(by='Critic_Score', ascending=False).head(5)
        top_five_games_and_scores_selected_year = []
        columns = ['Game Title', 'Critic Score']
        top_five_games_and_scores_selected_year.append(columns)
        count = 0 
        while count < 5: 
            rows = []
            game_data = top_games.iloc[count]
            title = game_data.iloc[0]
            score = int(game_data.iloc[9])
            rows.append(title)
            rows.append(score)
            top_five_games_and_scores_selected_year.append(rows)
            count += 1 
        return top_five_games_and_scores_selected_year

    def get_average_game_ratings_by_genre_and_year(self, genre): 
        selected_genre_df = self.data[self.data['Genre'] == genre]
        average_ratings = selected_genre_df.groupby(['Year_of_Release', 'Genre']).agg({'Critic_Score': 'mean'}).reset_index()
        year_and_critic_ratings = []
        columns = ['Year', 'Critic Rating']
        year_and_critic_ratings.append(columns)
        count = 0 
        while count < len(average_ratings): 
            rows = []
            ratings = average_ratings.iloc[count]
            year = int(ratings.iloc[0])
            rating = int(ratings.iloc[2])
            print(rating)
            rows.append(year)
            rows.append(rating)
            year_and_critic_ratings.append(rows)
            count += 1
        return year_and_critic_ratings

    def Top_sales_by_publisher_by_selected_year(self, year):
        selected_year_df = self.data[self.data['Year_of_Release'] == year]
        top_publishers = selected_year_df.groupby(['Publisher']).agg({'Global_Sales': 'sum'}).reset_index()
        top_publishers_sorted = top_publishers.sort_values(by='Global_Sales', ascending=False).head(5)
        return top_publishers_sorted
    
    def get_distinct_years(self):
        unique_values = sorted(self.data['Year_of_Release'].unique())
        print(unique_values)
    
    def get_distinct_genres(self):
        unique_genres = self.data['Genre'].unique()
        print(unique_genres)

    
test = EXAMINECSV()
test.get_distinct_genres()