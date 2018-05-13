import json
import tweepy
# keep credentials in a seperate folder so it need to be imported. also the file is added to the '.gitignore' file.
import credentials
from tweepy import OAuthHandler

# to access the credentials in the file we add 'credentials.' beforehand.
auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.OAUTH_TOKEN, credentials.OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Dublin'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['scren_name']
                                for status in results
                                        for mention in status._json['entitles']['user_mentions'] ]

hashtags = [ hashtag['text']
                                for status in results
                                        for hashtag in status._json['entitles']['hashtags'] ]

words = [ words
                                for status in status_texts
                                        for word in text.split() ]


print json.dumps(status_texts[0.5], indent=1)
print json.dumps(screen_names[0.5], indent=1)
print json.dumps(hashtags[0.5], indent=1)
print json.dumps(words[0.5], indent=1)