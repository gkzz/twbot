import feedparser
import time
import random
import datetime
#import tweepy
#import twitter
from requests_oauthlib import OAuth1Session
import keys   #ここでトークンなどの設定ファイルを読み込む。
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
            #contents['title'] = entry.title
            #print('title: ', contents['title'])
            #contents['link'] = entry.link
            #print('link: ', contents['link'])
            contents.append(tmp)
            try_conts += 1
    
    return contents



        
# RSSから記事タイトルを取得
feed_urls = [
    # イクラチャンネル
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCtLG0FmkyhcPbHIAepy50mg',

    # PEANUTS!! ／ cherry CC tonic ©（チェリーココトニック）
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCKk0SS7RrZIdOCH46WmSM4w',

    # ザ・スパイシーズ
    'https://www.youtube.com/feeds/videos.xml?channel_id=spicykoyadofu',

    # miotron
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCmQQ2ReK5p2vfwkeabJyz_g',

    # 山瀬亜子
    'https://www.youtube.com/feeds/videos.xml?channel_id=UC3R8ycupH-PcofJz_7KTnfA',

    # マーベルエール Yell Marvel
    'https://www.youtube.com/feeds/videos.xml?channel_id=UC2pqdo5roC5GrIcw1CpjpRg',

    # sony music 綾野ましろ
    'https://www.youtube.com/feeds/videos.xml?channel_id=sonymusicnetwork',

    # アクターズスクール広島
    'https://www.youtube.com/feeds/videos.xml?channel_id=ActorsHiroshima',

]

twitter = OAuth1Session(
    keys.CONSUMER_KEY,
    keys.CONSUMER_SECRET,
    keys.ACCESS_TOKEN,
    keys.ACCESS_TOKEN_SECRET,
    )


if __name__ == '__main__':
    start = time.time()

    pr_tweet = '【ライブの予定があるアーティスト様へ】\
    無言フォローすみません！\
    ライブ情報をTweet、RTweet、いいね！します。フォローバックしていただけるとうれしいです♬\
    【No Music, No Life!】\
    #ライブ情報 #セトリ #相互フォロー'

    params = {"status": pr_tweet + " "} 
    twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

    _tweets = []
    
    for feed_url in feed_urls:
        time.sleep(random.randint(8,12))
        _tweets.extend(make_contents(feed_url))
        print('LINE73', _tweets)
    
    #for _tweet in _tweets:
    #    try:
    #        params = {"status": _tweet + " "} 
    #        twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
    #        print('LINE78', _tweet)
    #    except:
    #        pass
    
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


           