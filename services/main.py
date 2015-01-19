
from models import Tweets, Queue, Tweets_queue, Tweets_sent
from datetime import datetime
import sys, logging, tweepy
from cqlengine import connection
from cqlengine.management import sync_table

logging.basicConfig(level=logging.INFO)
connection.setup(['127.0.0.1'], "tiktok")
logging.info("Connected to tiktok database")


sync_table(Tweets)
sync_table(Queue)
sync_table(Tweets_queue)


g= Queue.objects.all()

for x in g:

    q= Tweets_queue.objects.filter(Tweets_queue.queue_id == x.id, Tweets_queue.time_to_send < datetime.utcnow())

    tweetlist= []
    for entry in q:
        tweet = Tweets.get(id = entry.tweet_id)
        tweetlist.append(tweet.tweet)
        logging.info()
        Tweets_sent.create(queue_id = entry.queue_id, time_sent = datetime.utcnow(), tweet_id = tweet.id)
        Tweets_queue.objects(queue_id = entry.queue_id, time_to_send = entry.time_to_send).delete()




sys.exit()