from requests import get
import json
from pprint import pprint

url='https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/316321'

weather = get(url).json()['items']
pprint(weather)

