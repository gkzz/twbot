import feedparser
import time
import random
import datetime
from requests_oauthlib import OAuth1Session
import keys   
import os
import sys


def make_contents(url):
    contents = []
    feed_result = feedparser.parse(url)
    try_conts = 1
    for entry in feed_result.entries:
        if try_conts <= 3:
            #import pdb; pdb.set_trace()
            tmp = entry.title + ' ' + entry.link
            contents.append(tmp)
            try_conts += 1
    
    return contents



        
# get RSSs of some Youtube channels

# LADY GAGA
# https://www.youtube.com/channel/UCNL1ZadSjHpjm4q9j2sVtOA

# Avicii
# https://www.youtube.com/channel/UC1SqP7_RfOC9Jf9L_GRHANg
feed_urls = [

    # LADY GAGA
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCNL1ZadSjHpjm4q9j2sVtOA"
    
    # Avicii
    "https://www.youtube.com/feeds/videos.xml?channel_id=UC1SqP7_RfOC9Jf9L_GRHANg"

]

twitter = OAuth1Session(
    keys.CONSUMER_KEY,
    keys.CONSUMER_SECRET,
    keys.ACCESS_TOKEN,
    keys.ACCESS_TOKEN_SECRET,
    )


if __name__ == '__main__':
    start = time.time()
    
    _tweets = []
    
    for feed_url in feed_urls:
        time.sleep(random.randint(8,12))
        _tweets.extend(make_contents(feed_url))
    
    
    random_conts = 1
    while True:
        if random_conts <= 5:
            randomtweet = _tweets[random.randrange(len(_tweets))]
            params = {"status": randomtweet + " "} 
            twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
            random_conts += 1
        else:
            break
        
    end = time.time()
    print("process {0} ms".format((end - start) * 1000))
    sys.exit()


           