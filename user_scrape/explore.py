################################################################################################
# Script to play with, test, and explore data 
# 
# python3 explore.py
#
# Author: Colton Bishop
# Questions contact cmbishop@princeton.edu
#################################################################################################

import pickle
import os.path
from os import path
import sys
from datetime import datetime

def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	else:
		print("Cannot find {}",format(name))

def save_obj(obj, name):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# tweets = load_obj("data/tweets")

tweets = load_obj("data/sectors/big7")


for firm in tweets:
	print(len(tweets[firm]))


# for firm in tweets:
# 	ids = {}
# 	cleaned[firm] = []
# 	for tweet in tweets[firm]:
# 		if tweet["tweet_id"] not in ids:
# 			ids[tweet["tweet_id"]] = 1
# 			cleaned[firm].append(tweet)

# save_obj(cleaned, "data/cleaned")