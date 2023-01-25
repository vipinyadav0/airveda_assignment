from django.urls import path
from .views import index, devices_graph

app_name = 'home'


urlpatterns = [
    path('', index, name='index'),
    path('devices-graph/<str:device_uid>/',devices_graph, name='devices_graph' )
]
