from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from musics.core import urls as core_urls


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^list', TemplateView.as_view(template_name='list.html')),

)

urlpatterns += core_urls.urlpatterns
