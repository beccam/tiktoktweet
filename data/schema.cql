//schema for tiktoktweet

DROP KEYSPACE IF EXISTS tiktoktweet;
CREATE KEYSPACE tiktoktweet WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };

use tiktoktweet;


/* Table to store tweets. There is timestamp for the initial creation of the tweet and one for date/time
 * modified incase any edits are made.
*/
CREATE TABLE tweets (
  id UUID,
  tweet text,
  description text,
  created timestamp,
  modified timestamp,
  PRIMARY KEY(id)
);

//Table to store the different queues created. A queue is a list of tweets of a particular category. Each queue type gets its own unique id.
CREATE TABLE queue (
  id UUID,
  name text,
  created timestamp,
  modified timestamp,
  PRIMARY KEY (id)
);

//Table showing what tweets are associated with which queues and time for the tweet to be sent out. Each tweet is in a particular queue with a certain set time to be set out, hence the chosen primary key. Clustering order for time_to_send is descending such that next tweet to go out is at the top of the list.
CREATE TABLE tweets_queue (
   queue_id UUID,
   time_to_send timestamp,
   tweet_id UUID,
   PRIMARY KEY(queue_id, time_to_send, tweet_id)
) WITH CLUSTERING ORDER BY (time_to_send DESC, tweet_id ASC);


//Tables to hold responses to tweets. TIMEUUID is used as a distinct identifier here to deal with the unlikely possibility that two people could reply to a tweet at the exact same time. The queue_id is including in the primary key such that we can select the responses for a particular queue. Ordering by time descending is chosen such that the latest reply will be at the top of the list.

CREATE TABLE queue_tweet_responses (
   time_received TIMEUUID,
   tweet_id UUID,
   queue_id UUID,
   response text,
   PRIMARY KEY(queue_id, time_received)
) WITH CLUSTERING BY (time_received desc);



//Table to hold tweets which have already been sent. This is so we can keep track of tweets that have already been sent out. Eventually this could be work to help us if the program crashes and we don't end up sending the same tweets out again by accident.
CREATE TABLE tweets_sent (
   queue_id UUID,
   time_sent timestamp,
   tweet_id UUID,
   PRIMARY KEY(queue_id, time_sent)
) WITH CLUSTERING ORDER BY (time_sent desc);


