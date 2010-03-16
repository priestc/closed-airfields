import os
from django.contrib.gis.db import models
from django.contrib.gis.utils import LayerMapping

class USState(models.Model):
    code = models.CharField(max_length=2)
    mpoly = models.MultiPolygonField(srid=4269)
    
    objects = models.GeoManager()
    
    class Meta:
        verbose_name_plural = "US State Borders"
    
    def __unicode__(self):
        return self.code
    
    @classmethod
    def goon(cls, *args, **kwargs):
        from annoying.functions import get_object_or_None
        return get_object_or_None(cls,  *args, **kwargs)
    

usstate_mapping = {
    'code' : 'STATE',
    'mpoly' : 'MULTIPOLYGON',
}

def import_state(verbose=True):
    us_shp = os.path.abspath(
                                os.path.join(os.path.dirname(__file__),
                                'data/states/s_01au07.shp')
                            )
                            
    lm = LayerMapping(USState, us_shp, usstate_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
