################################################################################################
# Big 7 Analysis
# 
# import lex
# 
# Author: Colton Bishop
# Questions contact cmbishop@princeton.edu
#
# The file lex.py contains functions for analyzing Twitter data from the Big 7 banks. 
#
# Big 7 Bank names: 
# @blackrock, @jpmorgan, @wellsfargo, @citibank, @bankofamerica, @goldmansachs, @morganstanley
#
# Color names (see Social Media Document for Keywords Associated with Colors):
# green, blue, red, orange, teal, pink, violet
#
#######################
# API Functionalities #
#######################
#
# get_tweets(name_of_firm) 
# -> returns list of all tweets for specfied firm 
#    EX: all_blackrock_tweets = get_tweets("@blackrock") 
#
# filter_by_word(tweets, word) 
# -> returns list of all tweets in 'tweets' that contain word
# 	 EX: all_blackrock_tweets_that_contain_word_climate = filter_by_word(blackrock, "climate")
#
# filter_by_color(tweets, color_name) 
# -> returns list of all tweets in 'tweets' of color color_name
# 	 EX: all_green_blackrock_tweets = filter_by_color(blackrock, "green")
#
# all_by_color(color_name)
# -> Returns all tweets (from all big 7 firms) of color color_name
#    EX: all_green_tweets = all_by_color("green")
#
# color_analysis(firm_name)
# -> Plots change in word usage over time for a firm, measuring by # tweets that fall into each word group
#
# color_engagement_analysis(firm_name):
# -> Plots change in word usage over time for a firm
# 	 Engagement Score: Favorite Count + Retweet Counts of all Tweets in color group
# 	 i.e. how many people reacted to blackrock tweets in each color group in March 2019, April 2019, etc?
#
# run_all_color_analyses()
# -> run color_analysis for all big 7 firms
#
# run_all_engagement_analyses()
# -> run color_engagement_analysis for all big 7 firms
#
# color_bars()
# -> Creates one plot per color group comparing the % of Tweets per firm that fall into color group
#
# 
################################################################################################

import pickle 
import sys
import os.path
from os import path
import matplotlib.pyplot as plt
import numpy as np
import csv

# Ensure pkl data file is in the same directory as the
# script you are using to access it.
# Include the following load function in your script.

def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	print("Cannot find file {}".format(name + '.pkl'))
	return None

data_path = "../data/"

# Loads the pkl file for big 7
tweets = load_obj("../data/sectors/big7")

# Key words

green = ["climate", "environment", "sustainability", "sustainable", "global warming", "anthropocene", "biodiversity"]

blue = ["emissions", "fossil fuel", "divestment", "oil", "coal", "natural gas", "greenhouse gas", ["arctic", "drilling"], ["arctic", "exploration"], "drilling", "extraction", ["energy","emissions"], ["energy","environment"], ["energy","fossil fuel"], ["energy","sustainability"], ["energy","divestment"], "carbon"]

red = [["risk","climate change"], ["risk","environment"], ["risk","sustainability"], ["opportunity","climate change"], ["opportunity","environment"], ["opportunity","sustainability"], ["cost","climate change"], ["cost","environment"], ["cost","sustainability"], ["benefit","climate change"], ["benefit","environment"], ["benefit","sustainability"], "responsible", "responsibility", "esg", "green bonds", ["future", "responsibility"], ["future", "well-being"], ["future", "generations"], ["future", "responsible"], ["future", "sustainability"]]

orange = ["regulation", ["transparency","environment"], ["transparency","investment"], ["transparency","climate change"], ["transparency","emissions"], ["transparency","pollution"], ["accountability","emissions"], ["accountability","environment"], ["accountability","investment"], ["accountability","climate change"], ["accountability","pollution"], "carbon disclosure", "carbon risk disclosure", "tcfd"]

teal = [["solar", "power"], ["solar", "energy"], ["solar","resources"], ["solar","technology"], ["solar","plants"], "renewables", ["wind", "power"], ["wind", "energy"], ["wind", "resources"], ["wind", "technology"], ["wind", "turbines"], ["wind", "farms"], "green technologies", ["green", "investing"], ["green", "investment"], "adaptation", "mitigation"]

