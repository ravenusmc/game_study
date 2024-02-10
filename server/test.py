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