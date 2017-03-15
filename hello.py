__author__ = 'user'

import sys
import string
from twython import Twython

APP_KEY = ' ' # Consumer Key here
APP_SECRET = ' '   # Secret Consumer Key here
OAUTH_TOKEN = ' '  # Access Token here
OAUTH_TOKEN_SECRET = ' '  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


for i in range(0, 1):
    user_timeline = twitter.get_user_timeline(screen_name="BarackObama",count=3200)
    for tweet in user_timeline:
        if "america" in tweet['text'].lower():
            print tweet['text']

