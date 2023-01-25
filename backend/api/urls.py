from django.urls import path, include
from rest_framework import routers
from .views import DeviceViewSet, DeviceAPIView, DeviceReadingViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('devices/<str:uid>/', DeviceAPIView.as_view()),
    path('devices/<str:device_uid>/readings/<str:parameter>/', DeviceReadingViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]