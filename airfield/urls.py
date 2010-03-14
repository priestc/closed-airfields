from django.conf.urls.defaults import *

from airfield.models import Airfield

from django.views.generic.date_based import archive_index

#########################
                 
latest_changes = {'queryset': Airfield.objects.all(),
                  'date_field': 'revised',
                  'allow_empty': True,
                  'template_name': 'latest.html',}
                  
#########################

urlpatterns = patterns('',
    
    url(
        r'latest_changes\.html$',
        archive_index,
        latest_changes,
        name="latest_changes",
    ),
    
    url(
        r'(?P<slug>.+)\.html$',
        'airfield.views.airfield',
        name='airfield',
    ),
    
)
