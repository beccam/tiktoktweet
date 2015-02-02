
from ConfigParser import SafeConfigParser
from models import Tweets, Queue, Tweets_queue, Tweets_sent
from datetime import datetime
import sys, logging, tweepy, time
from cqlengine import connection
from cqlengine.management import sync_table


'''
This is for sending tweets. It can be run periodically
'''

logging.basicConfig(level=logging.INFO)
connection.setup(['127.0.0.1'], "tiktok")
logging.info("Connected to tiktok database")

sync_table(Tweets)
sync_table(Queue)
sync_table(Tweets_queue)


parser = SafeConfigParser()
parser.read('config.txt')

CONSUMER_KEY = parser.get('conf', 'CONSUMER_KEY')
CONSUMER_SECRET = parser.get('conf', 'CONSUMER_SECRET')
ACCESS_KEY = parser.get('conf', 'ACCESS_KEY')
ACCESS_SECRET = parser.get('conf', 'ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



g= Queue.objects.all()

for x in g:

    q= Tweets_queue.objects.filter(Tweets_queue.queue_id == x.id, Tweets_queue.time_to_send < datetime.utcnow())


    for entry in q:
        tweet = Tweets.get(id = entry.tweet_id)
        logging.info("Checking for tweets in for queue_id = %s" %  entry.queue_id)
        Tweets_sent.create(queue_id = entry.queue_id, time_sent = datetime.utcnow(), tweet_id = tweet.id)
        Tweets_queue.objects(queue_id = entry.queue_id, time_to_send = entry.time_to_send).delete()
        api.update_status(tweet.tweet)
        logging.info("Sent tweet")




sys.exit()

