from requests import get
import json
from pprint import pprint
from haversine import haversine

from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret

)

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = 52.066844
my_lon = 1.203174

all_stations = get(stations).json()['items']

def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station
    


closest_stn = find_closest()
weather = weather + str(closest_stn)
my_weather = get(weather).json()['items'] [0] ['ambient_temp']

   

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

pprint (my_weather)
message = (my_weather)
twitter.update_status(status=message)
print("Tweeted: %s" % message)



