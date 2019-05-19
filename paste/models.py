from django.db import models

# Create your models here.
class textpaste(models.Model):
    Username = models.CharField(max_length = 15)
    Text = models.CharField(max_length = 264)
