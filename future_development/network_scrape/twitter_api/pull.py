import twitter

api = twitter.Api(consumer_key=["v7eSzVS0EKjwrDhkgY9iUYSxi"],
                  consumer_secret=["D7KeEJYuhWj1tRUSKQc4i3beOnCBoROYHqY4GjkvPMn5O2Kh4k"],
                  access_token_key=["1185579278173425667-hNI7QURnmXAh1BSyycGq21W1gqQki6"],
                  access_token_secret=["UVnsbxz1XWyJ861MqAIKTNkOpzNkLK1zBgKLgRVRKMMbw"])

twurl authorize --consumer-key v7eSzVS0EKjwrDhkgY9iUYSxi --consumer-secret D7KeEJYuhWj1tRUSKQc4i3beOnCBoROYHqY4GjkvPMn5O2Kh4k


twurl "/1.1/followers/ids.json?cursor=-62&screen_name=WellsFargo&count=5000" > out.txt