from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

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
    return HttpResponse(text)



"""
def schedule(request):


def queue(request):


def queue_detail(request):


def edit(request):


def responses(request):


def responses_detail(request):
"""