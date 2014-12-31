from django.conf.urls import patterns, url

from tiktokadmin import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^create/$', views.create, name='create'),
                       url(r'^create/add/$', views.create_post, name='create_post'),
                       url(r'^queue/$', views.queue, name='queue'),
                       url(r'^queue/add/$', views.queue_created, name='queue_created'),
                       url(r'^queue/edit/$', views.queue_edit, name='queue_edit'),
                       url(r'^queue/edit/tweet_edit/$', views.tweet_edit, name='tweet_edit'),
                       url(r'^queue/delete/$', views.queue_deleted, name='queue_deleted'),
                       url(r'^schedule/$', views.schedule_tweet, name='schedule_tweet'),


                       )