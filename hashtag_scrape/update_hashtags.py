################################################################################################
# Script to update Twitter data pickle file with new Tweets published since last update
# (All recent Tweets that contain one of the targeted hashtags- see Social Media Search Document)
#
# python3 update_hashtags.py
#
# Author: Colton Bishop
# Questions contact cmbishop@princeton.edu
#################################################################################################

import tweepy
from tweepy import OAuthHandler
import sys
import pickle
import os.path
from os import path
import csv

####input your credentials here
consumer_key = "v7eSzVS0EKjwrDhkgY9iUYSxi"
consumer_secret = "D7KeEJYuhWj1tRUSKQc4i3beOnCBoROYHqY4GjkvPMn5O2Kh4k"
access_token = "1185579278173425667-hNI7QURnmXAh1BSyycGq21W1gqQki6"
access_secret = "UVnsbxz1XWyJ861MqAIKTNkOpzNkLK1zBgKLgRVRKMMbw"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
api = tweepy.API(auth,  wait_on_rate_limit=True)


# Functions to save and load tweets
def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	buckets = {}
	return buckets

def save_obj(obj, name):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# Users whose hashtags we are scraping
targets = ["#BankingonClimateChange", "#InsureOurFuture", "#DefundClimateChange","#ProtectTheArctic", "#StandWithTheGwichin", "#StoptheMoneyPipeline"]
extension = "pkl/"

k = 0

# For each user in our target set
for target in targets:

	# Load the dictionary that contains their tweets
	tweets = load_obj(extension + target)
	old_length = len(tweets)

	print("{}/6 TARGETS HIT".format(k), flush=True)
	k += 1
	i = 0

	# Pull tweets from the past two weeks that contain this hashtag
	for tweet in tweepy.Cursor(api.search,q=target,
							   lang="en",
							   since="2017-04-03", tweet_mode='extended').items():

		# Once we reach a tweet we've already scraped, break and move on to next target.
		if tweet.id in tweets:
			break
		i += 1

		# Extract and format relevant information; add it to dictionary
		try:
			text = tweet.retweeted_status.full_text
		except:
			text = tweet.full_text

		hashtags = []
		try:
			for hashtag in tweet.retweeted_status.entities["hashtags"]:
				hashtags.append(hashtag["text"])
		except:
			for hashtag in tweet.entities["hashtags"]:
				hashtags.append(hashtag["text"])

		date = tweet.created_at
		tweet_id = tweet.id
		user = tweet.user.screen_name
		favorite_count = tweet.favorite_count
		retweet_count = tweet.retweet_count

		data = {"text": text, "tweet_id": tweet_id, "hashtags": hashtags, "date": date, "user": user, "favorite_count": favorite_count, "retweet_count": retweet_count}
		tweets[tweet_id] = data

	# Save updated data for user 
	print("{} new tweets for {}!".format(i, target))
	save_obj(tweets, extension + target)



