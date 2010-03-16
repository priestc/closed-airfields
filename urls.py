# encoding: utf-8

from django.conf.urls.defaults import *
from django.contrib import admin

from django.views.generic.simple import direct_to_template, redirect_to

admin.autodiscover()

#########################

urlpatterns = patterns('',
    
    (r'^$',           redirect_to, {"url": "/home.html"}),
    
    (r'^admin/doc/',  include('django.contrib.admindocs.urls')),
    (r'^admin/',      include(admin.site.urls)),
    (r'^airfield/',   include('closed_airfields.airfield.urls')),

    url(
        r'^browse_by_(?P<var>state|name)\.html$',
        'airfield.views.browse_by',
        name="browse_by"
    ),
    
    url(
        r'^map\.html$',
        'airfield.views.themap',
        name="map"
    ),
    
    url(
        r'^home\.html$',
        direct_to_template,
        {'template': "home.html"},
        name="home"
    ),
    
    (r'robots.txt', 'airfield.views.robot'),
    
    ###################################
    
    (r'^ca-media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': '/srv/closed_airfields/media', 'show_indexes': True},
    ),
)
