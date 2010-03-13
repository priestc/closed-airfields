import Image
import os
import re

from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.gis.db import models

THUMB = """<a title="Click for full"
              href="{fullurl}"
              target="_blank">
              <img src="{thumburl}" alt="thumbnail image"/>
           </a>""".replace("\n", "")

class Airfield(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=40)
    location = models.PointField(null=False, blank=False)
    body = models.TextField()
    revised = models.DateField()
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('airfield', [self.slug])
        
    def render_with_images(self):
        
        #add an 'i' to the front of each tag to please format()
        body = re.sub(r'{(.+)}', r'{i\1}', self.body)
        
        d = {}
        img_mapping = {}
        for im in self.figure_set.all():
            img_inset = im.make_inset()
            img_mapping["i" + im.name] = img_inset
        
        return mark_safe(body.format(**img_mapping))

class Figure(models.Model):
    image = models.ImageField(upload_to="images")
    caption = models.TextField()
    name = models.CharField(max_length=16)
    airfield = models.ForeignKey("Airfield")
    contrib = models.CharField(max_length=56, blank=True)
    
    def make_thumb(self, size):
        """
        Make a thumbnail according to the passed size, then return that
        image as an <img> tag.
        """
        
        SMALLER_SIZE = (500,500)
        TINY_SIZE = (80,80)
        
        # the name of the file, eg: 'jgs99.jpg'
        image_name = os.path.split(self.image.path)[-1]
        
        # full path of image from root, eg: /srv/project/media/image/jgs99.jpg
        full_path = self.image.path
        
        # full path of thumbnail, eg: /srv/project/media/image/tiny/jgs99.jpg
        thumb_path = os.path.join(os.path.dirname(full_path), size, image_name)
        
        exists = os.path.exists(thumb_path)
        
        # create thumbnail if it doesn't already exist
        if not exists and size == 'tiny':
            im = Image.open(full_path)
            im.thumbnail(TINY_SIZE, Image.ANTIALIAS)
            im.save(thumb_path, 'JPEG')
        elif not exists and size == 'smaller':
            im = Image.open(full_path)
            im.thumbnail(SMALLER_SIZE, Image.ANTIALIAS)
            im.save(thumb_path, 'JPEG')
        
        # url for the thumbnail, eg: /media/images/tiny/
        thumb_url = os.path.join(settings.MEDIA_URL, 'images', size, image_name)
        
        return THUMB.format(fullurl=self.image.url, thumburl=thumb_url)
    
    def thumb(self):
        """
        Return a tiny thumbnail for display in the admin interface
        """
        return self.make_thumb('tiny')
    thumb.allow_tags = True
    thumb.short_description = 'Thumb'
    
    
    def make_inset(self):
        
        contrib = ""
        if self.contrib:
            contrib = "<br><small><strong>Image Courtesy of {0}</strong></small>"\
                            .format(self.contrib)
        
        l = [
             '<div class="figure">',
                '{thumb}',
                '<div class="caption">{caption}{contrib}</div>',
             '</div>',
             ]
             
        caption = self.caption
        thumb = self.make_thumb('smaller')
             
        return "".join(l).format(**locals())
