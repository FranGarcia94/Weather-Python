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

data_2=[]


# Variables

weather=data['weather'][0]['main']          # Short weather description

desc=data['weather'][0]['description']      

temp = data['main']['temp']                 

tempmax = data['main']['temp_max']          

tempmin = data['main']['temp_min']          

feel_like = data['main']['feels_like']      

humidity = data['main']['humidity']         

wind = data['wind']['speed']                

clouds = data['clouds']['all']              

sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise'])).strftime('%H:%M:%S') 

sunset = datetime.utcfromtimestamp(int(data['sys']['sunset'])).strftime('%H:%M:%S')   

hora=datetime.utcfromtimestamp(int(data['dt'])).strftime('%H:%M:%S')                  

name=data['name']                           


data_2.append([name, str(temp) + ' ºC', desc, sunrise + ' - ' + sunset, str(wind) + ' km/h', str(clouds) + ' %', str(humidity) + ' %', str(tempmax) +' - '+ str(tempmin), hora])


# Print data with a 'github' format.

print(tabulate(data_2, headers=[ 'City', 'Temp. (ºC)', 'Description', 'Sunrise - Sunset', 'Wind Speed', 'Clouds', 'Humidity', 'T.Max - T.Min', 'Measurement Time'],tablefmt="github"))

