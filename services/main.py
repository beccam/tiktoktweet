from cqlengine import columns
from cqlengine.models import Model
from services.models import Tweets, Queue, Tweets_queue
from datetime import datetime

from cqlengine import connection

connection.setup(['127.0.0.1'], "tiktok")

from cqlengine.management import sync_table
sync_table(Tweets)
sync_table(Queue)
sync_table(Tweets_queue)

q= Tweets_queue.objects.filter(Tweets_queue.queue_id = ceb55051-01b6-4b41-b965-c61adb5ad817)
q.filter(Tweets_queue.time_to_send > datetime.utcnow())

print q