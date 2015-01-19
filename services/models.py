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
