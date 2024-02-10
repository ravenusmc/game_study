from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing files that I made: 
from scraping import *
from support import *
from sentiment import *
from data import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/getGameReviews', methods=['GET', 'POST'])
def fetchGameReviews():
    if request.method == 'POST':
        support = Support()
        sentiment = Sentiment()
        post_data = request.get_json()
        game_title_lowercase = support.lower_case_all_letters(post_data)
        corrected_game_title = support.add_dash_to_game_titles(game_title_lowercase)
        scrape = Scraping(corrected_game_title)
        data_container = {}
        game_title = scrape.get_title_of_game()
        data_container['game_title'] = game_title
        scores = scrape.get_scores_of_game()
        data_container['scores'] = scores
        critic_score_data, critic_quote_data, stat_dict = scrape.get_critic_scores_and_data()
        data_container['critic_score_data'] = critic_score_data
        data_container['critic_quote_data'] = critic_quote_data
        data_container['stat_dict'] = stat_dict
        critic_language_data, critic_sentiment_average = sentiment.get_sentiment(critic_quote_data)
        data_container['critic_language_data'] = critic_language_data
        data_container['critic_sentiment_average'] = critic_sentiment_average
        user_score_data, user_quote_data, user_stat_dict = scrape.get_user_scores_and_data()
        data_container['user_score_data'] = user_score_data
        data_container['user_quote_data'] = user_quote_data
        data_container['user_stat_dict'] = user_stat_dict
        user_language_data, user_sentiment_average = sentiment.get_sentiment(user_quote_data)
        data_container['user_language_data'] = user_language_data
        data_container['user_sentiment_average'] = user_sentiment_average
    return jsonify(data_container)

@app.route('/buildCSVCharts', methods=['GET', 'POST'])
def buildCSVCharts():
    if request.method == 'POST':
        requested_data_container = {}
        data = EXAMINECSV()
        post_data = request.get_json()
        year = post_data['year']
        genre = post_data['genre']
        game_with_highest_score, critic_score_of_game = data.get_best_single_game_by_year(year)
        requested_data_container['best_single_game'] = game_with_highest_score
        requested_data_container['best_game_score'] = critic_score_of_game
        requested_data_container['best_game_by_genre_and_year'] = data.get_best_single_game_by_year_and_genre(year, genre)
        requested_data_container['top_five_games_and_scores_selected_year'] = data.get_top_five_games_by_year(year)
        requested_data_container['year_and_critic_ratings'] = data.get_average_game_ratings_by_genre_and_year(genre)
        requested_data_container['top_publishers_by_selected_year'] = data.Top_sales_by_publisher_by_selected_year(year)
    return jsonify(requested_data_container)

@app.route('/buildGenreGraph', methods=['GET', 'POST'])
def buildGenreGraph():
    if request.method == 'POST':
        requested_data_container = {}
        data = EXAMINECSV()
        post_data = request.get_json()
        genres = post_data['selectedGenres']
        merged_df = data.get_average_game_ratings_by_year_and_selected_genres(genres)
        year_and_critic_ratings = data.build_data_from_merged_df(genres, merged_df)
    return jsonify(year_and_critic_ratings)

if __name__ == '__main__':
    app.run()
