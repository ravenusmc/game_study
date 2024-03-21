[['Year', 'Role-Playing', 'Adventure'],
	[1994, 93, 89]
	[1995, 88, 90]
]


average_scores = self.data.groupby(['Year_of_Release', 'Genre'])['Critic_Score'].mean().reset_index()
# Merge the original dataset with the calculated averages
merged_df = pd.merge(self.data, average_scores, on=['Year_of_Release', 'Genre'], how='left', suffixes=('', '_avg'))
# Fill NaN values with 0 (for cases where there is no average score)
merged_df['Critic_Score'] = merged_df['Critic_Score_avg'].fillna(0)
# Drop the temporary column used for averages
merged_df = merged_df.drop(columns=['Critic_Score_avg'])
print(merged_df)

    Year_of_Release         Genre  Critic_Score
0              1996  Role-Playing     94.000000
1              1997  Role-Playing     81.750000
2              1998  Role-Playing     82.428571
3              1999  Role-Playing     81.111111

    Year_of_Release      Genre  Critic_Score
0              1998  Adventure     49.000000
1              1999  Adventure     89.500000
2              2000  Adventure     67.333333
3              2001  Adventure     71.571429
4              2002  Adventure     68.500000
5              2003  Adventure     68.500000


    Year_of_Release         Genre  Critic_Score   Genre2 Critic_Score_genre2 genre3 critic_score_genre3 
0              1996  Role-Playing     94.000000             0.000000             0.000000
1              1997  Role-Playing     81.750000             0.000000             0.000000
2              1998  Role-Playing     82.428571             0.000000             0.000000


    Year_of_Release      Genre  Critic_Score  Genre_genre2  Critic_Score_genre2
0              1998  Adventure     49.000000  Role-Playing            82.428571
1              1999  Adventure     89.500000  Role-Playing            81.111111
2              2000  Adventure     67.333333  Role-Playing            76.411765
3              2001  Adventure     71.571429  Role-Playing            73.636364

            # Rename the 'Critic_Score' column to 'Critic_Score_genre1'
            #average_ratings.rename(columns={'Critic_Score': 'Critic_Score_genre1'}, inplace=True)


        score_columns = [col for col in merged_df.columns if 'Critic_Score' in col]
        while count < len(merged_df):
            data_frame_row_data = merged_df.iloc[count]
            year = int(data_frame_row_data['Year_of_Release'])
            row = [year]
            for column in score_columns:
                rating = int(data_frame_row_data[column])
                row.append(rating)
                print(row)
                input()


