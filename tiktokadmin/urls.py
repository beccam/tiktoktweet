from django.conf.urls import patterns, url

from tiktokadmin import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^create/$', views.create, name='create'),
                       url(r'^create/add/$', views.create_post, name='create_post'),
                       url(r'^queue/$', views.queue, name='queue'),
                       url(r'^queue/add/$', views.queue_created, name='queue_created'),
                       url(r'^queue/edit/$', views.queue_edit, name='queue_edit'),
                       url(r'^tweet/edit/$', views.tweet_edit, name='tweet_edit'),
                       url(r'^tweet/delete/$', views.tweet_delete, name='tweet_delete'),
                       url(r'^queue/delete/$', views.queue_deleted, name='queue_deleted'),
                       url(r'^schedule/$', views.schedule_tweet, name='schedule_tweet'),
                       url(r'^responses/$', views.responses, name='responses'),
                       url(r'^responses/manage/$', views.responses_manage, name='responses_manage'),


                       )