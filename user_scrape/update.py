################################################################################################
# Script to update Twitter data pickle file with new Tweets published since last update
# (All recent Tweets from ~400 targeted users specified in the Social Media Search Document)
# 
# python3 update.py
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

consumer_key = "v7eSzVS0EKjwrDhkgY9iUYSxi"
consumer_secret = "D7KeEJYuhWj1tRUSKQc4i3beOnCBoROYHqY4GjkvPMn5O2Kh4k"
access_token = "1185579278173425667-hNI7QURnmXAh1BSyycGq21W1gqQki6"
access_secret = "UVnsbxz1XWyJ861MqAIKTNkOpzNkLK1zBgKLgRVRKMMbw"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
api = tweepy.API(auth,  wait_on_rate_limit=True)


def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	buckets = initialize_dictionary()
	return buckets

def save_obj(obj, name):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


tweets = load_obj("data/tweets")


def extended_from_tweet(tweet):

	try:
		text = tweet.retweeted_status.full_text
	except:
		text = tweet.full_text

	# print(tweet)
	# print(tweet)
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

	# Other valuable information: # followers/following for user, variable info (like links to images, location information on Tweet/user)
	data = {"text": text, "tweet_id": tweet_id, "hashtags": hashtags, "date": date, "user": user, "favorite_count": favorite_count, "retweet_count": retweet_count}

	return data


def pull_new(user, limit):
	print("Getting tweets from user {}".format(user))
	pull = []
	try:
		for tweet in tweepy.Cursor(api.user_timeline,id=user,tweet_mode='extended').items():
			if limit != "NA" and tweet.created_at <= limit:
				break
			pull.append(extended_from_tweet(tweet))
		return pull
	except:
		print("Private user {}".format(user))
		return []
i = 0
for user in tweets:
	i += 1
	if len(tweets[user]) == 0:
		most_recent = "NA"
	else:
		most_recent = tweets[user][0]["date"]
	pull = pull_new(user, most_recent)
	print("{} {}, length is {}".format(i, user, len(pull)))
	pull.extend(tweets[user])
	tweets[user] = pull

save_obj(tweets, "data/tweets")

