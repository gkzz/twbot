from requests_oauthlib import OAuth1Session
import json
import keys
import random
import datetime

twitter = OAuth1Session(keys.CONSUMER_KEY,  keys.CONSUMER_SECRET, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)

tweets = [

    "Don’t beg for it, earn it. Do it, and you’ll be rewarded.",
    "Freedom is something that you need to actively acquire. ",
    
    ]   

randomtweet = tweets[random.randrange(len(tweets))]

params = {"status": randomtweet + " "} 
twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
