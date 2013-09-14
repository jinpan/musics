from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('core.views',
    url(r'^api/queue/$', 'get_queue'),

    # only post requests should be sent here
    url(r'^api/add/$', 'add'),
    url(r'^api/dequeue/$', 'dequeue'),
    url(r'^api/downvote/$', 'downvote'),
    url(r'^api/upvote/$', 'upvote'),
)