pink = ["covid", "corona", "pandemic", "epidemic", "COV-2", "outbreak", "social distanc", "ventilator", "face mask", "care act"]

violet = [["cov", "climate"], ["corona", "climate"], ["pandemic", "climate"], ["epidemic", "climate"]]

# Big 7 Tweets

br = tweets["@blackrock"]
jp = tweets["@jpmorgan"]
wells = tweets["@wellsfargo"]
citi = tweets["@citibank"]
boa = tweets["@bankofamerica"]
gs = tweets["@goldmansachs"]
ms = tweets["@morganstanley"]

all_firms = [br, jp, wells, citi, boa, gs, ms]
all_firm_names = ["@blackrock", "@jpmorgan", "@wellsfargo", "@citibank", "@bankofamerica", "@goldmansachs", "@morganstanley"]

name_to_tweets = {"@blackrock": br, "@jpmorgan": jp, "@wellsfargo" : wells, "@citibank" : citi, "@bankofamerica" : boa, "@goldmansachs" : gs, "@morganstanley" : ms}

name_to_color = {"green" : green, "blue" : blue, "red" : red, "orange" : orange, "teal" : teal, "pink" : pink, "violet" : violet}


# Returns 1 if sentence contains color word, 0 otherwise
# Can be changed to return count of color words in sentence
def count(sentence, color):
	text = sentence.lower()
	count = 0
	for word in color:
		if isinstance(word, str):
			if word in text:
				count += 1
		elif isinstance(word, list):
			if word[0] in text and word[1] in text:
				count += 1
	if count > 0:
		return 1
	return 0

def engagement_count(sentence, color, score):
	text = sentence.lower()
	count = 0
	for word in color:
		if isinstance(word, str):
			if word in text:
				return score
		elif isinstance(word, list):
			if word[0] in text and word[1] in text:
				return score
	return 0


# Returns count that a tweet received for each color
def all_counts(text):
	g = count(text, green)
	b = count(text, blue)
	r = count(text, red)
	o = count(text, orange)
	t = count(text, teal)
	p = count(text, pink)
	v = count(text, violet)
	return g, b, r, o, t, p, v

# Assigns 'score' to each color group if text contains word from that group
def all_engagement_counts(text, score):
	g = engagement_count(text, green, score)
	b = engagement_count(text, blue, score)
	r = engagement_count(text, red, score)
	o = engagement_count(text, orange, score)
	t = engagement_count(text, teal, score)
	p = engagement_count(text, pink, score)
	v = engagement_count(text, violet, score)
	return g, b, r, o, t, p, v

# Converts tweet to timestamp: 03/20
def stamp(tweet):
	return "{}/{}".format(tweet["date"].month, tweet["date"].year)

# Plots line graph
def plot(y, g, b, r, o, t, p, v, title, filename, y_label='Month'):

	x_label='Month'
	plt.figure(figsize=(17,9))
	plt.plot(y, g, color='g')
	plt.plot(y, b, color='b')
	plt.plot(y, r, color='r')
	plt.plot(y, o, color='orange')
	plt.plot(y, t, color='cyan')
	plt.plot(y, p, color='pink')
	plt.plot(y, v, color='purple')
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	ax = plt.gca()
	n = 3  # Keeps every 7th label
	[l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]
	# plt.show()
	plt.savefig('results/{}.png'.format(filename))


# Analysis A:
# Line plot for each firm showing how # hits (or % of tweets) for each of the color groups 
# Time bins: days, months, years?

def initialize_variables(firm):
	# Create Variables
	start = [firm[-1]["date"].month, firm[-1]["date"].year]
	end = [firm[0]["date"].month, firm[0]["date"].year]

	y, g, b, r, o, t, p, v = [], [], [], [], [], [], [], []
	bins = {}
	i = 0
	done = True
	# Initialize
	while done:
		done = (start[0] != end[0]) or (start[1] != end[1])
		s = "{}/{}".format(start[0], start[1])
		bins[s] = i
		y.append(s)
		i += 1
		g.append(0)
		b.append(0)
		r.append(0)
		o.append(0)
		t.append(0)
		p.append(0)
		v.append(0)
		if start[0] == 12:
			start[0] = 1
			start[1] += 1
		else:
			start[0] += 1

	return start, end, y, g, b, r, o, t, p, v, bins

