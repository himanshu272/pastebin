from django.db import models

# Create your models here.
class textpaste(models.Model):
    Username = models.CharField(max_length = 20)
    Text = models.TextField()
    language_choices = (
        ('python','PYTHON'),
        ('C++','C/C++'),
        ('java','Java'),
        ('javascript','JavaScript'),
        ('none','TextFile'),
    )
    language = models.CharField(max_length = 10, choices = language_choices, default='none')