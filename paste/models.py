from django.db import models

# Create your models here.

class Paste(models.Model):
    text = models.CharField(max_length=2000)
    title = models.CharField(max_length=40)
    date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
