#You will need to find your particular city ID number and put it in the two URLs Below
# search for your city by name on this site:
#http://openweathermap.org/help/city_list.txt

from urllib.request import urlopen
import json
def gettemp():
    """ call openweathermap api"""
    response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=5fe7f50c1e68a9928903db3ced74a54b') 
    mydata = response.read()
    return mydata
 
weather = gettemp()
w = json.loads(weather)

#CURRENT TEMPERATURE
#print w['main']['temp'] #in kelvin
temperature = float(w['main']['temp'])
temperature = ((temperature - 273) * 1.8) + 32 #convert from kelvin to Farenheit
print ("Current Temp:")
print (round(temperature))

####################################################################
#FORECAST
def getforecast():
    """ call openweathermap api"""
    response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=5fe7f50c1e68a9928903db3ced74a54b') #put your city ID number at the end
    mydata = response.read()
    return mydata
 
weather = getforecast()
w = json.loads(weather)


#TODAY'S LOW
temperature = float(w['list'][0]['temp']['min'])
temperature = ((temperature - 273) * 1.8) + 32
print ("Daily Low: ")
print (round(temperature))

#TODAY'S HIGH 
temperature = float(w['list'][0]['temp']['max'])
temperature = ((temperature - 273) * 1.8) + 32
print ("Daily High: ")
print (round(temperature))

#rain or clear today?
todayforecast = w['list'][0]['weather'][0]['main']
print ("The weather is: ")
print (todayforecast)

if todayforecast == 'Clear':
	pass
if todayforecast == 'Rain':
	pass
if todayforecast == 'Clouds':
	pass
if todayforecast == 'Snow':
	pass
