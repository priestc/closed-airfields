from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from django.conf import settings

GMAP = GoogleMap(key=settings.GOOGLE_MAPS_API_KEY)

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'
