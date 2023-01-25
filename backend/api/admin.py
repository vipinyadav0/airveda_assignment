from django.contrib import admin
from .models import Device, TemperatureReading, HumidityReading

# Register your models here.
class TemperatureReadingAdmin(admin.ModelAdmin):
    list_display = ('id','temperature', 'created_at')
class HumidityReadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'humidity', 'created_at')
admin.site.register(Device)
admin.site.register(TemperatureReading, TemperatureReadingAdmin)

admin.site.register(HumidityReading, HumidityReadingAdmin)

