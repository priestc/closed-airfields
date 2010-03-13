# encoding: utf-8

from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/doc/',  include('django.contrib.admindocs.urls')),
    (r'^admin/',      include(admin.site.urls)),
    (r'^airfield/',   include('closed_airfields.airfield.urls')),
    
    url(
        r'latest_changes\.html',
        'airfield.views.latest_changes',
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














"""
{1953}

Photo of the airfield while open has not been located. The date of construction of this small landing strip is unknown. The earliest reference to this field which has been located was on the April 1953 Fargo Sectional Chart (courtesy of Timothy Aanerud). It depicted Wimbledon as a public-use airfield having a 2,600' unpaved runway. The March 1965 Fargo Sectional Chart (courtesy of Timothy Aanerud) depicted Wimbledon in the same fashion.

{1982}

At some point between 1965-86, the status of Wimbledon changed to a private airfield, as that is how it was depicted on the July 1986 Twin Cities Sectional Chart (according to Timothy Aanerud).

{1997}

In the 1997 USGS aerial photo, there were no obvious signs of use of the Wimbledon Airport (no aircraft visible outside, etc.). A single small hangar was located just west of the north end of the runway.

{2001}

The last depiction which has been located of Wimbledon as an active airfield was on the July 2001 Twin Cities Sectional Chart (courtesy of Timothy Aanerud).

The Wimbledon Airport was evidently closed (for reasons unknown) at some point between 2001-03, as it was no longer depicted at all on the July 2003 Twin Cities Sectional Chart (according to Timothy Aanerud).

{2006}

Jim reported also seeing a building being used for storage which looked “very much like a hangar.” Wimbledon Airport is located southwest of the intersection of Route 9 & 96th Avenue Southeast.

Thanks to Timothy Aanerud for pointing out this airfield.
"""
