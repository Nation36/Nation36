from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'maps'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name = 'home'),
    path('new-map', TemplateView.as_view(template_name='newMap.html'), name = 'newMap'),
    path('new-map/layout', TemplateView.as_view(template_name='layout.html'), name = 'layout'),
    path('my-maps', views.MapListView.as_view(), name = 'map_list'),
#    path('<int:pk>', views.MapDetailView.as_view(), name = 'map_detail')
]
