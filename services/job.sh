#!/bin/sh

python ../manage.py runserver &
python ./send_tweets.py &
python ./check_for_replies.py &