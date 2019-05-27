from django.db import models

# Create your models here.
class textpaste(models.Model):
    Username = models.CharField(max_length = 20)
    Text = models.TextField()