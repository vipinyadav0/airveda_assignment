from django.shortcuts import render
from datetime import datetime
from rest_framework import viewsets, status
from .models import Device, HumidityReading, TemperatureReading
from .serializers import DeviceSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import HumidityReadingSerializer, TemperatureReadingSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'uid'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        device = self.get_object()
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

class DeviceAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'uid'

class DeviceReadingViewSet(viewsets.ViewSet):
    def list(self, request, device_uid, parameter):
        try:
            device = Device.objects.get(uid=device_uid)
        except Device.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print(request.GET)
        print(device_uid)
        print(parameter)

        start_on = datetime.strptime(request.GET.get('start_on'), '%Y-%m-%dT%H:%M:%S')
        end_on = datetime.strptime(request.GET.get('end_on'), '%Y-%m-%dT%H:%M:%S')

        if parameter == 'temperature':
            readings = TemperatureReading.objects.filter(
                device=device, created_at__range=(start_on, end_on)
            )
            serializer = TemperatureReadingSerializer(readings, many=True)
        elif parameter == 'humidity':
            readings = HumidityReading.objects.filter(
                device=device, created_at__range=(start_on, end_on)
            )
            serializer = HumidityReadingSerializer(readings, many=True)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)