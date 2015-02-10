from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from tiktokadmin.models import Tweets, Queue, Tweets_queue, Queue_tweet_responses
from tiktokadmin.classes import TweetMetaData
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
    template = loader.get_template('tiktokadmin/create_post.html')
    text = request.POST['tweettext']
    queueid = request.POST['queue_id']
    tweetid = uuid.uuid4()
    if queueid != '0':
        tweet_time = request.POST['when_to_tweet']
        if tweet_time == '':
            template = loader.get_template('tiktokadmin/create_post_no_time.html')
            context = RequestContext(request)
            return HttpResponse(template.render(context))

        tweet_time = datetime.strptime(tweet_time, '%Y-%m-%d %H:%M:%S')
        Tweets_queue.create(queue_id = queueid, time_to_send = tweet_time, tweet_id = tweetid)
    Tweets.create(id = tweetid, created = datetime.utcnow(), modified = datetime.utcnow(),  tweet = text)
    context = RequestContext(request, {'text': text})
    return HttpResponse(template.render(context))


def queue(request):
    template = loader.get_template('tiktokadmin/queue.html')
    queue_list = Queue.objects.all()
    context = RequestContext(request, {'queue_list': queue_list})
    return HttpResponse(template.render(context))

def queue_created(request):
    template = loader.get_template('tiktokadmin/queue_created.html')
    text = request.POST['queuename']
    if not text:
        return HttpResponse("No queue name was entered")
    Queue.create(id = uuid.uuid4(), created = datetime.utcnow(), modified = datetime.utcnow(),  name = text)
    context = RequestContext(request, {'text': text} )
    return HttpResponse(template.render(context))

def queue_edit(request):
    template = loader.get_template('tiktokadmin/queue_edit.html')
    queue_id = request.POST['queue_id']
    tweetqueue_list = Tweets_queue.objects.filter(queue_id = queue_id)
    queuelist = Queue.get(id = queue_id)
    #do a foreach loop on tweetqueue_list to get all tweet_ids for reteiving tweets from Tweets table.
    tweet_list = []
    for entry in tweetqueue_list:
        tweet = Tweets.get(id = entry.tweet_id)
        tweet_list.append(TweetMetaData(tweet.id, tweet.tweet, entry.queue_id, entry.time_to_send.strftime("%Y-%m-%d %H:%M:%S")))
    context = RequestContext(request, {'tweet_list': tweet_list,'queue_id': queue_id, 'queuelist': queuelist} )
    return HttpResponse(template.render(context))


def queue_delete(request):
    template = loader.get_template('tiktokadmin/queue_deleted.html')
    if 'queue_id' in request.POST:
        queue_id = request.POST['queue_id']
        Tweets_queue.objects(queue_id= queue_id).delete()
        Queue.objects(id= queue_id).delete()
        context = RequestContext(request)
        return HttpResponse(template.render(context))
    else:
        pass


def tweet_edit(request):
    if 'queue_id' in request.POST:
        template = loader.get_template('tiktokadmin/tweet_edit.html')
        time_to_send = request.POST['time_to_send']
        tweet_id = request.POST['tweet_id']
        queue_id = request.POST['queue_id']
        tweet_data = Tweets.get(id = tweet_id)
        context = RequestContext(request, {'tweet_data':tweet_data,'queue_id': queue_id, 'time_to_send': time_to_send})
        return HttpResponse(template.render(context))
    else:
        template = loader.get_template('tiktokadmin/tweet_edit.html')
        tweet_id = request.POST['tweet_id']
        tweet_data = Tweets.get(id = tweet_id)
        context = RequestContext(request, {'tweet_data':tweet_data})
        return HttpResponse(template.render(context))

def tweet_final(request):
    template = loader.get_template('tiktokadmin/tweet_final.html')
    if 'queue_id' in request.POST:
        text = request.POST['tweettext']
        old_tweet_time = request.POST['old_tweet_time']
        old_tweet_time = datetime.strptime(old_tweet_time, '%Y-%m-%d %H:%M:%S')
        tweet_time = request.POST['new_time']
        tweet_id = request.POST['tweet_id']
        tweet_time = datetime.strptime(tweet_time, '%Y-%m-%d %H:%M:%S')
        queue_id = request.POST['queue_id']
        Tweets.objects(id=tweet_id).update(tweet= text, modified = datetime.utcnow())
        Tweets_queue.objects(queue_id = queue_id, time_to_send = old_tweet_time).delete()
        Tweets_queue.create(queue_id = queue_id, time_to_send = tweet_time, tweet_id = tweet_id)

    else:
        text = request.POST['tweettext']
        tweet_time = request.POST['new_time']
        tweet_id = request.POST['tweet_id']
        Tweets.objects(id=tweet_id).update(tweet= text, modified = datetime.utcnow())
    context = RequestContext(request, {'text':text})
    return HttpResponse(template.render(context))


def schedule_tweet(request):
    template = loader.get_template('tiktokadmin/schedule_tweet.html')
    tweet_list = Tweets.objects.all()
    context = RequestContext(request, {'tweet_list': tweet_list})
    return HttpResponse(template.render(context))


def responses(request):
    template = loader.get_template('tiktokadmin/responses.html')
    queue_list = Queue.objects.all()
    context = RequestContext(request, {'queue_list': queue_list})
    return HttpResponse(template.render(context))

def responses_manage(request):
    template = loader.get_template('tiktokadmin/responses_manage.html')
    queue_id = request.POST['queue_id']
    responsequeue_list = Queue_tweet_responses.filter(queue_id = queue_id)
    queuelist = Queue.get(id = queue_id)
    context = RequestContext(request, {'responsequeue_list': responsequeue_list, 'queuelist': queuelist})
    return HttpResponse(template.render(context))

def tweet_delete(request):
    return HttpResponse("hi")

def add_queue(request):
    template = loader.get_template('tiktokadmin/add_queue.html')
    tweet_id = request.POST['tweet_id']
    queue_list = Queue.objects.all()
    context = RequestContext(request, {'queue_list': queue_list, 'tweet_id': tweet_id})
    return HttpResponse(template.render(context))

def add_queue_done(request):
    template = loader.get_template('tiktokadmin/queue_done.html')
    tweet_id = request.POST['tweet_id']
    when_to_tweet = request.POST['when_to_tweet']
    tweet_time = datetime.strptime(when_to_tweet, '%Y-%m-%d %H:%M:%S')
    queue_id = request.POST['queue_id']
    Tweets_queue.create(queue_id = queue_id, time_to_send = tweet_time, tweet_id = tweet_id)
    context = RequestContext(request, {'queue_id': queue_id, 'when_to_tweet': when_to_tweet})
    return HttpResponse(template.render(context))





"""
def schedule(request):


def queue_detail(request):


def edit(request):


def responses(request):


def responses_manage(request):
"""