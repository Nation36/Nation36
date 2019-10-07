from django.db import models
from django.urls import reverse

# Create your models here.

class Object (models.Model):
    name = models.CharField(max_length=50)
    appearance = models.ImageField(upload_to='')

    def __str__(self):
        return self.name

class Map (models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    background = models.ImageField(upload_to='')
    created = models.DateTimeField(auto_now_add = True)
    objects = models.ManyToManyField(Object, through = 'Layout')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return

class Layout (models.Model):
    map = models.ForeignKey(Map, on_delete = models.CASCADE)
    object = models.ForeignKey(Object, on_delete = models.CASCADE)
    x_position = models.IntegerField()
    y_position = models.IntegerField()
