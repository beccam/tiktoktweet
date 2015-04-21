from django.conf.urls import patterns, include, url
from django.contrib import admin
from tiktoktweet.settings import STATIC_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiktoktweet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tiktokadmin/', include('tiktokadmin.urls', namespace="tiktokadmin")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : True}),
                        )