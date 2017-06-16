from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'
weather = get(url).json()

## list comprehension to get all the temperatures in a list
temperatures = [record['ambient_temp'] for record in weather['items']]



## list comprehension to get all the temperatures in a list in a readable format
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]

plt.plot(timestamps, temperatures)
## Set the axis labels
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