What I was working on: 
# def build_data_from_merged_df(self, genres, merged_df):
    #     year_and_critic_ratings = []
    #     columns = ['Year']
    #     columns.extend(genres)
    #     year_and_critic_ratings.append(columns)
    #     count = 0 
    #     while count < len(merged_df):
    #         rows = []
    #         data_frame_row_data = merged_df.iloc[count]
    #         year = int(data_frame_row_data.iloc[0])
    #         rows.append(year)
    #         if len(data_frame_row_data) ==3:
    #             rating_1 = int(data_frame_row_data.iloc[2])
    #             rows.append(rating_1)
    #         elif len(data_frame_row_data) == 5:
    #             rating_1 = int(data_frame_row_data.iloc[2])
    #             rating_2 = int(data_frame_row_data.iloc[4])
    #             rows.append(rating_1)
    #             rows.append(rating_2)
    #         elif len(data_frame_row_data) == 7:
    #             rating_1 = int(data_frame_row_data.iloc[2])
    #             rating_2 = int(data_frame_row_data.iloc[4])
    #             rating_3 = int(data_frame_row_data.iloc[6])
    #             rows.append(rating_1)
    #             rows.append(rating_2)
    #             rows.append(rating_3)
    #         year_and_critic_ratings.append(rows)
    #         count += 1
    #     print(year_and_critic_ratings)


    DATA.py back up

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
        filtered_df = self.data[(self.data['Year_of_Release'] == selected_year) & (self.data['Genre'] == genre)]
        if filtered_df.empty:
            # Handle the case where no games are found for the selected year and genre
            best_game_by_genre_and_year.append("No games found for the selected year and genre")
            best_game_by_genre_and_year.append(0)  # Assigning a default score of 0
        else:
            highest_score_index = filtered_df['Critic_Score'].idxmax()
            game_with_highest_score = filtered_df.loc[highest_score_index, 'Name']
            critic_score_of_game = int(filtered_df.loc[highest_score_index, 'Critic_Score'])
            best_game_by_genre_and_year.append(game_with_highest_score)
            best_game_by_genre_and_year.append(critic_score_of_game)
        return best_game_by_genre_and_year
    
    def get_top_five_games_by_year(self, year):
        top_five_games_and_scores_selected_year = []
        year_data = self.data[self.data['Year_of_Release'] == year]
        if year_data.empty:
            # Handle the case where no games are found for the selected year
            top_five_games_and_scores_selected_year.append(["No games found for the selected year", 0])  # Default score of 0
        else:
            top_games = year_data.sort_values(by='Critic_Score', ascending=False).head(5)
            top_five_games_and_scores_selected_year.append(['Game Title', 'Critic Score'])
            for index, game_data in top_games.iterrows():
                title = game_data['Name']
                score = int(game_data['Critic_Score'])
                top_five_games_and_scores_selected_year.append([title, score])
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
            rows.append(year)
            rows.append(rating)
            year_and_critic_ratings.append(rows)
            count += 1
        return year_and_critic_ratings
    
    def get_average_game_ratings_by_year_and_selected_genres(self, genres): 
        data_frame_list = []
        for genre in genres:
            selected_genre_df = self.data[self.data['Genre'] == genre]
            average_ratings = selected_genre_df.groupby(['Year_of_Release', 'Genre']).agg({'Critic_Score': 'mean'}).reset_index()
            data_frame_list.append(average_ratings)
        # Merge DataFrames based on the "Year_of_Release" column
        merged_df = data_frame_list[0]  # Initialize with the first DataFrame
        for i, df in enumerate(data_frame_list[1:], start=2):
            merged_df = pd.merge(merged_df, df, on=['Year_of_Release'], how='outer', suffixes=('', f'_genre{i}'))
        # Fill missing values with 0
        merged_df = merged_df.fillna(0)
        return merged_df
    
    def build_data_from_merged_df(self, genres, merged_df):
        year_and_critic_ratings = []
        columns = ['Year']
        columns.extend(genres)
        year_and_critic_ratings.append(columns)
        for index, row in merged_df.iterrows():
            current_row = [int(row['Year_of_Release'])]
            for i in range(2, len(row), 2):  # Assuming ratings columns start from index 2 and are in increments of 2
                rating = int(row.iloc[i])
                current_row.append(rating)

            year_and_critic_ratings.append(current_row)
        return year_and_critic_ratings

    def Top_sales_by_publisher_by_selected_year(self, year):
        top_publishers_by_selected_year = []
        columns = ['Publisher', 'Sales']
        top_publishers_by_selected_year.append(columns)
        selected_year_df = self.data[self.data['Year_of_Release'] == year]
        top_publishers = selected_year_df.groupby(['Publisher']).agg({'Global_Sales': 'sum'}).reset_index()
        top_publishers_sorted = top_publishers.sort_values(by='Global_Sales', ascending=False).head(5)
        count = 0
        while count < 5:
            rows = []
            sales = top_publishers_sorted.iloc[count]
            publisher = sales['Publisher']
            total_sales = int(sales['Global_Sales'])
            rows.append(publisher)
            rows.append(total_sales)
            top_publishers_by_selected_year.append(rows)
            count += 1
        return top_publishers_by_selected_year
    
    def top_sales_by_publisher_by_selected_year_and_genre(self, year, genre):
        top_publishers_by_selected_year_and_genre = []
        columns = ['Publisher', 'Sales']
        top_publishers_by_selected_year_and_genre.append(columns)
        # Filter the data by year and genre
        selected_data = self.data[(self.data['Year_of_Release'] == year) & (self.data['Genre'] == genre)]
        # Group by Publisher and sum the Global_Sales
        top_publishers = selected_data.groupby(['Publisher']).agg({'Global_Sales': 'sum'}).reset_index()
        # Sort and get the top 5 publishers
        top_publishers_sorted = top_publishers.nlargest(5, 'Global_Sales')
        # Iterate through the top publishers and add to the result list
        for _, row in top_publishers_sorted.iterrows():
            top_publishers_by_selected_year_and_genre.append([row['Publisher'], row['Global_Sales']])
        return top_publishers_by_selected_year_and_genre
    
    def get_distinct_years(self):
        unique_values = sorted(self.data['Year_of_Release'].unique())
        print(unique_values)
    
    def get_distinct_genres(self):
        unique_genres = self.data['Genre'].unique()
        print(unique_genres)

    
# test = EXAMINECSV()
# test.get_distinct_genres()

    # <!-- What graphs to make?
	# 	-Sales, by publisher, by year 
	# 		-Need to see top 5 publishers probably 
	# 		-user clicks button to change to next year
	# 		-DONE  
	# 	-Graph of user scores versus critic score for best game 
	# 		-Should I do this? -->

    best_game_by_genre_and_year[0] === 'No games found for the selected year and genre'

    Have to fix the bug on the genre graph