# Plots change in word usage over time for a firm, measuring by # tweets that fall into each word group
def color_analysis(firm_name):

	firm = name_to_tweets[firm_name]
	title = 'Change in Word Usage Over Time (by Tweet Count) for {}'.format(firm_name)
	start, end, y, g, b, r, o, t, p, v, bins = initialize_variables(firm)
		
	# Track key word hits per month
	for tweet in firm:
	 	timestamp = stamp(tweet)
	 	index = bins[timestamp]
	 	counts = all_counts(tweet["text"])
	 	g[index] += counts[0]
	 	b[index] += counts[1]
	 	r[index] += counts[2]
	 	o[index] += counts[3]
	 	t[index] += counts[4]
	 	p[index] += counts[5]
	 	v[index] += counts[6]

	filename = "{}_color".format(firm_name)
	plot(y, g, b, r, o, t, p, v, title, filename=filename, y_label='Count of Tweets that Fall into Each Color Category')


# Plots change in word usage over time for a firm, measuring by engagement score (favorite + retweet counts) for each word group
# (How many people reacted to tweets in the green group in March, April, etc)
def color_engagement_analysis(firm_name):
	firm = name_to_tweets[firm_name]
	start, end, y, g, b, r, o, t, p, v, bins = initialize_variables(firm)
	title = 'Change in Word Usage Over Time (by Engagement) for {}'.format(firm_name)
	for tweet in firm:
		 	timestamp = stamp(tweet)
		 	index = bins[timestamp]
		 	counts = all_engagement_counts(tweet["text"], tweet["favorite_count"] + tweet["retweet_count"])
		 	g[index] += counts[0]
		 	b[index] += counts[1]
		 	r[index] += counts[2]
		 	o[index] += counts[3]
		 	t[index] += counts[4]
		 	p[index] += counts[5]
		 	v[index] += counts[6]

	filename = "{}_color_engagement".format(firm_name)
	plot(y, g, b, r, o, t, p, v, title, filename=filename, y_label='Engagement Score (Favorite + Retweet Count) for Each Color Category')


# Returns the percentage full Tweet count of all colors for a firm
def percent_count(tweets):
	g, b, r, o, t, p, v = 0, 0, 0, 0, 0, 0, 0
	total = len(tweets)
	for tweet in tweets:
		g1, b1, r1, o1, t1, p1, v1 = all_counts(tweet["text"])
		g += g1
		b += b1
		r += r1
		o += o1
		t += t1 
		p += p1
		v += v1

	return g/total, b/total, r/total, o/total, t/total, p/total, v/total


def plot_bar(title, y, x, y_label, filename):
	y_pos = np.arange(len(y))
	plt.figure(figsize=(17,9))
	plt.bar(y_pos, x, align='center', alpha=0.5)
	plt.xticks(y_pos, y)
	plt.ylabel(y_label)
	plt.title(title)
	plt.savefig('results/{}.png'.format(filename))
	# plt.show()

# Creates one plot per word group comparing the % of Tweets per firm that fall into word group
def color_bars():

	br_counts = percent_count(br)
	jp_counts = percent_count(jp)
	wells_counts = percent_count(wells)
	citi_counts = percent_count(citi)
	boa_counts = percent_count(boa)
	gs_counts = percent_count(gs)
	ms_counts = percent_count(ms)

	y_green = [br_counts[0], jp_counts[0], wells_counts[0], citi_counts[0], boa_counts[0], gs_counts[0], ms_counts[0]]
	y_blue = [br_counts[1], jp_counts[1], wells_counts[1], citi_counts[1], boa_counts[1], gs_counts[1], ms_counts[1]]
	y_red = [br_counts[2], jp_counts[2], wells_counts[2], citi_counts[2], boa_counts[2], gs_counts[2], ms_counts[2]]
	y_orange = [br_counts[3], jp_counts[3], wells_counts[3], citi_counts[3], boa_counts[3], gs_counts[3], ms_counts[3]]
	y_teal = [br_counts[4], jp_counts[4], wells_counts[4], citi_counts[4], boa_counts[4], gs_counts[4], ms_counts[4]]
	y_pink = [br_counts[5], jp_counts[5], wells_counts[5], citi_counts[5], boa_counts[5], gs_counts[5], ms_counts[5]]
	y_violet = [br_counts[6], jp_counts[6], wells_counts[6], citi_counts[6], boa_counts[6], gs_counts[6], ms_counts[6]]

	title = "Usage of {} Words per Firm"
	y_label = "Percentage of Tweets"
	x_names = ["BlackRock", "JPMorgan", "WellsFargo", "CitiBank", "Bank of America", "GoldmanSachs", "MorganStanley"]

	plot_bar(title.format("Green"), x_names, y_green, y_label, filename="green")
	plot_bar(title.format("Blue"), x_names, y_blue, y_label, filename="blue")
	plot_bar(title.format("Red"), x_names, y_red, y_label, filename="red")
	plot_bar(title.format("Orange"), x_names, y_orange, y_label, filename="orange")
	plot_bar(title.format("Teal"), x_names, y_teal, y_label, filename="teal")
	plot_bar(title.format("Pink"), x_names, y_pink, y_label, filename="pink")
	plot_bar(title.format("Violet"), x_names, y_violet, y_label, filename="violet")

