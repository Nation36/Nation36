from rest_framework import viewsets
from .serializers import MapSerializer
from .models import Map

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all().order_by('last_name')
    serializer_class = MapSerializer
