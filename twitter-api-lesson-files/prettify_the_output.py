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

# Lexical Diversity Lesson Code

# Take a list of items passed as a parameter to the 
# get_lexical_diversity function
def get_lexical_diversity(items):
        # Change the items to set to ensure all items are unique
        # get the length of the set
        # divide the set length by the length of the items list
        # multiply by 1.0 to avoide rounding off to the nearest integer
        return 1.0*len(set(items))/len(items)

# Take a list of tweets passed as a parameter to the
# get_average_words function
def get_average_words(tweets):
        # split each tweet into words
        # get the number of resulting words
        # sum each result set
        total_words = sum([ len(tweet.split()) for tweet in tweets ])
        # Divide the sum by the number of tweets to get the average
        # multiply by 1.0 to avoid rounding off to the nearest integer
        return 1.0*total_words/len(tweets)

# Invoke the functions by passing in our lists gathered earlier
print "Average words: %s" % get_average_words(status_texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)