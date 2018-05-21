import json
# import 3rd party data analysis package 'Pandas'
import pandas
# we use pyplot in particular here from matplotlib for creating
# our charts, by convention pyplot is named plt when imported.
# matplotlib is a 3rd party graphics package.
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

# create a results list that will store tweets read in from
# the JSON file.
results = []
# Read in the contents of tweet_mining.json line by line and
# store it in results.
tweets_file = open(tweets_data_path, "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

# Test the code to see if the results have been populated.
print len(results)

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

# get each tweet language and the count of its appearance 
# (not to be confused with programming languages)

# You get an ordered Pandas series. A series is a one-dimensional labeled array 
# capable of holding any data type (integers, strings, floating point numbers, 
# Python objects, etc.). It is ordered by default. In this case, 
# the series holds the languages as labels and their count values 
# as entries. This series is assigned to tweets_by_lang.
tweets_by_lang = statuses['lang'].value_counts()
# get each tweet country of origin and the count of its appearance
tweets_by_country = statuses['country'].value_counts()

# create our drawing space/window (figure). This is really the drawing 
# window that you create subplots (graph/chart) on.
fig = plt.figure()
# add a plot area for our data on the figure - 1,1,1 means a single chart/graph
# create a subplot for the figure which is used to create your chart
# You can display more than one subplot on a figure, but in this case
# you will display a single bar chart
ax1 = fig.add_subplot(2,1,1)
# plot a second chart
ax2 = fig.add_subplot(2,1,2)

# style the axes and labels of our first plot
ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Tweet Languages', fontsize=15)
ax1.set_xlabel('Number of tweets', fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')
# style the title
ax1.set_title('Top 10 languages', fontsize=15, color='#666666')

# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')

# color the spines (borders) of your chart for some subtle UX.
for spine in ax1.spines.values():
    spine.set_edgecolor('#666666')

# style the axes and labels of our first plot
ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Tweet Languages', fontsize=15)
ax2.set_xlabel('Number of tweets', fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')
# style the title
ax2.set_title('Top 10 Countries', fontsize=15, color='#666666')

# plot the top 10 tweet coutries and appearance count using a bar chart
tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')

# color the spines (borders) of your chart for some subtle UX.
for spine in ax2.spines.values():
    spine.set_edgecolor('#666666')

# render the two graphs at once
plt.show()