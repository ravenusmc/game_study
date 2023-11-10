# importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob

class Sentiment():

    def get_sentiment(self, sentiment_data):
        count = 1
        print(sentiment_data[count][1])
        speech_text_ready_for_analysis = TextBlob(sentiment_data[count][1])
        sentence_sentiment = speech_text_ready_for_analysis.sentiment[0]
        print(sentence_sentiment)