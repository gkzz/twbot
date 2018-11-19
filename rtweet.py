import tweepy
import time
#from keys import *
import keys
import random
import logging 

logging.basicConfig(level=logging.INFO)

# __name__ is "name" of the modules
logger = logging.getLogger(__name__)


#twitter = OAuth1Session(keys.CONSUMER_KEY,  keys.CONSUMER_SECRET, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#print(auth)
#print(api)


#https://twitter.com/takeda_juku

#q = q_list[random.randrange(len(q_list))]

q_list = [

    '#TopNews min_retweets:1 OR min_faves:10',
    '#python',
]

for q in q_list:
    try:
        time.sleep(random.randint(3,5))
        for tweet in tweepy.Cursor(api.search, q).items(20):
            try:
                print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
                time.sleep(random.randint(3,5))
                tweet.retweet()
                logger.info(tweet.retweet())
                #print('Retweet published successfully.')
        
                # Where sleep(10), sleep is measured in seconds.
                # Change 10 to amount of seconds you want to have in-between retweets.
                # Read Twitter's rules on automation. Don't spam!
                time.sleep(random.randint(11,14))
        
            # Some basic error handling. Will print out why retweet failed, into your terminal.
            except tweepy.TweepError as error:
                print('\nError. Retweet not successful. Reason: ')
                print(error.reason)
        
            except StopIteration:
                break

    except tweepy.TweepError as error:
                print('\nError. Retweet not successful. Reason: ')
                print(error.reason)
        
    except StopIteration:
        break
    