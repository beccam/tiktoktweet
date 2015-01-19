from cqlengine import columns
from cqlengine.models import Model
from models import Tweets, Queue, Tweets_queue, Tweets_sent
from datetime import datetime
import sys

from cqlengine import connection

connection.setup(['127.0.0.1'], "tiktok")

from cqlengine.management import sync_table
sync_table(Tweets)
sync_table(Queue)
sync_table(Tweets_queue)

q= Tweets_queue.objects.filter(Tweets_queue.queue_id == 'ceb55051-01b6-4b41-b965-c61adb5ad817')

tweetlist= []
for entry in q:
    tweet = Tweets.get(id = entry.tweet_id)
    tweetlist.append(tweet.tweet)
    print "Here is your tweet: s% " % tweet.tweet
    Tweets_sent.create(queue_id = entry.queue_id, time_sent = datetime.utcnow(), tweet_id = tweet.id)
    Tweets_queue.objects(queue_id = entry.queue_id, time_to_send = entry.time_to_send).delete()

k= Tweets_queue.objects.filter(Tweets_queue.queue_id == 'c4aaa481-3a98-4f4b-a5f0-6d330ccd904d')

tweet_list= []
for entry in k:
    tweet = Tweets.get(id = entry.tweet_id)
    tweet_list.append(tweet.tweet)
    print "Here is your tweet: s% " % tweet.tweet
    Tweets_sent.create(queue_id = entry.queue_id, time_sent = datetime.utcnow(), tweet_id = tweet.id)
    Tweets_queue.objects(queue_id = entry.queue_id, time_to_send = entry.time_to_send).delete()

sys.exit()