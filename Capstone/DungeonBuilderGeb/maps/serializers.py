from rest_framework import serializers
from .models import Map

class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ['id','author', 'name', 'background', 'layout', 'created']
