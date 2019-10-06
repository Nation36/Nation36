from django.db import models
from django.urls import reverse

# Create your models here.
class Map (models.Model):
    author = models.ForeignKey()
    name = models.CharField(max_length=100)
    background = models.ImageField(upload_to='')
    layout = models.ImageField(upload_to='', )
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return
