################################################################################################
# Separate Twitter data by sectors 
# 
# python3 extract_sectors.py
#
# Author: Colton Bishop
# Questions contact cmbishop@princeton.edu
#################################################################################################

import pickle
import os.path
from os import path
import sys
from datetime import datetime

# Functions to save and load objects
def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	buckets = initialize_dictionary()
	return buckets
def save_obj(obj, name):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# Loads all tweets
tweets = load_obj("data/tweets")

# Reads lines of sector_to_firm.txt into list
f = open('data/sector_to_firm.txt', "r")
lines = f.readlines()
f.close()


# Dictionary mapping sector to list of firms in that sector 
# {sector : [firms]}
sectors = {}

# Dictionary mapping sector to dictionary (which maps firms to list of all tweets for that firm)
# {sector : {firm : [tweets]}}
tweets_by_sector = {}

for firm in lines:
	firm = firm.strip("\n")
	if firm[0] != "@":
		current_sector = firm
		sectors[current_sector] = []
		tweets_by_sector[current_sector] = {}
	else:
		sectors[current_sector].append(firm)

for firm in tweets:
	for sector in sectors:
		if firm in sectors[sector]:
			tweets_by_sector[sector][firm] = tweets[firm]


for sector in tweets_by_sector:
	save_obj(tweets_by_sector[sector], "data/sectors/{}".format(sector))


