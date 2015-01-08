__author__ = 'rebeccamills'

class TweetMetaData:
    def __init__(self, tweet_id, tweet, queue_id, time_to_send):
        self.tweet_id = tweet_id
        self.tweet = tweet
        self.queue_id = queue_id
        self.time_to_send = time_to_send
