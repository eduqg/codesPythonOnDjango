from __future__ import unicode_literals
from django.db import models

from urlparse import urlparse
from django.core.files import File
import urllib

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=100)
    pic=models.ImageField()
    def __unicode__(self):
        return self.name

