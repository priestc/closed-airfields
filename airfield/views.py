from models import Airfield
from annoying.decorators import render_to
from django.conf import settings
from django.views.generic.list_detail import object_detail
from django.contrib.gis.maps.google import GoogleMap
from django.contrib.gis.maps.google.overlays import GMarker, GIcon, GPolygon
from django.shortcuts import get_object_or_404

@render_to('map.html')
def themap(request):
    google = GoogleMap(map_type='terrain', center=(-99, 38.8), zoom=4)
    return locals()

def overlay(request, x, y, z):
    
    from gtileoverlay.overlays import GTileOverlay
    
    qs = Airfield.objects.all()    
    icon = '/srv/closed_airfields/media/icons/red_pad.png'

    ov = GTileOverlay(x=x, y=y, zoom=z, queryset=qs, icon=icon, field='location')
    
    return ov.as_response()

def browse_by(request, var):
    pass

@render_to('airfield.html')
def airfield(request, slug):
    
    airfield = get_object_or_404(Airfield, slug=slug)
    
    icon = GIcon("myicon", image="http://flightlogg.in/fl-media/icons/red_pad.png",
                           shadow='http://example.com',
                           iconsize=(32,32),
                           iconanchor=(16,16))
    
    kwargs = {}
    if airfield.runway:                      
        kwargs['polygons'] = [GPolygon(airfield.runway)]
    else:
        kwargs['markers'] = [GMarker(airfield.location, icon=icon)]
        kwargs['zoom'] = 15
        kwargs['center'] = airfield.location
    
    google = GoogleMap(map_type='satellite', **kwargs)
    
    return locals()

def robot(request):
    
    t="""User-agent: *
Disallow: /fl-uploads/*
Allow: /"""
    
    from django.http import HttpResponse
    return HttpResponse(t, mimetype="text/html")
