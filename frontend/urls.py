#ROOT_URLCONF = 'djangorest.urls'
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from frontend.views import index
urlpatterns = patterns('',
    url(r'^index/$', 'frontend.views.index_page', name='index'),
    
)
