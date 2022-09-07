from django.db import models

class info(models.Model):
    name = models.CharField(max_length=264)
    age = models.IntegerField()
