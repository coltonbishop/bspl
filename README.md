# Environmental Data Collection and Analysis for the Andlinger Center for Engery and the Environment

Note: If you are a new contributor, download the data and documentation from the BSPL (Behavioral Science for Policy Lab) Google Drive [here](https://drive.google.com/drive/u/0/folders/1KT3xeNJ_Ns0IOPil2io-mcsB-Fx0z33z). For access to the drive, email cmbishop@princeton.edu. 


# Overview

This repository can be used as a toolkit for the the collection and analysis of Twitter environmental data. It exposes an API that allows targeted analysis of regions, time periods, political campaigns, and groups of users or corporations. It supports semantic, geographical, and networking analyses.


# Run the Demo

In  the demo folder, see example data and code for working with and analyzing the collected Twitter data. Includes  basic examples such as “How many times does Goldman Sachs use the word "sustainability" in our data?” or “Who used the phrase "climate change" first in our data: JP Morgan or Bank of America?”). 


# The user_scrape Directory

This directory contains the code for scraping, maintenance, and analysis of the user targeted Twitter data. This data includes Tweets scraped from around 400 targeted users specified in the Social Media Search document on the BSPL Drive. Over the past few months, we have been scraping all newly published Tweets, as well as up to 3k tweets prior to the start of scraping per user. 

This directory contains the code for analyses such as i) creating bar plots per color group comparing the % of Tweets per firm that fall in each group or ii) visualizing the change in word group (color)  usage over time for each firm, measuring by # tweets that fall into each word group or by engagement, where engagement is measured by the number of favorites and retweets a firm’s colored Tweets received. For instance, how many people reacted to blackrock tweets in each color group in March 2019, April 2019, etc? These slides will be updated periodically as new data is scraped and analyzed. 

![Analysis of JP Morgan Word Grouping Engagement over Time](user_scrape/analysis/results/@jpmorgan_color_engagement.png)

# The hashtag_scrape Directory 

This directory contains the code for scraping, maintenance, and analysis of specific hashtag data. On the BSPL Drive, find the data and CSV files for Tweets over the last few weeks that contain one of the target “Stop the Money Pipeline” hashtags. 

# The future_development Directory

This directory contains messy code for in-progress projects (such as the continuous scraping and analysis of Tweets from certain geographical areas, the scraping and analysis of follower and following network data, and the scraping of Tweet replies.



