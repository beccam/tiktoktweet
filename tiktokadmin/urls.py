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
                       url(r'^tweet/final/$', views.tweet_final, name='tweet_final'),
                       url(r'^tweet/delete/$', views.tweet_delete, name='tweet_delete'),
                       url(r'^queue/delete/$', views.queue_delete, name='queue_delete'),
                       url(r'^schedule/$', views.schedule_tweet, name='schedule_tweet'),
                       url(r'^schedule/queue$', views.add_queue, name='add_queue'),
                       url(r'^schedule/queue_done$', views.add_queue_done, name='add_queue_done'),
                       url(r'^responses/$', views.responses, name='responses'),
                       url(r'^responses/manage/$', views.responses_manage, name='responses_manage'),


                       )