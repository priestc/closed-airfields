from models import Airfield
from django.views.generic.list_detail import object_detail

def display_airfield(request, slug):
    return object_detail(request,
                         queryset=Airfield.objects.all(),
                         slug=slug,
                         slug_field='slug',
                         template_name='airfield.html',
                         template_object_name='airfield')
                         

def browse_by(request, var):
    return None

def latest_changes(request):
    return None

def search(request):
    return None

def themap(request):
    return None
