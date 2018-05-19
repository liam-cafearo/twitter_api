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

# Invoke 'get_user' passing in '@madonna' as test data.
# 'get_user' then returns a User instance that is assigned
# to the user variable.
user = api.get_user('@madonna')

# The access the 'screen_name' and 'followers_count' properties
# of the user object.
print user.screen_name
print user.followers_count

# Invoke the user.friends() method to return a list of the user's
# friends and for each friend the user has, print the friend screen
# name and the number of their followers.
for friend in user.friends():
    print
    print friend.screen_name
    print friend.followers_count