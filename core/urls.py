from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),

)


