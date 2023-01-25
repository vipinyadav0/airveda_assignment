from django.shortcuts import render
from api.models import Device, HumidityReading, TemperatureReading
import requests

# Create your views here.
def index(request):
    url = "http://127.0.0.1:8000/api/devices"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
    "uid": "1001",
    "name": "Device 4",
}
    response = requests.post(url, headers=headers, json=data)

    # print("Status Code", response.status_code)
    # print("JSON Response ", response.json())
    response = requests.get(url)
    print(response.json())

    # devices = Device.objects.all()
    context = {
        'devices' : response.json()
    }
    return render(request,'index.html', context=context)