import sys
from collections import namedtuple
import request
Waether = numedtuple('Weater', ['location_name', 'the_temp', 'air_pressure', 'humidity'])

def location_id(location_name):
    pass

def get_location_weather(location_id):
    pass

def_weather_report(weather):
    pass



resp = request.get('https://www.metaweather.com/api/location/search/?query=london')
print(resp.json())

location_name = sys.agrv[1]
location_id = get_location_weather(location_name)
weater = get_location_weather(location_id, location_name)
report = def_weather_report(weater)

print(report)