from __future__ import unicode_literals
from django.db import models

from urlparse import urlparse
from django.core.files import File
import urllib

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    pic = models.ImageField(null=False, blank=False, width_field="width", height_field="height")


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp"]


