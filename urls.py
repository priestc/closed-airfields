# encoding: utf-8

from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.views.generic.date_based import archive_index
admin.autodiscover()

#########################
from airfield.models import Airfield

latest_changes = {'queryset': Airfield.objects.all(),
                  'date_field': 'revised',
                  'template_name': 'latest.html',}


#########################

urlpatterns = patterns('',

    (r'^admin/doc/',  include('django.contrib.admindocs.urls')),
    (r'^admin/',      include(admin.site.urls)),
    (r'^airfield/',   include('closed_airfields.airfield.urls')),
    
    url(
        r'latest_changes\.html',
        archive_index,
        latest_changes,
        name="latest_changes"
    ),
    
    url(
        r'browse_by_(?P<var>state|name)\.html',
        'airfield.views.browse_by',
        name="browse_by"
    ),
    
    url(
        r'map\.html',
        'airfield.views.themap',
        name="map"
    ),
    
    url(
        r'home\.html',
        direct_to_template,
        {'template': "home.html"},
        name="home"
    ),
    
    ###################################
    
    (r'^ca-media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': '/srv/closed_airfields/media', 'show_indexes': True},
    ),
)
