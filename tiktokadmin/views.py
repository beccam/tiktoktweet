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
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def create_post(request):
    text = request.POST['tweettext']
    Tweets.create(id = uuid.uuid4(), created = datetime.utcnow(), modified = datetime.utcnow(),  tweet = text)
    return HttpResponse(text)

def create_to_queue(request):
    tweet_time = request.POST['when_to_tweet']
    queue_name = request.POST['{{queue.id}}']
    Tweets_queue.create(queue_id = queue_name, time_to_send = tweet_time, tweet_id = Tweets.get(id))
    return HttpResponse(tweet_time, queue_name )

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
    return HttpResponse("hi")

def queue_deleted(request):
    return HttpResponse("hi")

def tweet_edit(request):
    template = loader.get_template('tiktokadmin/tweet_edit.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

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





"""
def schedule(request):


def queue_detail(request):


def edit(request):


def responses(request):


def responses_manage(request):
"""