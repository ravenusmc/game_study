# importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob

class Sentiment():

    def get_average(self, sentence_sentiment_list):
        return sum(sentence_sentiment_list) / len(sentence_sentiment_list)

    def get_sentiment(self, sentiment_data):
        language_data = []
        columns = ['count', 'Sentiment']
        language_data.append(columns)
        count = 1
        sentence_sentiment_list = [] 
        while count < len(sentiment_data):
            rows = []
            text_ready_for_analysis = TextBlob(sentiment_data[count][1])
            sentence_sentiment = text_ready_for_analysis.sentiment[0]
            sentence_sentiment_list.append(sentence_sentiment)
            rows.append(count)
            rows.append(sentence_sentiment)
            language_data.append(rows)
            count += 1
        sentiment_average = self.get_average(sentence_sentiment_list)
        return language_data, sentiment_average