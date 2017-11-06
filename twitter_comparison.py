from twython import Twython
from nltk.sentiment.vader import (printProgressBar, SentimentIntensityAnalyzer)
from helpers import most_common
import sys
import csv

print('###########################################################')
print('')
print('')
print("TRUMP TWITTER ANALYSIS - WE READ THEM, SO YOU DON'T HAVE TO")
print("-------------- 3,788 of them to be exact -----------------")
print('')
print('')
print('###########################################################')

# Need to extend the CSV read limit
csv.field_size_limit(sys.maxsize)

# Global variables
all_trump_tweets_array = []


# Open and read through the trump csv
spamReader = csv.reader(open('3k_trump_tweets.csv',encoding='mac_roman',  newline=''), delimiter=' ', quotechar='|')
for row in spamReader:
    # For every row of the tweet create a single string variable to add to the toal variable string
    single_trump_tweet = ' '.join(row)
    all_trump_tweets_array.append(single_trump_tweet)


count = 0

# 2015 Global Values
ag_neg_2015 = 0
ag_pos_2015 = 0
ag_compound_2015 = 0

# 2016 Global Values
ag_neg_2016 = 0
ag_pos_2016 = 0
ag_compound_2016 = 0

# 2017 Global Values
ag_neg_2017 = 0
ag_pos_2017 = 0
ag_compound_2017 = 0

# For All the Trump Tweets perform a sentimanet analysis on it
for tweet in all_trump_tweets_array:
    single_score = SentimentIntensityAnalyzer().polarity_scores(tweet)
    printProgressBar(count, 3788, prefix = 'Reading Tweets:', suffix = 'THESE TWEETS ARE HUGE', length = 100)
    # The tweets are sorted by date hence we can define exact parts where the dates cut off
    if count >= 0 and count <= 1020:
        ag_neg_2015 += single_score['neg']
        ag_pos_2015 += single_score['pos']
        ag_compound_2015 += single_score['compound']
    if count >= 1021 and count <= 2040:
        ag_neg_2016 += single_score['neg']
        ag_pos_2016 += single_score['pos']
        ag_compound_2016 += single_score['compound']
    if count >= 2041:
        ag_neg_2017 += single_score['neg']
        ag_pos_2017 += single_score['pos']
        ag_compound_2017 += single_score['compound']

    count += 1

# Peform simple avg. calucatinos
ag_neg_2015 = ag_neg_2015/1020
ag_pos_2015 = ag_pos_2015/1020
ag_compound_2015 = ag_compound_2015/1020

ag_neg_2016 = ag_neg_2016/1019
ag_pos_2016 = ag_pos_2016/1019
ag_compound_2016 = ag_compound_2016/1019

ag_neg_2017 = ag_neg_2017/1741
ag_pos_2017 = ag_pos_2017/1741
ag_compound_2017 = ag_compound_2017/1741

print('')
print('')

# Print our scores
print('TRUMP SCORES 2015: ', 'Aggregate Negativity: ',ag_neg_2015,'Aggregate Positivity: ', ag_pos_2015, 'Aggregate Compound: ', ag_compound_2015)
print('TRUMP SCORES 2016: ', 'Aggregate Negativity: ',ag_neg_2016,'Aggregate Positivity: ', ag_pos_2016, 'Aggregate Compound: ', ag_compound_2017)
print('TRUMP SCORES 2017: ', 'Aggregate Negativity: ',ag_neg_2017,'Aggregate Positivity: ', ag_pos_2017, 'Aggregate Compound: ', ag_compound_2017)

