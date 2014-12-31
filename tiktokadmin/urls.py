from django.conf.urls import patterns, url

from tiktokadmin import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^create/$', views.create, name='create'),
                       url(r'^create/add/$', views.create_post, name='create_post'),
                       url(r'^queue/$', views.queue, name='queue'),
                       url(r'^queue/add/$', views.queue_created, name='queue_created'),
                       url(r'^queue/edit/$', views.queue_edit, name='queue_edit'),


                       )