from rest_framework import serializers
from .models import Map, Obj, Layout


class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obj
        fields = ['id', 'appearance', 'name']

class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = ['id', 'map', 'obj', 'x_position', 'y_position']

class LayoutNestedSerializer(serializers.ModelSerializer):
    obj = ObjSerializer(read_only=True)
    class Meta:
        model = Layout
        fields = ['id', 'obj', 'x_position', 'y_position']

class MapSerializer(serializers.ModelSerializer):
    layout_set = LayoutNestedSerializer(read_only = True, many=True)
    class Meta:
        model = Map
        fields = ['id','author', 'name', 'background', 'created', 'layout_set']
