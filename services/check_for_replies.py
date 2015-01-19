'''
import tweepy
from cqlengine import connection
from cqlengine.management import sync_table

class Listener(tweepy.StreamListener):

    connection.setup(['127.0.0.1'], "tiktok")

    def on_status(self, status):
        try:
            c = self.conn.cursor()
            c.execute("""insert into feed_post values (%r,'%s','%s',%d)""") % (status.id, status.text, status.author.screen_name, status.created_at)
            self.conn.commit()
        except:
            pass


def main():
    auth = tweepy.OAuthHandler('C_KEY', 'C_SECRET')
    auth.set_access_token('ACCESS_TOKEN', 'ACCESS_SECRET')
    stream = tweepy.Stream(auth=auth, listener=Listener())
    stream.filter(track=('CassandraPopQuiz',))

'''