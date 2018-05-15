import json
import tweepy
# keep credentials in a seperate folder so it need to be imported. also the file is added to the '.gitignore' file.
import credentials
from tweepy import OAuthHandler
# import Python's Counter Class
from collections import Counter

# to access the credentials in the file we add 'credentials.' beforehand.
auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.OAUTH_TOKEN, credentials.OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Dublin'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
                for status in results
                for hashtag in status._json['entities']['hashtags'] ]

words = [ w for t in status_texts
        for w in t.split()]


for entry in [screen_names, hashtags, words]:
        counter = Counter(entry)
        print counter.most_common()[:10] # the top 10 results
        print