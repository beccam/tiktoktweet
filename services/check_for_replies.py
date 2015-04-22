import tweepy
from models import Tweets, Queue, Tweets_queue, Tweets_sent, Queue_tweet_responses, Tweets_sent_by_twitter_id
from datetime import datetime
import sys, logging, tweepy, time
from cqlengine import connection, columns
from cqlengine.management import sync_table
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.txt')

logging.basicConfig(level=logging.INFO)
connection.setup([(parser.get('connection', 'host'))], (parser.get('connection', 'keyspace')))
logging.info("Connected to " + (parser.get('connection', 'keyspace')) + " database")


consumer_key = parser.get('conf', 'CONSUMER_KEY')
consumer_secret = parser.get('conf', 'CONSUMER_SECRET')
access_token = parser.get('conf', 'ACCESS_KEY')
access_token_secret = parser.get('conf', 'ACCESS_SECRET')

class StdOutListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        print(status.text)
        print(status.in_reply_to_status_id)
        print(status.created_at)
        print(status.author.screen_name)


        list = Tweets_sent_by_twitter_id.objects.filter(twitter_id = status.in_reply_to_status_id)
        tweet = list.get()
        Queue_tweet_responses.create(queue_id = tweet.queue_id , time_received = columns.TimeUUID.from_datetime(status.created_at), tweet_id = tweet.tweet_id, response = status.text, user = status.author.screen_name )

        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

def fill_in_timeline(auth):
    api = tweepy.API(auth)
    public_tweets = api.search((parser.get('replies', 'in_reply_to')), count =100)
    for status in public_tweets:

        print(status.text)
        print(status.in_reply_to_status_id)
        print(status.created_at)
        print(status.author.screen_name)

        if status.in_reply_to_status_id != None:

            list = Tweets_sent_by_twitter_id.objects.filter(twitter_id = status.in_reply_to_status_id)
            tweet = list.get()
            Queue_tweet_responses.create(queue_id = tweet.queue_id , time_received = status.created_at, tweet_id = tweet.tweet_id, response = status.text, user = status.author.screen_name )


if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler((parser.get('conf', 'CONSUMER_KEY')), (parser.get('conf', 'CONSUMER_SECRET')))
    auth.set_access_token((parser.get('conf', 'ACCESS_KEY')), (parser.get('conf', 'ACCESS_SECRET')))

    fill_in_timeline(auth)

    stream = tweepy.Stream(auth, listener)
    stream.filter(follow=[(parser.get('replies', 'account_id'))])

