from django.db import models

from cqlengine import columns
from cqlengine.models import Model

# Create your models here.

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


class Queue_tweet_responses(Model):
    queue_id = columns.UUID(primary_key=True)
    time_received = columns.TimeUUID(primary_key=True, clustering_order="DESC")
    tweet_id = columns.UUID()
    response = columns.Text()

class Tweets_sent(Model):
    queue_id = columns.UUID(primary_key=True)
    time_sent = columns.DateTime(primary_key=True, clustering_order="DESC")
    tweet_id = columns.UUID()

