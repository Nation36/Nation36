from django.db import models
from django.urls import reverse
from DungeonBuilderGeb import settings
# Create your models here.

class Obj (models.Model):
    name = models.CharField(max_length=50)
    appearance = models.ImageField(upload_to='')

    def __str__(self):
        return self.name

class Map (models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    background = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
    created = models.DateTimeField(auto_now_add = True)
    obj = models.ManyToManyField(Obj, through = 'Layout')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'api/maps/{self.id}'

class Layout (models.Model):
    map = models.ForeignKey(Map, on_delete = models.CASCADE)
    obj = models.ForeignKey(Obj, on_delete = models.CASCADE)
    x_position = models.IntegerField()
    y_position = models.IntegerField()

    def __str__(self):
        return f'{self.map} -- {self.obj} ({self.x_position},{self.y_position})'
