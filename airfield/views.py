from models import Airfield
from annoying.decorators import render_to
from django.views.generic.list_detail import object_detail
from django.contrib.gis.maps.google import GoogleMap
from django.contrib.gis.maps.google.overlays import GMarker, GIcon
from django.shortcuts import get_object_or_404

@render_to('map.html')
def themap(request):
    google = GoogleMap()
    return locals()


def browse_by(request, var):
    pass

@render_to('airfield.html')
def airfield(request, slug):
    
    airfield = get_object_or_404(Airfield, slug=slug)
    
    icon = GIcon("myicon", image="http://flightlogg.in/fl-media/icons/red_pad.png",
                           shadow='http://example.com',
                           iconsize=(32,32),
                           iconanchor=(16,16))
                           
    marker = GMarker(airfield.location.wkt, icon=icon)
    google = GoogleMap(markers=[marker])
    
    return locals()
