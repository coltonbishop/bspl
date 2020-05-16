################################################################################################
# DEMO for Accessing BSPL Twitter Data
#
# python3 demo.py
#
# Author: Colton Bishop
# Questions contact cmbishop@princeton.edu
#################################################################################################
#
# big7.pkl is a chunk of the full BSPL Twitter data
# Download the full dataset (with the tweets from all ~400 users) from the BSPL Google Drive
# 
# 
# The structure of the dictionary stored in big7.pkl is as follows:
# big7_tweets = {firm : [all_firm_tweets]}
# ex: all_MS_tweets = tweets["@MorganStanley"]
#     first_MS_tweet = all_MS_tweets[0]

# The structure of each Tweet obejct is represented as follows
# first_MS_tweet = {"text": text, "tweet_id": tweet_id, "hashtags": hashtags, "date": date, "user": user, "favorite_count": favorite_count, "retweet_count": retweet_count}
# ex:   first_MS_tweet_text = first_MS_tweet["text"]
#		first_MS_tweet_author = first_MS_tweet["user"]
#
# The structure of the big7.pkl tweets dictionary is as follows:
# all_tweets = {firm : [tweets]}
# ex: all_MS_tweets = tweets["@MorganStanley"]
# 	  first_MS_tweet = all_MS_tweets[0]
#     first_MS_tweet_text = first_MS_tweet.text
#
# Big 7 Bank names: 
# @blackrock, @jpmorgan, @wellsfargo, @citibank, @bankofamerica, @goldmansachs, @morganstanley
# 
############################################################################################################
############################################################################################################

# library for saving and loading Python objects
import pickle
import sys
import os.path
from os import path

# Ensure pkl data file is in the same directory as the
# script you are using to access it.
# Include the following load function in your script.

def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	print("Cannot find file {}".format(name + '.pkl'))
	return None

# Loads the pkl file specified in the commandline
big7_tweets = load_obj("big7")

# Example 1: How many times does Goldman Sachs use the word "sustainability" in our data?
count = 0
for tweet in big7_tweets["@goldmansachs"]:
	if "sustainability" in tweet["text"].lower():
		count += 1
print("{}/{} tweets have the word sustainability!".format(count, len(big7_tweets["@goldmansachs"])))

# Example 2: Who used the phrase "climate change" first in our data: JP Morgan or Bank of America?
import datetime

best_jp_date = datetime.datetime.now()
for tweet in big7_tweets["@jpmorgan"]:
	if "climate change" in tweet["text"].lower() and tweet["date"] < best_jp_date:
		best_jp_date = tweet["date"]

best_boa_date = datetime.datetime.now()
for tweet in big7_tweets["@bankofamerica"]:
	if "climate change" in tweet["text"].lower() and tweet["date"] < best_boa_date:
		best_jp_date = tweet["date"]

if best_boa_date < best_jp_date:
	print("Bank of America was first!")
if best_boa_date > best_jp_date:
	print("JP Morgan was first!")














