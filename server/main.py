from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing files that I made: 
from scraping import *
from support import *
from sentiment import *

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
        # data_container.append(game_title)
        scores = scrape.get_scores_of_game()
        data_container['scores'] = scores
        # data_container.append(scores)
        # critic_score_data, critic_quote_data, stat_dict = scrape.get_critic_scores_and_data()
        # critic_language_data, critic_sentiment_average = sentiment.get_sentiment(critic_quote_data)
        # data_container.append(critic_score_data)
        # data_container.append(critic_quote_data)
        # data_container.append(stat_dict)
        # data_container.append(critic_language_data)
        # data_container.append(critic_sentiment_average)
        # user_score_data, user_quote_data = scrape.get_user_scores_and_data()
        # user_language_data, user_sentiment_average = sentiment.get_sentiment(user_quote_data)
        # data_container.append(user_score_data)
        # data_container.append(user_quote_data)
        # data_container.append(user_language_data)
        # data_container.append(user_sentiment_average)
    return jsonify(data_container)

if __name__ == '__main__':
    app.run()
