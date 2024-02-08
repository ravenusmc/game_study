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