from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from musics.core import urls as core_urls


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),

)

urlpatterns += core_urls.urlpatterns

