######################################################
######################################################
# Script to Visualize Big Seven Twitter Data
#
# python3 visualize.py
#
# Author: Colton Bishop
# Questions contact cmbishop@princeton.edu
######################################################
######################################################

import numpy as np
import matplotlib.pyplot as plt

# l = [name, ours_count, total_count, follwers]

# Big Seven
blackrock = ["BlackRock", 3239, 14489, 394578]
JPMorgan = ["JP Morgan", 3241, 7125, 497473]
WellsFargo = ["Wells Fargo", 3202, 18863, 313933]
Citibank = ["CitiBank", 3231, 12584, 397087]
BankofAmerica = ["Bank of America", 3217, 9527, 540846]
GoldmanSachs = ["Goldman Sachs", 3220, 12291, 764462]
MorganStanley = ["Morgan Stanley", 3198, 9053, 543594]

big7 = [blackrock, JPMorgan, WellsFargo, Citibank, BankofAmerica, GoldmanSachs, MorganStanley]

# Tech Firms
Apple = ["Apple", 0, 0, 4052966]
Samsung = ["Samsung", 3235, 3757, 474561]
Microsoft = ["Microsoft", 3248, 16819, 8826500]
Google = ["Google", 3200, 106497, 21833629]
intel = ["Intel", 0, 15049, 4825899]
IBM = ["IBM", 3222, 14151, 569001]
Facebook = ["Facebook", 0, 13685, 13474118]
HonHaiPrecision = ["HonHai", 0, 0,18]
TencentGlobal = ["Tencent", 44, 44, 8263]
Oracle = ["Oracle", 3193, 20690, 771875]
amazon = ["Amazon", 0, 32271, 3205956]
Twitter = ["Twitter", 0, 13222, 57344020]
Square = ["Square", 3193, 13536, 253933]

tech = [Apple, Samsung, Microsoft, Google, intel,  IBM, Facebook,
HonHaiPrecision, TencentGlobal, Oracle, amazon,  Twitter, Square]


x_tech_tweets = []
x_tech_total = []
x_tech_followers = []
y_tech = []

x_7_tweets = []
x_7_total = []
x_7_followers = []
y_7 = []

for company in tech:
	x_tech_tweets.append(company[1])
	x_tech_total.append(company[2])
	x_tech_followers.append(company[3])
	y_tech.append(company[0])

for company in big7:
	x_7_tweets.append(company[1])
	x_7_total.append(company[2])
	x_7_followers.append(company[3])
	y_7.append(company[0])


def plot_bar(title, x, y_label, y):
	y_pos = np.arange(len(y))
	plt.bar(y_pos, x, align='center', alpha=0.5)
	plt.xticks(y_pos, y)
	plt.ylabel(y_label)
	plt.title(title)
	plt.show()

plot_bar("Big 7: Total Tweets", x_7_total, "Total Number of Tweets", y_7)
plot_bar("Big 7: Our Tweet Count", x_7_tweets, "# Tweets we Have", y_7)
plot_bar("Big 7: Followers", x_7_followers, "Total Number of Followers", y_7)

plot_bar("Tech Companies: Total Tweets", x_tech_total, "Total Number of Tweets", y_tech)
plot_bar("Tech Companies: Our Tweet Count", x_tech_tweets, "# Tweets we Have", y_tech)
plot_bar("Tech Companies: Followers", x_tech_followers, "Total Number of Followers", y_tech)


