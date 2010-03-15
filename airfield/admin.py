from django import forms
from django.forms.widgets import TextInput
from django.contrib.gis import admin
from django.db import models
from main.gmaps_admin import GoogleAdmin
from models import Airfield, Figure

###############################################################################

class AirfieldAdminForm(forms.ModelForm):
    class Meta:
        model = Airfield
        widgets = {"body": forms.Textarea(attrs={"cols": 85, "rows": 35}),
                   "remarks": forms.TextInput(attrs={'style': "width:60em"})}

class FigureAdminForm(forms.ModelForm):
    class Meta:
        model = Figure
        widgets = {"contrib": forms.TextInput(),
                   "caption": forms.Textarea(attrs={"cols": 30, "rows": 3})}
        

###############################################################################

class FigureInline(admin.StackedInline):
    form = FigureAdminForm
    fields = ('image','name','caption','contrib')
    model = Figure
    extra = 1

class AirfieldAdmin(GoogleAdmin):
    fieldsets = (
    
        ('Main', {
            "fields": ('name', 'slug', 'revised', 'body', 'remarks')
        }),
        
        ('Geographic Data', {
            "classes": ('collapse',),
            "fields": ('state', 'lat_lng', 'location', 'runway')
        }),
    
    )
    
    form = AirfieldAdminForm
    list_display = ('name', 'remarks', 'revised')
    prepopulated_fields = {"slug": ("name",)}
    inlines = [FigureInline]
    readonly_fields = ('lat_lng', )
    save_on_top = True


########################################

class FigureAdmin(admin.ModelAdmin):
    list_display = ('airfield', 'name', 'thumb')

########################################

admin.site.register(Airfield, AirfieldAdmin)
admin.site.register(Figure, FigureAdmin)
