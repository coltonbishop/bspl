################################################################################################
# Converts the pickled hashmaps containing hashtag data (in pkl/) into CSV files (saved to csv/)
# 
# python3 hash2csv.py
#
# Author: Colton Bishop
# Questions contact cmbishop@princeton.edu
#################################################################################################

import sys
import pickle
import os.path
from os import path
import csv

# Function to load object
def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	buckets = {}
	return buckets

# Targeted users
hashtags = ["#BankingonClimateChange", "#InsureOurFuture", "#DefundClimateChange","#ProtectTheArctic", "#StandWithTheGwichin", "#StoptheMoneyPipeline"]
csv_ext = "csv/"
pkl_ext = "pkl/"

# For each pickled data file, creates CSV file
for h in hashtags:
	tags = load_obj(pkl_ext + h)

	with open('{}.csv'.format(csv_ext + h + "_new"), 'w', newline='') as csvfile:
		fieldnames = ['tweet_id', 'date', 'user', 'favorite_count', 'retweet_count', 'text']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")
		writer.writeheader()
		for id in tags:
			tweet = tags[id]
			text = tweet['text'].replace("\n", ":").replace(",", " ")
			# print(text)
			# input("Continue?")
			writer.writerow({'tweet_id' : tweet['tweet_id'], 'date' : tweet['date'], 'user' : tweet['user'], 'favorite_count' : tweet['favorite_count'], 'retweet_count' : tweet['retweet_count'], 'text' : text})
