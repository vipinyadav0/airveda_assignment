from django.shortcuts import render
from api.models import Device, HumidityReading, TemperatureReading
import requests
import json

# Create your views here.
def index(request):
    url = "http://127.0.0.1:8000/api/devices"

    response = requests.get(url)
    # print(response.json())

    res = requests.get(url + '/4718dc2d-b2f2-43df-8436-f5845acfca50/readings/humidity/?start_on=2023-01-25T00:00:00&end_on=2023-01-31T23:59:59')
    # print(res.json())
    context = {
        'devices' : response.json(),
        'device_data': res.json()
    }
    return render(request,'index.html', context=context)

def devices_graph(request, device_uid=None):
    url = "http://127.0.0.1:8000/api/"
    humidity = requests.get(url + f'devices/{device_uid}/readings/humidity/?start_on=2023-01-25T00:00:00&end_on=2023-01-31T23:59:59')
    temp = requests.get(url + f'devices/{device_uid}/readings/temperature/?start_on=2023-01-25T00:00:00&end_on=2023-01-31T23:59:59')
    # print(temp.json())
    # for x in temp.json():
        # print(x.get('temperature'))


    data = [{"time":"2023-01-25T00:00:00"},
            {"time":"2023-01-24T00:00:00"},
            {"time":"2023-01-23T00:00:00"},
            {"time":"2023-01-26T00:00:00"},
            {"time":"2023-01-27T00:00:00"}]
    json_data = json.dumps(data)
    temp = json.dumps(temp.json())
    humidity = json.dumps(humidity.json())
    context = {
        'humidity' : humidity,
        'temp' : temp,
        'json_data': json_data,
    }
    # print(device_uid)
    # print(request.GET)
    # print(context)
    
    return render(request, 'device-graph.html', context)
