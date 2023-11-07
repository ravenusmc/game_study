from flask import Flask, jsonify, request
from flask_cors import CORS

#Importing files that I made: 
from scraping import *
from support import *

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/getGameReviews', methods=['GET', 'POST'])
def fetchGameReviews():
    if request.method == 'POST':
        support = Support()
        post_data = request.get_json()
        game_title_lowercase = support.lower_case_all_letters(post_data)
        corrected_game_title = support.add_dash_to_game_titles(game_title_lowercase)
        scrape = Scraping(corrected_game_title)
        game_title = scrape.get_title_of_game()
    return jsonify('5')

if __name__ == '__main__':
    app.run()
