#!/bin/sh

python ./manage.py runserver &
python ./services/send_tweets.py &
python ./services/check_for_replies.py &