from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from tiktokadmin.models import Tweets
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

def queue(request):
    template = loader.get_template('tiktokadmin/queue.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))



def queue_created(request):
    text = request.POST['queuename']
    Tweets.create(id = uuid.uuid4(), created = datetime.utcnow(), modified = datetime.utcnow(),  name = text)
    return HttpResponse(text)


"""
def schedule(request):


def queue_detail(request):


def edit(request):


def responses(request):


def responses_detail(request):
"""