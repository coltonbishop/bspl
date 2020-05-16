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
api = tweepy.API(auth,  wait_on_rate_limit=False)
name = "network"

print("Beginning Program")
	

# network[user] = [[who_they_follow], [their_followers]]
network = {}

def save_net(obj, name="network"):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_net():
	if path.exists('network.pkl'):
		with open('network.pkl', 'rb') as f:
			return pickle.load(f)
	print("Cannot find network.pkl")

def get_followers(user):
	followers = []
	friends = []
	for user in tweepy.Cursor(api.followers, screen_name=user).items():
		print(user.screen_name)
		followers.append(user.screen_name)
	for user in tweepy.Cursor(api.friends, screen_name=user).items():
		friends.append(user.screen_name)

	network[user] = [friends, followers]

f = open('users.txt', "r")
lines = f.readlines()
f.close()
i = 1
for line in lines:
	print("{}/7".format(i))
	i += 1
	line = line.strip('\n')
	network[line] = get_followers(line)

save_net(network)