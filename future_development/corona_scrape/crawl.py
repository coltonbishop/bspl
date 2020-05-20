from lxml import html
import requests
import re
import pickle 
import csv
from os import path




# {[tile, date, url, text]}
articles = []

# Filter by which we reject or accept articles
strainer = ['connecticut', "lamont", " c.t."]

link_strainer = ['connecticut', 'stamfordadvocate.com', 'courant.com', 'theday.com', 'rep-am.com', 'jounralinquirer.com', 'connpost.com', 
'nhregister.com', 'myrecordjournal.com', 'newstimes.com', 'thehour.com']

# Data source 
base_url = "https://visualizenow.org/corona-news?page={}"
i = 0

# Returns TRUE if article is relevant; else False
def relevant(text):
	for item in strainer:
		if item in text:
			return True
	return False

# Returns TRUE if article is relevant; else False
def relevant_link(link):
	for item in link_strainer:
		if item in link:
			return True
	return False
# Load Python object from pkl file
def load_obj(name):
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	print("Cannot find file {}".format(name + '.pkl'))
	return None
# Save Python object to pkl file
def save_obj(obj, name):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

print("Beginning Iterations")
# Iterates through each page of the data source
while(len(articles) < 10000):
	i+= 1
	# Saves files every 100 Pages (every 1000 Articles)
	if i % 100 == 0:
		print("Scraping Page {}, {} Relevant Articles Found".format(i, len(articles)))
		save_obj(articles, "articles")

	page = requests.get(base_url.format(i))
	tree = html.fromstring(page.content)
	# Iterates through the rows and columns (articles) on each page
	for y in range(1,11):
		for x in range(1, 4):
			link = tree.xpath("//div[@class='row pt-2 pb-2'][{}]/div[@class='col-md-4'][{}]/p[@class='font-weight-bold'][1]/a[1]/@href".format(y, x))[0].replace("\t", "").replace("\n", "").lower()
			title = tree.xpath("//div[@class='row pt-2 pb-2'][{}]/div[@class='col-md-4'][{}]/p[@class='font-weight-bold'][1]/a[1]/text()[1]".format(y, x))[0].replace("\t", "").replace("\n", "").strip(" ").lower()
			text = requests.get(link).content.lower()
			# If text or title flagged as relevant, save it in our data dictionary. 
			if relevant(title) or relevant_link(link) or relevant(text):
				date = tree.xpath("//div[@class='row pt-2 pb-2'][{}]/div[@class='col-md-4'][{}]/p[3]/text()[1]".format(y, x))[0].replace("\t", "").replace("\n", "").strip(" ")
				data = {"title": title, "date": date, "link": link, "text" : text}
				articles.append(data)
