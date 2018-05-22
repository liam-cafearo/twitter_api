import json
# import pythons own regex
import re
# import 3rd party data analysis package 'Pandas'
import pandas
# we use pyplot in particular here from matplotlib for creating
# our charts, by convention pyplot is named plt when imported.
# matplotlib is a 3rd party graphics package.
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

def read_json(file_path):
    results = []
    tweets_file = open(file_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    # re.search finds a pattern anywhere in the string
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results = read_json(tweets_data_path)

# create a dataframe. A DataFrame is a 2-dimensional labeled data 
# structure with columns of potentially different types. You can 
# think of it like a spreadsheet or SQL table, or a dict of 
# Series objects. It is generally the most commonly used pandas object.
statuses = pandas.DataFrame()

# Create a column in our status’ DataFrame for text, lang, 
# and country and populate the DataFrame with these values for each 
# tweet read from the file.

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
# store the language values
statuses['lang'] = map(lambda status: status['lang'], results)
# sometimes there may not be a 'place' listed in the tweet, so set to 'N/A' if not present.
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] else "N/A", results)

# new DataFrame columns
# create columns, python, java etc, then propulate the columns with the matching data
statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['java'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
statuses['ruby'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))

# output the number of tweets where it is True (matches keywords) and that contain our keywords
print statuses['python'].value_counts()[True]
print statuses['java'].value_counts()[True]
print statuses['c#'].value_counts()[True]
print statuses['ruby'].value_counts()[True]


slices = [statuses['python'].value_counts()[True],
            statuses['java'].value_counts()[True],
            statuses['c#'].value_counts()[True],
            statuses['ruby'].value_counts()[True]]
activities = ['python', 'java', 'c#', 'ruby']
cols = ['c','m','r','b']

# first we select the 'slices', these are the relevant sizes for each part
plt.pie(slices,
        labels=activities,
        # then we specify the color list for the corresponding slices
        colors=cols,
        # The start angle '90 degrees' means the first division will
        # be a vertical line
        startangle=90,
        # we add shadow to the plot for a bit of character
        shadow= True,
        # we can use explode to pull a slice out a bit we have four 
        # total slices, so if we didn't want to pull any out we would
        # do 0,0,0,0. If we wanted to pull out the first slice we would
        # do 0.1,0,0,0
        explode=(0,0.1,0,0),
        # 'autopct' optionally overlays the percentages onto 
        # the graph itself
        autopct='%1.1f%%')

plt.title('Percentage of\ncoding languages being tweeted')
plt.show()