# Returns [(Month, Year, Text)] for all tweets that contain word
def print_firm_by_word(tweets, word):
	filtered_tweets = []
	for tweet in tweets:
		timestamp = stamp(tweet)
		sentence = tweet["text"]
		user = tweet["user"]
		text = sentence.lower()
		if word in text:
			print(user)
			print(timestamp)
			print(text)
			print("\n")
	return filtered_tweets

def print_all_by_word(word):
	for bank in all_firms:
		print_firm_by_word(bank, word)


# Prints Author, Date, and Body of All COLOR Tweets
def print_all_by_color(color_name):
	color = name_to_color[color_name]
	for firm in all_firms:
		for tweet in firm:
			timestamp = stamp(tweet)
			sentence = tweet["text"]
			user = tweet["user"]
			text = sentence.lower()
			if count(text, color) == 1:
				print(user)
				print(timestamp)
				print(text)

# Returns all tweets of color color_name
def all_by_color(color_name):
	color = name_to_color[color_name]
	filtered = []
	for firm in all_firms:
		for tweet in firm:
			text = tweet["text"].lower()
			if count(text, color) == 1:
				filtered.append(tweet)
	return filtered

# Plots change in word usage over time for a firm, measuring by # tweets that fall into each word group
def run_all_color_analyses():
	for firm_name in all_firm_names:
		color_analysis(firm_name)

# Plots change in word usage over time for a firm, measuring by engagement score (favorite + retweet counts) for each word group
# (How many people reacted to tweets in the green group in March, April, etc)
def run_all_engagement_analyses():
	for firm_name in all_firm_names:
		color_engagement_analysis(firm_name)

# Get tweets of a firm by name
def get_tweets(name_of_firm):
	return name_to_tweets[name_of_firm]

# Get tweets of a firm by name
def get_all_tweets():
	total = []
	for firm in tweets:
		total.extend(tweets[firm])
	return total

def filter_by_word(firm_tweets, word):
	filtered = []
	for tweet in firm_tweets:
		text = tweet["text"]
		text = text.lower()
		word = word.lower()
		if word in text:
			filtered.append(tweet)
	return filtered

def filter_by_color(firm_tweets, color_name):
	filtered = []
	color = name_to_color[color_name]
	for tweet in firm_tweets:
		text = tweet["text"].lower()
		if count(text, color) == 1:
			filtered.append(tweet)
	return filtered

# Creates CSV given Tweet dictionary and name
def create_csv(tweets, name):

	csv_ext = "csv/"

	with open('{}.csv'.format(csv_ext + name), 'w', newline='') as csvfile:
		fieldnames = ['tweet_id', 'date', 'user', 'favorite_count', 'retweet_count', 'text']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")
		writer.writeheader()
		for tweet in tweets:
			text = tweet['text'].replace("\n", ":").replace(",", " ")
			# print(text)
			# input("Continue?")
			writer.writerow({'tweet_id' : tweet['tweet_id'], 'date' : tweet['date'], 'user' : tweet['user'], 'favorite_count' : tweet['favorite_count'], 'retweet_count' : tweet['retweet_count'], 'text' : text})


