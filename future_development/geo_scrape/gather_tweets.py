# -*- coding: UTF-8 -*-
# https://www.bmc.com/blogs/track-tweets-location/
import tweepy
import sys
import pickle
import os.path
from os import path
import json

consumer_key = "v7eSzVS0EKjwrDhkgY9iUYSxi"
consumer_secret = "D7KeEJYuhWj1tRUSKQc4i3beOnCBoROYHqY4GjkvPMn5O2Kh4k"
access_token = "1185579278173425667-hNI7QURnmXAh1BSyycGq21W1gqQki6"
access_token_secret = "UVnsbxz1XWyJ861MqAIKTNkOpzNkLK1zBgKLgRVRKMMbw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


name = "nyc"
y1 = 40.5722
y2 = 40.9467
x1 = -74.1687
x2 = -73.8062


def save_obj(obj):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj():
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	buckets = []
	return buckets

tweets = load_obj()


class CustomStreamListener(tweepy.StreamListener):
	global name
	def on_status(self, status):
		#score = sent.sentiment_analyzer_scores_print(status.text)
		print(1)
		json = status._json
		tweets.append(json)
		save_obj(tweets)

	def on_error(self, status_code):
		print("error code:" + strc(status_code))

	def on_timeout(self):
		print("timeout")

listener = tweepy.streaming.Stream(auth, CustomStreamListener())
listener.filter(locations=[x1,y1,x2,y2])











