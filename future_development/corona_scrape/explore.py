from lxml import html
import requests
import re
import pickle 
import csv
from os import path

s = "lamont"

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

articles = load_obj("articles")
count = 0.0
for a in articles:
	title = a["title"].lower()
	link = a["link"].lower()
	text = a["text"].lower()

	if s in title or s in text or s in link:
		count += 1

print(count/len(articles))
