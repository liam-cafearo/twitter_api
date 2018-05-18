import json
import credentials
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
# we will use itemgetter as a means to sort out a list of tweet text 
# values and their associated retweet_count values, so we can display 
# them in order of popularilty
from operator import itemgetter

auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.OAUTH_TOKEN, credentials.OAUTH_TOKEN_SECRET)
# Create an instance of the Tweepy API that will do the actual data access. 
# In order for Twitter to allow the access to the API, you pass in the 
# OAuthHandler object when instantiating it.
api = tweepy.API(auth)

count = 150
query = 'Ireland'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 #the min amount of times a status is retweeted to gain entry to our list.

# anothing above our 'min_retweets' threshold gets added to pop_tweets
pop_tweets = [ status for status in results if status._json['retweet_count'] > min_retweets]

# create a list of tweet tuples associating each tweet's text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
                for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align the columns
print table