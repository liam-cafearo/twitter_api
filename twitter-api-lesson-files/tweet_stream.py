# Import the Twitter API and OAUTH keys
import credentials
# The Stream class is used to connect to the Twitter stream.
from tweepy import Stream
from tweepy import OAuthHandler
# The StreamListener class is used to pull in the stream data.
# This class needs to be extended in order to use it.
# In this case I hace created a child class called 'MyStreamListener'
from tweepy.streaming import StreamListener

# Create a keyword list of strings to search with.
keyword_list = ['python', 'java', 'c#', 'ruby'] # track list

# Create a child class of StreamListener called MyStreamListener
# to pull in live data.
class MyStreamListener(StreamListener):

    # Override the 'on_data' function of StreamListener that takes
    # stream data as a parameter. See notes on what this handles.
    def on_data(self, data):
        try:
            # open file as tweet_file and append ('a') to the file.
            with open('tweet_mining.json', 'a') as tweet_file:
                # write data to file
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    # Override the StreamListener on_error funtction, see notes.
    def on_error(self, status):
        print status
        return True

auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.OAUTH_TOKEN, credentials.OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
# add filter of keyword list
twitter_stream.filter(track=keyword_list)