from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from tiktokadmin.models import Tweets, Queue, Tweets_queue
import uuid
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('tiktokadmin/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def create(request):
    template = loader.get_template('tiktokadmin/create.html')
    queue_list = Queue.objects.all()
    context = RequestContext(request, {'queue_list': queue_list})
    return HttpResponse(template.render(context))

def create_post(request):
    text = request.POST['tweettext']
    tweet_time = request.POST['when_to_tweet']
    tweet_time = datetime.strptime(tweet_time, '%Y-%m-%d %H:%M:%S')
    queueid = request.POST['queue_id']
    tweetid = uuid.uuid4()
    Tweets.create(id = tweetid, created = datetime.utcnow(), modified = datetime.utcnow(),  tweet = text)
    Tweets_queue.create(queue_id = queueid, time_to_send = tweet_time, tweet_id = tweetid)
    return HttpResponse(text)


def queue(request):
    template = loader.get_template('tiktokadmin/queue.html')
    queue_list = Queue.objects.all()
    context = RequestContext(request, {'queue_list': queue_list})
    return HttpResponse(template.render(context))

def queue_created(request):
    text = request.POST['queuename']
    Queue.create(id = uuid.uuid4(), created = datetime.utcnow(), modified = datetime.utcnow(),  name = text)
    return HttpResponse(text)

def queue_edit(request):
    template = loader.get_template('tiktokadmin/queue_edit.html')
    queue_id = request.POST['queue_id']
    tweetqueue_list = Tweets_queue.objects.filter(queue_id = queue_id)
    #do a foreach loop on tweetqueue_list to get all tweet_ids for reteiving tweets from Tweets table.
    tweet_list = []
    for entry in tweetqueue_list:
        tweet_list.append(Tweets.get(id = entry.tweet_id))
    context = RequestContext(request, {'tweet_list': tweet_list},{'queue_id': queue_id} )
    return HttpResponse(template.render(context))


def queue_delete(request):
    if 'queue_id' in request.POST['queue_id']:
        Tweets_queue.objects(queue_id= queue_id).delete()
        Queue.objects(id= queue_id).delete()
    else:
        pass
    return HttpResponse("Tweet Deleted")

def tweet_edit(request):
    template = loader.get_template('tiktokadmin/tweet_edit.html')
    tweet_id = request.POST['tweet_id']
    queue_id = request.POST['queue_id']
    tweet_data = Tweets.get(id = tweet_id)
    context = RequestContext(request, {'tweet_data':tweet_data}, {'queue_id': queue_id})
    return HttpResponse(template.render(context))

def tweet_final(request):
    text = request.POST['tweettext']
    tweet_time = request.POST['new_time']
    tweet_id = request.POST['tweet_id']
    tweet_time = datetime.strptime(tweet_time, '%Y-%m-%d %H:%M:%S')
    queue_id = request.POST['queue_id']
    Tweets.objects(id=tweet_id).update(tweet= text, modified = datetime.utcnow())
    Tweets_queue.objects(queue_id=queue_id).update(time_to_send = tweet_time)
    return HttpResponse(text)


def schedule_tweet(request):
    template = loader.get_template('tiktokadmin/schedule_tweet.html')
    tweet_list = Tweets.objects.all()
    context = RequestContext(request, {'tweet_list': tweet_list})
    return HttpResponse(template.render(context))


def responses(request):
    template = loader.get_template('tiktokadmin/responses.html')
    tweet_list = Tweets.objects.all()
    context = RequestContext(request, {'tweet_list': tweet_list})
    return HttpResponse(template.render(context))

def responses_manage(request):
    return HttpResponse("hi")

def tweet_delete(request):
    return HttpResponse("hi")





"""
def schedule(request):


def queue_detail(request):


def edit(request):


def responses(request):


def responses_manage(request):
"""