import tweepy
from tweepy import OAuthHandler
import sys

consumer_key = "v7eSzVS0EKjwrDhkgY9iUYSxi"
consumer_secret = "D7KeEJYuhWj1tRUSKQc4i3beOnCBoROYHqY4GjkvPMn5O2Kh4k"
access_token = "1185579278173425667-hNI7QURnmXAh1BSyycGq21W1gqQki6"
access_secret = "UVnsbxz1XWyJ861MqAIKTNkOpzNkLK1zBgKLgRVRKMMbw"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,  wait_on_rate_limit=True)

replies=[] 
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)  

for full_tweets in tweepy.Cursor(api.user_timeline,screen_name='shell',timeout=999999).items(10):
  for tweet in tweepy.Cursor(api.search,q='to:bluthquotes', since_id=992433028155654144, result_type='recent',timeout=999999).items(1000):
  	if hasattr(tweet, 'in_reply_to_status_id_str'):
  		if (tweet.in_reply_to_status_id_str==full_tweets.id_str):
  			replies.append(tweet.text)
  print("Tweet :",full_tweets.text.translate(non_bmp_map))
  for elements in replies:
	   print("Replies :",elements)
  replies.clear()