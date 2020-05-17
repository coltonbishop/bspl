################################################################################################
# Big 7 Analysis
# 
# python3 analyze.py
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
# create_csv(tweets, name)
# -> convert tweets to a CSV file and save it in csv/
#
################################################################################################

from lex import run_all_color_analyses, run_all_engagement_analyses, color_bars, get_tweets, filter_by_word, filter_by_color, color_analysis, color_engagement_analysis, print_all_by_color, get_all_tweets, create_csv

# Run Key Analyses


tweets = get_all_tweets()
green_filtered = filter_by_color(tweets, "green") 
green_pink = filter_by_color(tweets, "pink") 


# green = filter_by_color(citi, "green")

# print(len(green))

# score = 0
# for tweet in green:
# 	score += tweet["favorite_count"]
# 	score += tweet["retweet_count"]

# print(score)


# run_all_color_analyses()

# run_all_engagement_analyses()

# color_bars()







