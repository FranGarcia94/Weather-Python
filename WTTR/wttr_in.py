#================================ WTTR ================================#
#                                                                      #
#                    Get weather data from wttr.in                     #
#                                                                      #
#======================================================================#

import requests
from tabulate import tabulate


# We have flexibility with how to put the place, for example: 'Paris', 'Eiffel Tower', 'los angeles, california'.
# As we can see, it is also possible to put famous monuments.

place = 'Paris' # Insert Place here


# Request

url = f'https://wttr.in/{place}?format=j1'

res = requests.get(url)
json_format = res.json()


# Variables

temp=json_format["current_condition"][0]['temp_C']                          # Temperature in Celsius

desc=json_format["current_condition"][0]['weatherDesc'][0]["value"]         

hour_of_data=json_format["current_condition"][0]['observation_time']        

hour_of_request=json_format["current_condition"][0]['localObsDateTime']     

sunrise=json_format["weather"][0]["astronomy"][0]['sunrise']                

sunset=json_format["weather"][0]["astronomy"][0]['sunset']                  

wind_speed=json_format["current_condition"][0]["windspeedKmph"]             

humidity=json_format["current_condition"][0]["humidity"]                    

uv_index=json_format["current_condition"][0]["uvIndex"]                     # UV Index (1-10)

data_2=[]

data_2.append([place, temp + ' ºC', desc, sunrise + ' - ' + sunset, wind_speed + ' km/h', humidity + ' %', uv_index + '/10', hour_of_data])

# Print data with a 'github' format.
print(tabulate(data_2, headers = [ 'Place', 'Temp. (ºC)', 'Description', 'Sunrise - Sunset', 'Wind Speed', 'Humidity', 'UV Index', 'Measurement Time'],tablefmt="github"))

