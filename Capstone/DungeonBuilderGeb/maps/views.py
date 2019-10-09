from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import MapSerializer, LayoutSerializer, ObjSerializer
from .models import Map, Layout, Obj


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all().order_by('created')
    serializer_class = MapSerializer

class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Layout.objects.all().order_by('id')
    serializer_class = LayoutSerializer

class ObjViewSet(viewsets.ModelViewSet):
    queryset = Obj.objects.all().order_by('name')
    serializer_class = ObjSerializer
