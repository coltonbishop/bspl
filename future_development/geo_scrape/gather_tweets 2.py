# -*- coding: UTF-8 -*-
# https://www.bmc.com/blogs/track-tweets-location/
import tweepy
import sys
import sent
import pickle
import os.path
from os import path

consumer_key = "v7eSzVS0EKjwrDhkgY9iUYSxi"
consumer_secret = "D7KeEJYuhWj1tRUSKQc4i3beOnCBoROYHqY4GjkvPMn5O2Kh4k"
access_token = "1185579278173425667-hNI7QURnmXAh1BSyycGq21W1gqQki6"
access_token_secret = "UVnsbxz1XWyJ861MqAIKTNkOpzNkLK1zBgKLgRVRKMMbw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

if len(sys.argv) == 1:

	name = input("Type the name of the project for which you would like to begin collecting data.\n")

	coors = input("Type 'yes' if you want to provide specific coordinates. (Default coordinates are boxed around NYC)\n")

	if coors == 'yes':
		y1 = float(input("Longitude min?\n"))
		y2 = float(input("Longitude max?\n"))
		x1 = float(input("Latitude min?\n"))
		x2 = float(input("Latitude max?\n"))
	else:
		print("Using default NYC coordinates.")
		y1 = 40.5722
		y2 = 40.9467
		x1 = -74.1687
		x2 = -73.8062
else: 
	name = "default"
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
	buckets = {}
	return buckets

buckets = load_obj()

def update(status,score):
	loc = status.user.location
	if loc not in buckets:
		buckets[loc] = [score]
	else:
		buckets[loc].append(score)
	save_obj(buckets)

# # The search term you want to find
# query = sys.argv[1]
# # Language code (follows ISO 639-1 standards)
# language = "en"

# # Calling the user_timeline function with our parameters
# results = api.search(q=query, lang=language)

# # foreach through all tweets pulled
# for tweet in results:
# 	print("\n")
# 	# printing the text stored inside the tweet object
# 	print(tweet.text)
# 	print("\n")
# 	todo = input("Input: location, next, or user:\n")
# 	if todo == "user":
# 		print(tweet.user.screen_name)
# 	if todo == "location":
# 		if tweet.user.location:
# 			print(tweet.user.location)
# 		else:
# 			print("No location data available")
# 	input("Press enter for next tweet")

class CustomStreamListener(tweepy.StreamListener):
	global name
	def on_status(self, status):
		score = sent.sentiment_analyzer_scores_print(status.text)
		if status.user.location:
			print(status.user.location)
			update(status,score['compound'])
		if status.geo:
			print(status.geo)

	def on_error(self, status_code):
		print("error code:" + strc(status_code))

	def on_timeout(self):
		print("timeout")

listener = tweepy.streaming.Stream(auth, CustomStreamListener())
listener.filter(locations=[x1,y1,x2,y2])
