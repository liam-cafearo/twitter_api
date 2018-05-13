import json
import tweepy
# keep credentials in a seperate folder so it need to be imported. also the file is added to the '.gitignore' file.
import credentials
from tweepy import OAuthHandler

# to access the credentials in the file we add 'credentials.' beforehand.
auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.OAUTH_TOKEN, credentials.OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
print json.dumps(results[0]._json, indent=4)

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place