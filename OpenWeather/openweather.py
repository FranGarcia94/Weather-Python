#============================= OPENWEATHER =============================#
#                                                                       #
#                    Get weather data from Openweather                  #
#                                                                       #
#=======================================================================#

import requests
import json
from datetime import datetime
from tabulate import tabulate


city = input('Enter a city: ') # Asks the user to enter a city.

api_key = "INSERT API KEY HERE" # API Key

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"


# Request

response = requests.get(url)
data = json.loads(response.text)

datas=[]


# Variables

weather=data['weather'][0]['main']          # Short weather description

desc=data['weather'][0]['description']      # Weather description

temp = data['main']['temp']                 # Temperature

tempmax = data['main']['temp_max']          # Maximum recorded temperature value in a short period of time

tempmin = data['main']['temp_min']          # Minimun recorded temperature value in a short period of time

feel_like = data['main']['feels_like']      # Feel like temperature

humidity = data['main']['humidity']         # Humidity

wind = data['wind']['speed']                # Wind speed

clouds = data['clouds']['all']              # Percentage of clouds

sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise'])).strftime('%H:%M:%S') # Sunrise time

sunset = datetime.utcfromtimestamp(int(data['sys']['sunset'])).strftime('%H:%M:%S')   # Sunset time

hora=datetime.utcfromtimestamp(int(data['dt'])).strftime('%H:%M:%S')                  # Data recording time

name=data['name']                           # Name of the place


datas.append([name, str(temp) + ' ºC', desc, sunrise + ' - ' + sunset, str(wind) + ' km/h', str(clouds) + ' %', str(humidity) + ' %', str(tempmax) +' - '+ str(tempmin), hora])


# Print datas with a 'github' format.

print(tabulate(datas, headers=[ 'City', 'Temp. (ºC)', 'Description', 'Sunrise - Sunset', 'Wind Speed', 'Clouds', 'Humidity', 'T.Max - T.Min', 'Measurement Time'],tablefmt="github"))

