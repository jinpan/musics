from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from musics.core import urls as core_urls


urlpatterns = patterns('',
    url(r'^list$', TemplateView.as_view(template_name='list.html')),
    url(r'^play$', TemplateView.as_view(template_name='play.html')),
)

urlpatterns += core_urls.urlpatterns
