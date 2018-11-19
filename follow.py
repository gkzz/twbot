import tweepy
import time
import keys
import random
import logging 

logging.basicConfig(level=logging.INFO)

# __name__ is "name" of the modules
logger = logging.getLogger(__name__)


auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#print(auth)
#print(api)


# try to follow your followers one by one
try:
    for follower in tweepy.Cursor(api.followers).items(20):
        time.sleep(random.randint(3,5))
        follower.follow()
        print (follower.screen_name)
except:
    pass


q_list = [

    '#TopNews min_retweets:1 OR min_faves:10',
    '#python',
]


#https://stackoverflow.com/questions/40065791/using-tweepy-to-follow-people-tweeting-a-specific-hashtag

usernames = []
for q in q_list:
    counts_num = 0
    while True:
        try:
            for tweet in tweepy.Cursor(api.search, q).items(100):
                time.sleep(random.randint(3,5))
                usernames.extend(tweet.user._json['screen_name'])
                counts_num += 1
                print(screen_name)
        except:
            break
    print(q +'>>> I could get'+ str(len(usernames)) +' users.')
username_conts = len(usernames)
print('TOTAL :' + str(len(usernames)))
print("##################")
for username in usernames:
    try:
        time.sleep(random.randint(3,5))
        api.create_friendship(username)
        print('I follow' + username + '.')
    except:
        print('api.create_friendship(user_id) >>> ERROR')
    
    