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

q_list = [
    
    '#TopNews min_retweets:1 OR min_faves:10',
    '#python',
]

for q in q_list:
    try:
        time.sleep(random.randint(3,5))
        for tweet in tweepy.Cursor(api.search, q).items(20):
            try:
                tweet.favorite()
                time.sleep(random.randint(3,5))
                logger.info(tweet.favorite())
                #print('Retweet published successfully.')
        
                # Where sleep(10), sleep is measured in seconds.
                # Change 10 to amount of seconds you want to have in-between retweets.
                # Read Twitter's rules on automation. Don't spam!
                time.sleep(random.randint(11,14))
        
            # Some basic error handling. Will print out why retweet failed, into your terminal.
            except tweepy.TweepError as error:
                print('\nError. Favorite not successful. Reason: ')
                print(error.reason)
        
            except StopIteration:
                break

    except tweepy.TweepError as error:
                print('\nError. Favorite not successful. Reason: ')
                print(error.reason)
        
    except StopIteration:
        break
    