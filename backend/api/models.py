from django.db import models

# Create your models here.
class Device(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TemperatureReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.temperature} ˚C"



class HumidityReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.humidity} %"