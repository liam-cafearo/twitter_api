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

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)


print common_trends