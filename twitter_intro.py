import json
import tweepy
from tweepy import OAuthHandler

# Replace these values with our own twitter app settings
CONSUMER_KEY = 'AK0Rw5s8ldBk9gmgqkX088XWD'
CONSUMER_SECRET = 'YnHl755jyuDwnDLcpHG3ps1cnggD13Xeq3ZwFtp645jjKUjlz2'
OAUTH_TOKEN = '483463582-x6m4lHVpZxYpQFjQIp15nxIC25uK6L5uIziw1cs4'
OAUTH_TOKEN_SECRET = 'bfyjnwr64SWeh4U49fH9CIZC00BgMK4Yvz5DxbhkVQOwt'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)