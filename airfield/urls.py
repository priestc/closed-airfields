from django.conf.urls.defaults import *

urlpatterns = patterns('airfield.views',
    url(r'(?P<slug>.+)\.html',    'display_airfield', name='airfield'),
)
