import json
from urllib.request import urlopen
from datetime import datetime
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#  The Above 2 lines are required If we want to use Secured https protocol
# Comment these 2 statements if you don't want to use https in line 37 i.e. use http instead
class weather:

    def __init__(self):
        self.cityid = None
        self.cityname = None
        self.link = None
        self.temperature = None
        self.temperature_max = None
        self.temperature_min = None
        self.temperature_desc = None
        self.wind_speed = None
        self.wind_degree = None
        self.sunrise = None
        self.sunset = None

    def findid(self):
        self.cityname = input("Enter City: ").lower()

        with open('CityList.json','r') as f:
            a = json.load(f)

        for data in a:
            x = data['name']

            if x.lower() == self.cityname:
                self.cityid = data['id']
                #print (self.cityid)
                break

    def getURL(self):
        if(self.cityid==None):
            print("Please enter a valid City\n")

        else:
            APIKEY = 'YOUR API KEY'
            url = 'https://api.openweathermap.org/data/2.5/weather?id='
            self.link = url + str(self.cityid) + '&appid=' + APIKEY
            #print(self.link)
            self.getTemp()

    def getTemp(self):
        response = urlopen(self.link)
        data = json.load(response)

        self.temperature = data['main']['temp']
        self.temperature_max = data['main']['temp_max']
        self.temperature_min = data['main']['temp_min']
        self.temperature_desc = data['weather'][0]['description']
        self.wind_speed = data['wind']['speed']
        self.wind_degree = data['wind']['deg']
        self.sunrise = data['sys']['sunrise']
        self.sunset = data['sys']['sunset']

        self.temperature-= 273.15
        self.temperature_max-= 273.15
        self.temperature_min-= 273.15
        print("\n")
        print("The Temperature is: ",round(self.temperature,2), "ºC") # Alt + 0 for degree symbol
        print("Description: ",self.temperature_desc.capitalize())
        print("Wind Speed: ",round((self.wind_speed*3.6),2)," km/hr")
        print("Wind Direction: ",round(self.wind_degree,2),"º")
        print("Sunrise @: ",datetime.utcfromtimestamp(self.sunrise).strftime('%H:%M:%S'),"UTC")
        print("Sunset @: ",datetime.utcfromtimestamp(self.sunset).strftime('%H:%M:%S'),"UTC")

        # The API call returns the time of Sunrise and Sunset in form of UNIX Timestamp
        # UNIX Timestamp is basically number of seconds that have elapsed since January 1,1970


def main():
    w = weather()
    w.findid()
    w.getURL()
main()
