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


    data = [{"time":"2022-01-01T00:00:00","temperature":20,"humidity":50},
            {"time":"2022-01-02T00:00:00","temperature":22,"humidity":45},
            {"time":"2022-01-03T00:00:00","temperature":24,"humidity":40},
            {"time":"2022-01-04T00:00:00","temperature":25,"humidity":35},
            {"time":"2022-01-05T00:00:00","temperature":28,"humidity":30}]
    json_data = json.dumps(data)
    print(json.dumps(temp.json()))
    context = {
        'humidity' : humidity.json(),
        'temp' : temp.json(),
        'json_data': json_data,
    }
    # print(device_uid)
    # print(request.GET)
    # print(context)
    
    return render(request, 'device-graph.html', context)
