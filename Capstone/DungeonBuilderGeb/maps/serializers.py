from rest_framework import serializers
from .models import Map, Object

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['id','author', 'name', 'background', 'layout', 'created']

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ['id', 'image', 'name']
