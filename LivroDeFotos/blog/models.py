from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    title = models.CharField(max_length=100)
    #width = models.IntegerField(default=0)
    #height = models.IntegerField(default=0)
    #image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title