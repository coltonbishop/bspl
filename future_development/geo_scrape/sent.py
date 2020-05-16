from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores_print(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
    return score

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)

# sentiment_analyzer_scores("I love this game! It is so cool and I can see it everywhere!")
# sentiment_analyzer_scores("Unimpressed with this shitty thing honestly. :/")

# {
#   "created_at": "Tue Sep 26 21:00:22 +0000 2017",
#   "id": 912783930431905797,
#   "id_str": "912783930431905797",
#   "text": "Can’t fit your Tweet into 140 characters? 🤔\n\nWe’re trying something new with a small group, and increasing the char… https://t.co/y1rJlHsVB5",
#   "source": "Twitter Web Client",
#   "truncated": true,
#   "in_reply_to_status_id": null,
#   "in_reply_to_status_id_str": null,
#   "in_reply_to_user_id": null,
#   "in_reply_to_user_id_str": null,
#   "in_reply_to_screen_name": null,
#   "user": {
#     "id": 783214,
#     "id_str": "783214",
#     "name": "Twitter",
#     "screen_name": "Twitter",
#     "location": "Everywhere",
#     "url": "https://about.twitter.com/",
#     "description": "What’s happening?!",
#     "translator_type": "null",
#     "protected": false,
#     "verified": true,
#     "followers_count": 56119543,
#     "friends_count": 140,
#     "listed_count": 91049,
#     "favourites_count": 5911,
#     "statuses_count": 10132,
#     "created_at": "Tue Feb 20 14:35:54 +0000 2007",
#     "utc_offset": null,
#     "time_zone": null,
#     "geo_enabled": true,
#     "lang": "en",
#     "contributors_enabled": false,
#     "is_translator": false,
#     "profile_background_color": "null",
#     "profile_background_image_url": "null",
#     "profile_background_image_url_https": "null",
#     "profile_background_tile": null,
#     "profile_link_color": "null",
#     "profile_sidebar_border_color": "null",
#     "profile_sidebar_fill_color": "null",
#     "profile_text_color": "null",
#     "profile_use_background_image": null,
#     "profile_image_url": "null",
#     "profile_image_url_https": "https://pbs.twimg.com/profile_images/1111729635610382336/_65QFl7B_normal.png",
#     "profile_banner_url": "https://pbs.twimg.com/profile_banners/783214/1556918042",
#     "default_profile": false,
#     "default_profile_image": false,
#     "following": null,
#     "follow_request_sent": null,
#     "notifications": null
#   },
#   "geo": null,
#   "coordinates": null,
#   "place": null,
#   "contributors": null,
#   "is_quote_status": false,
#   "extended_tweet": {
#     "full_text": "Can’t fit your Tweet into 140 characters? 🤔\n\nWe’re trying something new with a small group, and increasing the character limit to 280! Excited about the possibilities? Read our blog to find out how it all adds up. 👇\nhttps://t.co/C6hjsB9nbL",
#     "display_text_range": [
#       0,
#       239
#     ],
#     "entities": {
#       "hashtags": [

#       ],
#       "urls": [
#         {
#           "url": "https://t.co/C6hjsB9nbL",
#           "expanded_url": "https://cards.twitter.com/cards/gsby/4ubsj",
#           "display_url": "cards.twitter.com/cards/gsby/4ub…",
#           "unwound": {
#             "url": "https://cards.twitter.com/cards/gsby/4ubsj",
#             "status": 200,
#             "title": "Giving you more characters to express yourself",
#             "description": null
#           },
#           "indices": [
#             216,
#             239
#           ]
#         }
#       ],
#       "user_mentions": [

#       ],
#       "symbols": [

#       ]
#     }
#   },
#   "quote_count": 46955,
#   "reply_count": 17263,
#   "retweet_count": 50214,
#   "favorite_count": 89601,
#   "entities": {
#     "hashtags": [

#     ],
#     "urls": [
#       {
#         "url": "https://t.co/y1rJlHsVB5",
#         "expanded_url": "https://twitter.com/i/web/status/912783930431905797",
#         "display_url": "twitter.com/i/web/status/9…",
#         "indices": [
#           117,
#           140
#         ]
#       }
#     ],
#     "user_mentions": [

#     ],
#     "symbols": [

#     ]
#   },
#   "favorited": false,
#   "retweeted": false,
#   "possibly_sensitive": false,
#   "filter_level": "low",
#   "lang": "en",
#   "matching_rules": [
#     {
#       "tag": null
#     }
#   ]
# }