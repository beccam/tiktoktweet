from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from tiktokadmin.models import Tweets, Queue, Tweets_queue, Queue_tweet_responses
from tiktokadmin.classes import TweetMetaData
import uuid
from datetime import datetime

from ConfigParser import SafeConfigParser
from models import Tweets, Queue, Tweets_queue, Tweets_sent
from datetime import datetime
import sys, logging, tweepy, time
from cqlengine import connection
from cqlengine.management import sync_table


connection.setup(['127.0.0.1'], "tiktok")


sync_table(Tweets)
sync_table(Queue)
sync_table(Tweets_queue)

tweetqueue_list = Tweets_queue.objects.filter(queue_id = 'ceb55051-01b6-4b41-b965-c61adb5ad817')
#do a foreach loop on tweetqueue_list to get all tweet_ids for retrieving tweets from Tweets table.
for entry in tweetqueue_list:
    tweets = Tweets.get(id = entry.tweet_id)
    print tweets.tweet
