from django.contrib.gis import admin
from django.db import models
from main.gmaps_admin import GoogleAdmin
from models import Airfield, Figure

###############################################################################

class FigureInline(admin.StackedInline):
    model = Figure
    extra = 1

class Map(GoogleAdmin):
    fields = ('name', 'slug', 'lat_lng', 'location', 'runway', 'revised', 'body')
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name",)}
    inlines = [FigureInline]
    readonly_fields = ('lat_lng', )

########################################

class FigureAdmin(admin.ModelAdmin):
    list_display = ('airfield', 'name', 'thumb')

########################################

admin.site.register(Airfield, Map)
admin.site.register(Figure, FigureAdmin)
