from cqlengine import columns
from cqlengine.models import Model


class Tweets(Model):
    id = columns.UUID(primary_key=True)
    tweet = columns.Text()
    description = columns.Text()
    created = columns.DateTime()
    modified = columns.DateTime()

class Queue(Model):
    id = columns.UUID(primary_key=True)
    name = columns.Text()
    created = columns.DateTime()
    modified = columns.DateTime()

class Tweets_queue(Model):
    queue_id = columns.UUID(primary_key=True)
    time_to_send = columns.DateTime(primary_key=True, clustering_order="DESC")
    tweet_id = columns.UUID(primary_key=True, clustering_order="ASC")

class Tweets_sent(Model):
    queue_id = columns.UUID(primary_key=True)
    time_sent = columns.DateTime(primary_key=True, clustering_order="DESC")
    tweet_id = columns.UUID()

class Queue_tweet_responses(Model):
    queue_id = columns.UUID(primary_key=True)
    time_received = columns.DateTime(primary_key=True, clustering_order="DESC")
    user = columns.Text(primary_key=True)
    tweet_id = columns.UUID()
    response = columns.Text()


class Tweets_sent_by_twitter_id(Model):
    twitter_id = columns.BigInt(primary_key=True)
    queue_id = columns.UUID()
    tweet_id = columns.UUID()