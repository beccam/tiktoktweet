import uuid
import tweepy
from cqlengine import connection, columns, Model
from models import  Queue_tweet_responses
from cqlengine.management import sync_table


class Listener(tweepy.StreamListener):

    connection.setup(['127.0.0.1'], "tiktok")

    def on_status(self, status):
        try:
            Queue_tweet_responses.create(queue_id =, time_received = status.created_at, tweet_id = uuid.uuid4(),  response =status.text)
        except:
            pass


def main():
    auth = tweepy.OAuthHandler('C_KEY', 'C_SECRET')
    auth.set_access_token('ACCESS_TOKEN', 'ACCESS_SECRET')
    stream = tweepy.Stream(auth=auth, listener=Listener())
    stream.filter(track=('CassandraPopQuiz',))

