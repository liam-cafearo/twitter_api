import json
import tweepy
# keep credentials in a seperate folder so it need to be imported. also the file is added to the '.gitignore' file.
import credentials
from tweepy import OAuthHandler
# import Python's Counter Class
from collections import Counter
from prettytable import PrettyTable

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


for label, data in (('Text', status_texts),
                        ('Screen Name', screen_names),
                        ('Word', words)):
        table = PrettyTable(field_names=[label, 'count'])
        counter = Counter(data)
        [ table.add_row(entry) for entry in counter.most_common()[:10] ]
        table.align[label], table.align['Count'] = 'l', 'r' # align the columns
        print table