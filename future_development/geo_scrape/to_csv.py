import csv
import pickle
from os import path

name = "nyc"

def load_obj():
	if path.exists(name + '.pkl'):
		with open(name + '.pkl', 'rb') as f:
			return pickle.load(f)
	return buckets

tweets = load_obj()
field_names = ['created_at', 'id', 'id_str', 'text', 'source', 'truncated', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place', 'contributors', 'quoted_status_id', 'quoted_status_id_str', 'quoted_status', 'quoted_status_permalink', 'is_quote_status', 'quote_count', 'reply_count', 'retweet_count', 'favorite_count', 'entities', 'favorited', 'extended_entities', 'possibly_sensitive', 'retweeted', 'filter_level', 'lang', 'timestamp_ms', 'display_text_range', 'extended_tweet']


with open('data.csv', 'w', newline='') as csvfile:

	writer = csv.DictWriter(csvfile, fieldnames=field_names)

	writer.writeheader()

	for tweet in tweets:
		writer.writerow(tweet)

		