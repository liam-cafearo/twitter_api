import tweepy
import credentials
from tweepy import OAuthHandler

# Create an instance of Tweepy’s  OAuthHandler class by passing in 
# the CONSUMER_KEY and CONSUMER_SECRET values, and assign the 
# instance to the auth variable.
auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
# Invoke the set_access_token function passing in the OAUTH_TOKEN 
# and OAUTH_TOKEN_SECRET values as arguments. The OAuthHandler object 
# now has everything it needs to connect and authenticate with the new 
# Twitter application you just created on the Twitter developers site.
auth.set_access_token(credentials.OAUTH_TOKEN, credentials.OAUTH_TOKEN_SECRET)

# Create an instance of the Tweepy API that will do the actual data 
# access. In order for Twitter to allow the access to the API, you 
# pass in the OAuthHandler object when instantiating it.
api = tweepy.API(auth)

# We can easily harvest tweets that appear on a user’s timeline by 
# invoking the api.home_timeline method.
for status in tweepy.Cursor(api.home_timeline).items(10):
    # process a tweet
    print status.text