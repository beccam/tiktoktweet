TikTokTweet
===========

Twitter client for scheduling tweets.

## Introduction

TikTokTweet is a tweet scheduler written in Python and backed by Cassandra. Some features inlcude:

Ability to create a Tweet
* You can save it in the database for it for later
* Optionally add it directly to a queue to be tweeted out at a set time.

Add your saved tweets to a queue
* Assign a date and time to saved tweets to be sent out from the Schedule a Tweet page
* Choose a to particular queue to add the tweet to

Create queues for tweets
* Create and name queues for a specific categories of tweet
* Add tweets to these queues to be sent out on schedule
* Add tweets directly from Create Tweet or add a saved tweet from the Schedule a Tweet page
* Add new queues from the Manage queues page, and edit or delete queued tweets as well

Collect responses to you tweets
* Listener collects responses to you tweets
* These are stored in Cassandra according to the queue of the orginal tweet

## Requirements

The current version of TikTokTweets works with:
* Django (see the docs)
* cqlengine (Cassandra CQL 3 Object Mapper for Python)
* Tweepy
* Django Cassandra Engine 0.2.2 (the Cassandra backend for Django)
* Cassandra 2.x
* Python 2.7

Install Django

`pip install django`

Install cqlengine using

`pip install cqlengine`

Install Tweepy

`pip install tweepy`

Install Django Cassandra Engine

`pip install django-cassandra-engine`


## Configuration
Edit the comfiguration file conf/config.txt

```
[connection]
host = 127.0.0.1
keyspace = tiktok

[replies]
in_reply_to = @CassPopQuiz
account_id = 2815304775

[conf]
CONSUMER_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CONSUMER_SECRET = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_SECRET = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


[time]
my_time = 10

[db_settings]
keyspace = tiktok
host = 127.0.0.1
# for replication
strategy_class = SimpleStrategy
replication_factor = 1

```


## Run tiktoktweet

Once you’ve set your config file, you can start up

```
$ bash job.sh
```

and the app should be available in your browser:

http://127.0.0.1:8000/tiktokadmin/

