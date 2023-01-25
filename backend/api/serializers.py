from rest_framework import serializers
from .models import Device, HumidityReading, TemperatureReading

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('uid', 'name')

class TemperatureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = ('temperature',)

class HumidityReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityReading
        fields = ('humidity',)