from requests import get
import json
import folium
import os
import webbrowser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

stations = get(url).json()

lons = [station['weather_stn_long'] for station in stations['items']]
lats = [station['weather_stn_lat'] for station in stations['items']]
wsnames = [station['weather_stn_name'] for station in stations['items']]

map_ws = folium.Map(location=[54,-2], zoom_start=6)

CWD = os.getcwd()

for n in range(len(lons)):
    folium.Marker([lats[n],
                lons[n]],
                popup = wsnames[n]).add_to(map_ws)
    
map_ws.save('wsmap1.html')
webbrowser.open_new('file://'+CWD+'/'+'wsmap1.html')
