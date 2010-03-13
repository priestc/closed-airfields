from django.contrib.gis import admin
from django.db import models
from main.gmaps_admin import GoogleAdmin
from models import Airfield, Figure

###############################################################################

class FigureInline(admin.StackedInline):
    model = Figure
    extra = 1

class Base(object):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name",)}
    inlines = [FigureInline]


class NoMap(Base, admin.ModelAdmin):
    pass

class Map(Base, GoogleAdmin):
    pass

########################################

class FigureAdmin(admin.ModelAdmin):
    list_display = ('airfield', 'name', 'thumb')

########################################

admin.site.register(Airfield, Map)
admin.site.register(Figure, FigureAdmin)
