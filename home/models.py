from django.db import models
from django.db.models import ImageField

# Create your models here.

# Create your models here.
class Carousel_Item (models.Model):
    caption = models.CharField(max_length=200,blank=False)
    order = models.IntegerField()
    carousel_image = models.ImageField(upload_to='media')
    def __unicode__(self):
        return self.caption
